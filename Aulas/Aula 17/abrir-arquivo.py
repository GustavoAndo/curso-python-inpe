# importar biblioteca
from osgeo import gdal

# importar constantes
from gdalconst import *

gdal.UseExceptions()

# criar o dataset abrindo o arquivo para leitura
filename = "./raster/crop_rapideye.tif"
dataset = gdal.Open(filename, GA_ReadOnly)

# fechar o dataset e liberar memória
dataset = None 