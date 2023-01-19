from osgeo import gdal
from gdalconst import *

filename = "./raster/crop_rapideye.tif"
dataset = gdal.Open(filename, GA_ReadOnly)

# quantidade de bandas
bandas = dataset.RasterCount

print ("Número de bandas:", bandas)

# no caso da imagem RapidEye, as bandas 5
# e 3 correspondem às bandas NIR e RED
banda_nir = dataset.GetRasterBand(5)
banda_red = dataset.GetRasterBand(3)

# o tipo do dado armazenado e que acaba de ser lido a partir da banda
print ("Tipos de dados:")
print (" - banda NIR:", gdal.GetDataTypeName(banda_nir.DataType))
print (" - banda RED:", gdal.GetDataTypeName(banda_red.DataType))

#  o valor mínimo e máximo de uma banda 
(menor_valor, maior_valor) = banda_red.ComputeRasterMinMax()
print("Menor valor de RED:", menor_valor)
print("Maior valor de RED:", maior_valor)