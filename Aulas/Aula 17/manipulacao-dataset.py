from osgeo import gdal
from gdalconst import *

filename = "./raster/crop_rapideye.tif"
dataset = gdal.Open(filename, GA_ReadOnly)

gdal.UseExceptions()

# retorna uma tupla referentes à transformação de georreferenciamento do dataset 
geotransform = dataset.GetGeoTransform()
print (geotransform)

# [0] is the x coordinate of the upper left cell in raster
# [1] is the width of the elements in the raster
# [2] is the element rotation in x, is set to 0 if a north up raster
# [3] is the y coordinate of the upper left cell in raster
# [4] is the element rotation in y, is set to 0 if a north up raster
# [5] is the height of the elements in the raster (negative)

latitude = geotransform[3]
longitude = geotransform[0]
resolucao_x = geotransform[1]
resolucao_y = -geotransform[5]

print ("Latitude inicial do dataset:", latitude)
print ("Longitude inicial do dataset:", longitude)
print ("Resolução (x) do dataset:", resolucao_x)
print ("Resolução (y) do dataset:", resolucao_y)

# retorna uma descrição em formato WKT (Well-Known Text), que é uma linguagem de marcação de texto utilizada para representar um sistema de referência espacial dos objetos geográficos e a transformação entre sistemas de coordenadas
print (dataset.GetProjectionRef())

dataset = None 