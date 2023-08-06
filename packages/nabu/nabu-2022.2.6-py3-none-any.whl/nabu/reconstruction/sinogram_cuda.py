import numpy as np
import pycuda.gpuarray as garray
from ..cuda.kernel import CudaKernel
from ..utils import get_cuda_srcfile, updiv, deprecated_class
from .sinogram import SinoBuilder, SinoNormalization
from .sinogram import _convert_halftomo_right # FIXME Temporary patch
from ..cuda.processing import CudaProcessing


class CudaSinoBuilder(SinoBuilder):
    def __init__(self, sinos_shape=None, radios_shape=None, rot_center=None, halftomo=False, cuda_options=None):
        """
        Initialize a CudaSinoBuilder instance.
        Please see the documentation of nabu.reconstruction.sinogram.Builder
        and nabu.cuda.processing.CudaProcessing.
        """
        super().__init__(
            sinos_shape=sinos_shape, radios_shape=radios_shape, rot_center=rot_center,
            halftomo=halftomo,
        )
        self.cuda_processing = CudaProcessing(**(cuda_options or {}))
        self._init_cuda_halftomo()


    def _init_cuda_halftomo(self):
        if not(self.halftomo):
            return
        kernel_name = "halftomo_kernel"
        self.halftomo_kernel = CudaKernel(
            kernel_name,
            get_cuda_srcfile("halftomo.cu"),
            signature="PPPiii",
        )
        rc = self._rot_center_int
        blk = (32, 32, 1) # tune ?
        self._halftomo_blksize = blk
        self._halftomo_gridsize = (
            updiv(2 * rc, blk[0]),
            updiv((self.n_angles + 1)//2, blk[1]),
            1
        )
        d = self.n_x - rc # will have to be adapted for varying axis pos
        self.halftomo_weights = np.linspace(0, 1, 2*abs(d), endpoint=True, dtype="f")
        self.d_halftomo_weights = garray.to_gpu(self.halftomo_weights)
        if self._halftomo_flip:
            self.xflip_kernel = CudaKernel(
                "reverse2D_x",
                get_cuda_srcfile("ElementOp.cu"),
                signature="Pii"
            )
            blk = (32, 32, 1)
            self._xflip_blksize = blk
            self._xflip_gridsize_1 = (
                updiv(self.n_x, blk[0]),
                updiv(self.n_angles, blk[1]),
                1
            )
            self._xflip_gridsize_2 = self._halftomo_gridsize


    # Overwrite parent method
    def _radios_to_sinos_simple(self, radios, output, copy=False):
        if not(copy) and output is None:
            return radios.transpose(axes=(1, 0, 2)) # view
        if output is None: # copy and output is None
            na, nz, nx = radios.shape
            output = garray.zeros((nz, na, nx), "f")
        # not(copy) and output is not None
        for i in range(output.shape[0]):
            output[i, :, :] = radios[:, i, :]
        return output


    # Overwrite parent method
    def _radios_to_sinos_halftomo(self, radios, sinos):
        n_a, n_z, n_x = radios.shape
        n_a2 = (n_a + 1) // 2
        rc = self._rot_center_int
        out_dwidth = 2 * rc
        if sinos is not None:
            if sinos.shape[-1] != out_dwidth:
                raise ValueError(
                    "Expected sinos sinogram last dimension to have %d elements"
                    % out_dwidth
                )
            if sinos.shape[-2] != n_a2:
                raise ValueError("Expected sinograms to have %d angles" % n_a2)
        else:
            sinos = garray.zeros(self.sinos_halftomo_shape, dtype=np.float32)

        # FIXME: TEMPORARY PATCH, waiting for cuda implementation
        if self._rot_center_int > self.n_x:
            return self._radios_to_sinos_halftomo_external_cor(radios, sinos)
        #

        # need to use a contiguous 2D, array otherwise kernel does not work
        if n_a & 1:
            d_sino = garray.zeros((n_a + 1, n_x), "f")
        else:
            d_sino = radios[:, 0, :].copy()
        for i in range(n_z):
            d_sino[:n_a] = radios[:, i, :]
            if n_a & 1:
                d_sino[-1, :].fill(0)
            if self._halftomo_flip:
                self.xflip_kernel(
                    d_sino, n_x, n_a,
                    grid=self._xflip_gridsize_1, block=self._xflip_blksize
                )
            self.halftomo_kernel(
                d_sino,
                sinos[i],
                self.d_halftomo_weights,
                n_a, n_x, rc,
                grid=self._halftomo_gridsize,
                block=self._halftomo_blksize
            )
            if self._halftomo_flip:
                self.xflip_kernel(
                    sinos[i], 2*rc, n_a2,
                    grid=self._xflip_gridsize_2, block=self._xflip_blksize
                )
        return sinos


    def _radios_to_sinos_halftomo_external_cor(self, radios, sinos):
        """
        TEMPORARY PATCH waiting to have a cuda implementation
        Processing is done by getting reach radio on host, which is suboptimal
        """
        n_a, n_z, n_x = radios.shape
        n_a2 = n_a // 2
        rc = self._rot_center_int
        out_dwidth = 2 * rc

        # need to use a contiguous 2D, array otherwise kernel does not work
        sino = radios[:, 0, :].get()
        for i in range(n_z):
            radios[:, i, :].get(sino)
            if self._halftomo_flip:
                sino = sino[:, ::-1]
            sino_half = _convert_halftomo_right(sino, self._rot_center_int)
            sinos[i, :, :] = sino_half[:]
            if self._halftomo_flip:
                self.xflip_kernel(
                    sinos[i], 2*rc, n_a2,
                    grid=self._xflip_gridsize_2, block=self._xflip_blksize
                )
        return sinos


CudaSinoProcessing = deprecated_class(
    "'CudaSinoProcessing' was renamed 'CudaSinoBuilder'", do_print=True
)(CudaSinoBuilder)


class CudaSinoNormalization(SinoNormalization):
    def __init__(self, kind="chebyshev", sinos_shape=None, radios_shape=None, normalization_array=None, cuda_options=None):
        super().__init__(
            kind=kind, sinos_shape=sinos_shape, radios_shape=radios_shape, normalization_array=normalization_array
        )
        self._get_shapes(sinos_shape, radios_shape)
        self.cuda_processing = CudaProcessing(**(cuda_options or {}))
        self._init_cuda_normalization()


    _get_shapes = SinoBuilder._get_shapes

    #
    # Chebyshev normalization
    #

    def _init_cuda_normalization(self):
        self._d_tmp = garray.zeros(self.sinos_shape[-2:], "f")
        if self.normalization_kind == "chebyshev":
            self._chebyshev_kernel = CudaKernel(
                "normalize_chebyshev",
                filename=get_cuda_srcfile("normalization.cu"),
                signature="Piii",
            )
            self._chebyshev_kernel_args = [
                np.int32(self.n_x), np.int32(self.n_angles), np.int32(self.n_z)
            ]
            blk = (1, 64, 16) # TODO tune ?
            self._chebyshev_kernel_kwargs = {
                "block": blk,
                "grid": (1, int(updiv(self.n_angles, blk[1])), int(updiv(self.n_z, blk[2]))),
            }
        elif self.normalization_array is not None:
            normalization_array = self.normalization_array
            # If normalization_array is 1D, make a 2D array by repeating the line
            if normalization_array.ndim == 1:
                normalization_array = np.tile(normalization_array, (self.n_angles, 1))
            self._d_normalization_array = garray.to_gpu(normalization_array.astype("f"))
            if self.normalization_kind == "subtraction":
                generic_op_val = 1
            elif self.normalization_kind == "division":
                generic_op_val = 3
            self._norm_kernel = CudaKernel(
                "inplace_generic_op_2Dby2D",
                filename=get_cuda_srcfile("ElementOp.cu"),
                signature="PPii",
                options=["-DGENERIC_OP=%d" % generic_op_val]
            )
            self._norm_kernel_args = [
                self._d_normalization_array, np.int32(self.n_angles), np.int32(self.n_x)
            ]
            blk = (32, 32, 1)
            self._norm_kernel_kwargs = {
                "block": blk,
                "grid": (int(updiv(self.n_angles, blk[0])), int(updiv(self.n_x, blk[1])), 1)
            }

    def _normalize_chebyshev(self, sinos):
        if sinos.flags.c_contiguous:
            self._chebyshev_kernel(
                sinos, *self._chebyshev_kernel_args, **self._chebyshev_kernel_kwargs
            )
        else:
            # This kernel seems to have an issue on arrays that are not C-contiguous.
            # We have to process image per image.
            nz = np.int32(1)
            nthreadsperblock = (1, 32, 1) # TODO tune
            nblocks = (1, int(updiv(self.n_angles, nthreadsperblock[1])), 1)
            for i in range(sinos.shape[0]):
                self._d_tmp[:] = sinos[i][:]
                self._chebyshev_kernel(
                    self._d_tmp,
                    np.int32(self.n_x), np.int32(self.n_angles), np.int32(1),
                    grid=nblocks,
                    block=nthreadsperblock
                )
                sinos[i][:] = self._d_tmp[:]
        return sinos


    #
    # Array subtraction/division
    #

    def _normalize_op(self, sino):
        if sino.ndim == 2:
            # Things can go wrong if "sino" is a non-contiguous 2D array
            # But this should be handled outside this function, as the processing is in-place
            self._norm_kernel(sino, *self._norm_kernel_args, **self._norm_kernel_kwargs)
        else:
            if sino.flags.forc:
                # Contiguous 3D array. But pycuda wants the same shape for both operands.
                for i in range(sino.shape[0]):
                    self._norm_kernel(sino[i], *self._norm_kernel_args, **self._norm_kernel_kwargs)
            else:
                # Non-contiguous 2D array. Make a temp. copy
                for i in range(sino.shape[0]):
                    self._d_tmp[:] = sino[i][:]
                    self._norm_kernel(self._d_tmp, *self._norm_kernel_args, **self._norm_kernel_kwargs)
                    sino[i][:] = self._d_tmp[:]
        return sino

