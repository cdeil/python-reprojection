#ifndef OVERLAP_AREA
#define OVERLAP_AREA

double computeOverlap(double *ilon, double *ilat, double *olon, double *olat,
                      int energyMode, double refArea, double *areaRatio);

double computeSolidAngle(double *lon, double *lat, double *solid_angle, int n0, int n1);

#endif
