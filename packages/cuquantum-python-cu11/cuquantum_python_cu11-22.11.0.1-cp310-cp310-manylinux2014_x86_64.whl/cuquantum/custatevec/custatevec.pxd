# Copyright (c) 2021-2022, NVIDIA CORPORATION & AFFILIATES
#
# SPDX-License-Identifier: BSD-3-Clause

# The C types are prefixed with an underscore because we are not
# yet protected by the module namespaces as done in CUDA Python.
# Once we switch over the names would be prettier (in the Cython
# layer).

from libc.stdint cimport intptr_t, int32_t, uint32_t, int64_t

from cuquantum.utils cimport (DataType, DeviceAllocType, DeviceFreeType, int2,
                              LibPropType, Stream)


cdef extern from '<custatevec.h>' nogil:
    # cuStateVec types
    ctypedef void* _Handle 'custatevecHandle_t'
    ctypedef int64_t _Index 'custatevecIndex_t'
    ctypedef int _Status 'custatevecStatus_t'
    ctypedef void* _SamplerDescriptor 'custatevecSamplerDescriptor_t'
    ctypedef void* _AccessorDescriptor 'custatevecAccessorDescriptor_t'
    ctypedef struct _DeviceMemHandler 'custatevecDeviceMemHandler_t':
        void* ctx
        DeviceAllocType device_alloc
        DeviceFreeType device_free

        # Cython limitation: cannot use C defines in declaring a static array,
        # so we just have to hard-code CUSTATEVEC_ALLOCATOR_NAME_LEN here...
        char name[64]
    ctypedef void(*LoggerCallbackData 'custatevecLoggerCallbackData_t')(
        int32_t logLevel,
        const char* functionName,
        const char* message,
        void* userData)

    # cuStateVec enums
    ctypedef enum _ComputeType 'custatevecComputeType_t':
        pass

    ctypedef enum _Pauli 'custatevecPauli_t':
        CUSTATEVEC_PAULI_I
        CUSTATEVEC_PAULI_X
        CUSTATEVEC_PAULI_Y
        CUSTATEVEC_PAULI_Z

    ctypedef enum _MatrixLayout 'custatevecMatrixLayout_t':
        CUSTATEVEC_MATRIX_LAYOUT_COL
        CUSTATEVEC_MATRIX_LAYOUT_ROW

    ctypedef enum _MatrixType 'custatevecMatrixType_t':
        CUSTATEVEC_MATRIX_TYPE_GENERAL
        CUSTATEVEC_MATRIX_TYPE_UNITARY
        CUSTATEVEC_MATRIX_TYPE_HERMITIAN

    ctypedef enum _CollapseOp 'custatevecCollapseOp_t':
        CUSTATEVEC_COLLAPSE_NONE
        CUSTATEVEC_COLLAPSE_NORMALIZE_AND_ZERO

    ctypedef enum _SamplerOutput 'custatevecSamplerOutput_t':
        CUSTATEVEC_SAMPLER_OUTPUT_RANDNUM_ORDER
        CUSTATEVEC_SAMPLER_OUTPUT_ASCENDING_ORDER

    ctypedef enum _DeviceNetworkType 'custatevecDeviceNetworkType_t':
        CUSTATEVEC_DEVICE_NETWORK_TYPE_SWITCH
        CUSTATEVEC_DEVICE_NETWORK_TYPE_FULLMESH

    # cuStateVec consts
    int CUSTATEVEC_VER_MAJOR
    int CUSTATEVEC_VER_MINOR
    int CUSTATEVEC_VER_PATCH
    int CUSTATEVEC_VERSION
    int CUSTATEVEC_ALLOCATOR_NAME_LEN
