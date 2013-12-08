__all__ = ['make_header', 'make_image']


def make_header(nxpix=100, nypix=100, binsz=0.1, xref=0, yref=0,
           proj='CAR', coordsys='GAL',
           xrefpix=None, yrefpix=None):
    """Make a new FITS header dictionary.

    Uses the same parameter names as the Fermi tool gtbin.

    If no reference pixel position is given it is assumed ot be
    at the center of the image.
    """
    nxpix = int(nxpix)
    nypix = int(nypix)
    if not xrefpix:
        xrefpix = (nxpix + 1) / 2.
    if not yrefpix:
        yrefpix = (nypix + 1) / 2.

    if coordsys == 'CEL':
        ctype1, ctype2 = 'RA---', 'DEC--'
    elif coordsys == 'GAL':
        ctype1, ctype2 = 'GLON-', 'GLAT-'
    else:
        raise Exception('Unsupported coordsys: %s' % proj)

    header = {
        'NAXIS': 2, 'NAXIS1': nxpix, 'NAXIS2': nypix,
        'CTYPE1': ctype1 + proj,
        'CRVAL1': xref, 'CRPIX1': xrefpix, 'CUNIT1': 'deg', 'CDELT1':-binsz,
        'CTYPE2': ctype2 + proj,
        'CRVAL2': yref, 'CRPIX2': yrefpix, 'CUNIT2': 'deg', 'CDELT2': binsz,
        }
    return header


def make_image(header, dtype='float32'):
    """Make a new image.
    """
    from astropy.io.fits import ImageHDU
    # Note that FITS and NumPy axis order are reversed
    shape = (header['NAXIS2'], header['NAXIS1'])
    data = np.ones(shape, dtype=dtype)
    return ImageHUD(header=header, data=data)

