from ._overlap import compute_solid_angle

__all__ = ['compute_solid_angle_wcs']


def compute_solid_angle_wcs(wcs):
    """Compute solid angle image.
    
    Parameters
    ----------
    wcs : `astropy.wcs.WCS`
        WCS object describing the image
    
    Returns
    -------
    solid_angle : `numpy.array`
        Array with pixel solid angle as value
    """

    naxis1 = wcs.naxis1
    naxis2 = wcs.naxis2
    # Compute array of pixel corner coordinates
    # (note that this array is one longer than the pixel array
    shape = (naxis2 + 1, naxis1 + 1)
    y, x = np.indices(shape, dtype='int32')

    lon, lat = wcs.wcs_pix2world(x, y, 0)

    # TODO: need to flatten and reshape to (npix x 4)
    pix_lon = lon[:-1, :], lon[1:, :], lon[1:, :], lon[:-1, :]
    pix_lat = lat[:, :-1], lat[:, :-1], lat[:, 1:], lat[:, 1:]
    solid_angle = compute_solid_angle(pix_lon, pix_lat)
    
    return solid_angle.reshape((naxis2, naxis1))
