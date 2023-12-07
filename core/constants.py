QGIS_TOC_GROUPS = ['Raw_Data', 'Reprojected_Data', 'Sampling', 'Kriging', 'Validation', 'Error_Compensation',
                   'Gain_Surface']
DIRECTORY_STRUCTURE = ['00_Data', '01_Kriging', '02_Validation', '03_Error_Compensation', '04_Gain_Surface',
                       '05_Results']
POLYGONS_BUILDER_METHODS = ['Boucle rang', 'Ligne parcelle']

OPERATION = {
    'EPSG:32630': '+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad +step +proj=utm +zone=30 +ellps=WGS84',
    'EPSG:32631': '+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad +step +proj=utm +zone=31 +ellps=WGS84',
    'EPSG:32632': '+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad +step +proj=utm +zone=32 +ellps=WGS84'
}
