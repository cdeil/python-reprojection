import numpy as np
from .. import compute_overlap, compute_solid_angle

def test_compute_overlap():
    EPS = np.radians(1e-2)
    lon, lat = np.array([[0, EPS, EPS, 0]]), np.array([[0, 0, EPS, EPS]])
    overlap, area_ratio = compute_overlap(lon, lat, lon, lat)
    np.testing.assert_allclose(overlap, EPS ** 2, rtol=1e-6)
    np.testing.assert_allclose(area_ratio, 1, rtol=1e-6)

def test_compute_overlap2():
    EPS = np.radians(1e-2)
    ilon, ilat = np.array([[0, EPS, EPS, 0]]), np.array([[0, 0, EPS, EPS]])
    olon, olat = np.array([[0.5 * EPS, 1.5 * EPS, 1.5 * EPS, 0.5 * EPS]]), np.array([[0, 0, EPS, EPS]])
    
    overlap, area_ratio = compute_overlap(ilon, ilat, olon, olat)
    np.testing.assert_allclose(overlap, 0.5 * EPS ** 2, rtol=1e-6)
    np.testing.assert_allclose(area_ratio, 1, rtol=1e-6)

def test_compute_solid_angle():
    EPS = np.radians(1e-2)
    lon, lat = np.array([[0, EPS], [EPS, 0]]), np.array([[0, 0], [EPS, EPS]])
    solid_angle = compute_solid_angle(lon, lat)
    np.testing.assert_allclose(solid_angle, EPS ** 2, rtol=1e-6)
