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
GEOSTATISTIC_TRIAL = ['Id', "Field name", "Area", "Irrigated", "Soil type", "LPC Team", "Farmer", "Crop field", "Contour",
                      "Create date", "Update date"]

FETCH_ALL_DOMAIN = "SELECT * FROM domains.yes_or_not;"

FETCH_ALL_TEAM = "SELECT * FROM geostatistics.lpc_team;"
FETCH_ONE_TEAM = "SELECT * FROM geostatistics.lpc_team WHERE id = '{}';"

FETCH_ALL_CROP = "SELECT * FROM geostatistics.crop_trial;"
FETCH_ONE_CROP = "SELECT * FROM geostatistics.crop_trial WHERE id = '{}';"

FETCH_ALL_FARMER = "SELECT * FROM geostatistics.farmer;"
FETCH_ONE_FARMER = "SELECT * FROM geostatistics.farmer WHERE id = '{}';"

FETCH_ALL_TRIAL = """
SELECT
    gt.id, gt.field_name, gt.field_area, yn.description, gt.field_soil, gt.lpc_team, gt.farmer, gt.crop_trial, gt.id_contour, gt.create_date, gt.update_date
FROM
    geostatistics.geostatistic_trial gt
JOIN
    domains.yes_or_not yn ON gt.field_irrigation = yn.code
"""

INSERT_CROP_SQL = "INSERT INTO geostatistics.crop_trial (crop_name, sowing_date, harvest_date, variety, inter_ro_cm, " \
                  "create_date) VALUES (%s, %s, %s, %s, %s, %s);"
UPDATE_CROP_SQL = "UPDATE geostatistics.crop_trial SET crop_name = %s, " \
                  "sowing_date = %s, harvest_date = %s, variety = %s, inter_ro_cm = %s, update_date = %s WHERE id = %s;"
DELETE_CROP_SQL = "DELETE FROM geostatistics.crop_trial WHERE id = '{}';"

INSERT_FARMER_SQL = "INSERT INTO geostatistics.farmer (first_name, last_name, address, zipcode, town, country," \
                  "create_date) VALUES (%s, %s, %s, %s, %s, %s, %s);"
UPDATE_FARMER_SQL = "UPDATE geostatistics.farmer SET first_name = %s, " \
                  "last_name = %s, address = %s, zipcode = %s, town = %s, country = %s, update_date = %s WHERE id = %s;"
DELETE_FARMER_SQL = "DELETE FROM geostatistics.farmer WHERE id = '{}';"


INSERT_TRIAL_SQL = "INSERT INTO geostatistics.geostatistic_trial (field_name, field_area, field_irrigation, " \
                   "field_soil, lpc_team, farmer, crop_trial, id_contour, create_date) VALUES (%s, %s, %s, %s, %s, " \
                   "%s, %s, %s, %s);"
UPDATE_TRIAL_SQL = "UPDATE geostatistics.geostatistic_trial SET field_name = %s, field_area = %s, field_irrigation = " \
                   "%s, field_soil = %s, lpc_team = %s, farmer = %s, crop_trial = %s, id_contour = %s, update_date = " \
                   "%s WHERE id = %s;"
DELETE_TRIAL_SQL = "DELETE FROM geostatistics.geostatistic_trial WHERE id = '{}';"

INSERT_TEAM_SQL = "INSERT INTO geostatistics.lpc_team (first_name, last_name, create_date) VALUES (%s, %s, %s);"
UPDATE_TEAM_SQL = "UPDATE geostatistics.lpc_team SET first_name = %s, last_name = %s,  update_date = %s WHERE id = %s;"
DELETE_TEAM_SQL = "DELETE FROM geostatistics.lpc_team WHERE id = '{}';"
