import numpy as np
cimport numpy as np
import cython

ctypedef np.double_t DOUBLE_T

cdef extern from "overlapArea.h":
    double computeOverlap(double * ilon, double * ilat, double * olon, double * olat,
                          int energyMode, double refArea, double * areaRatio)
    double computeSolidAngle(double * lon, double * lat, double * solid_angle, int n0, int n1)

@cython.wraparound(False)
@cython.boundscheck(False)
def compute_overlap(np.ndarray[double, ndim=2] ilon,
                    np.ndarray[double, ndim=2] ilat,
                    np.ndarray[double, ndim=2] olon,
                    np.ndarray[double, ndim=2] olat):
    """Compute the overlap between two 'pixels' in spherical coordinates.
    
    Parameters
    ----------
    ilon : np.ndarray
        The longitudes (in radians) defining the four corners of the input pixel
    ilat : np.ndarray
        The latitudes (in radians) defining the four corners of the input pixel
    olon : np.ndarray
        The longitudes (in radians) defining the four corners of the output pixel
    olat : np.ndarray
        The latitudes (in radians) defining the four corners of the output pixel
    
    Returns
    -------
    overlap : np.ndarray
        Pixel overlap solid angle in steradians
    area_ratio : np.ndarray
        TODO
    """
    cdef int i
    cdef int n = ilon.shape[0]

    cdef np.ndarray[double, ndim = 1] overlap = np.empty(n, dtype=np.double)
    cdef np.ndarray[double, ndim = 1] area_ratio = np.empty(n, dtype=np.double)

    for i in range(n):
        overlap[i] = computeOverlap(& ilon[i, 0], & ilat[i, 0], & olon[i, 0], & olat[i, 0],
                                    0, 1, & area_ratio[i])

    return overlap, area_ratio


@cython.wraparound(False)
@cython.boundscheck(False)
def compute_solid_angle(np.ndarray[double, ndim=2] lon,
                        np.ndarray[double, ndim=2] lat):
    """Compute solid angle of pixels in spherical coordinates.
    
    Parameters
    ----------
    lon : np.ndarray
        Pixel corner longitude coordinate array (in radians)
    lat : np.ndarray
        Pixel corner latitude coordinate array (in radians)
    
    Returns
    -------
    solid_angle : np.ndarray
        Pixel solid angle in steradians
    """
    #assert lon.shape == lat.shape
    
    #cdef int ii, jj
    cdef int n0 = lon.shape[0]
    cdef int n1 = lon.shape[1]


    cdef np.ndarray[double, ndim = 2] solid_angle = np.empty((n0, n1), dtype=np.double)

    computeSolidAngle(&lon[0, 0], &lat[0, 0], &solid_angle[0, 0], n0, n1)
    #for ii in range(lon.shape[0]):
    #    for jj in range(lon.shape[1]):
    #        solid_angle[ii, jj] = 42 #computeSolidAngle(&lon[ii, jj])

    return solid_angle
