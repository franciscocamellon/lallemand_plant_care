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

CROP_COLUMN_NAMES = ['Id', "Crop name", "Sowing date", "Harvesting date", "Variety", "InterRoCM", "Create date",
                     "Update date"]
FARMER_COLUMN_NAMES = ['Id', "First name", "Last name", "Address", "Zipcode", "Town", "Country", "Create date",
                       "Update date"]

INSERT_CROP_SQL = "INSERT INTO geostatistics.crop_trial (crop_name, sowing_date, harvest_date, variety, inter_ro_cm, " \
                  "create_date) VALUES (%s, %s, %s, %s, %s, %s);"
UPDATE_CROP_SQL = "UPDATE geostatistics.crop_trial SET crop_name = %s, " \
                  "sowing_date = %s, harvest_date = %s, variety = %s, inter_ro_cm = %s, update_date = %s WHERE id = %s;"

INSERT_FARMER_SQL = "INSERT INTO geostatistics.farmer (first_name, last_name, address, zipcode, town, country," \
                  "create_date) VALUES (%s, %s, %s, %s, %s, %s, %s);"
UPDATE_FARMER_SQL = "UPDATE geostatistics.farmer SET first_name = %s, " \
                  "last_name = %s, address = %s, zipcode = %s, town = %s, country = %s, update_date = %s WHERE id = %s;"
