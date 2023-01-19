from osgeo import gdal
from gdalconst import *

filename = "./raster/crop_rapideye.tif"
dataset = gdal.Open(filename, GA_ReadOnly)

# número de linhas e colunas
linhas = dataset.RasterYSize
colunas = dataset.RasterXSize

print ("Número de linhas:", linhas)
print ("Número de colunas:", colunas)