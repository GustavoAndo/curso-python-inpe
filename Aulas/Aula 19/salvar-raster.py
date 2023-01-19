# Neste exemplo, vamos abrir duas bandas, realizar uma aritmética (NDVI) seguida de um fatiamento, e salvar o resultado num arquivo GeoTIFF. Para salvar um arquivo com imagens, é preciso criar um novo dataset, informar todos os metadados relacionados ao contexto geográfico (sistema de projeção, limite geográfico, etc.) além do número de bandas, número de linhas e colunas.

# importar bibliotecas
from osgeo import gdal
import numpy as np
from matplotlib import pyplot as plt

# importar constantes
from gdalconst import *

# informar o uso de exceções
gdal.UseExceptions()

# biblioteca de funções relacionadas ao sistema
# sys: System-specific parameters and functions
import sys

# abrir 2 imagens com 1 banda cada
filename_crop_1_band_5 = "./raster/crop-1-band-5.tif" # red
filename_crop_1_band_7 = "./raster/crop-1-band-7.tif" # nir

try:
    dataset_crop_1_band_5 = gdal.Open(filename_crop_1_band_5, GA_ReadOnly) 
    dataset_crop_1_band_7 = gdal.Open(filename_crop_1_band_7, GA_ReadOnly) 
except:
    print ("Erro na abertura de algum arquivo!")

crop_1_band_5 = dataset_crop_1_band_5.GetRasterBand(1)
crop_1_band_7 = dataset_crop_1_band_7.GetRasterBand(1)

numpy_crop_1_band_5 = crop_1_band_5.ReadAsArray()
numpy_crop_1_band_7 = crop_1_band_7.ReadAsArray()

numpy_crop_1_ndvi = (numpy_crop_1_band_7 - numpy_crop_1_band_5) / (numpy_crop_1_band_7 + numpy_crop_1_band_5)
numpy_output = numpy_crop_1_ndvi > 0.5

# obter metadados
linhas = dataset_crop_1_band_5.RasterYSize
colunas = dataset_crop_1_band_5.RasterXSize
bandas = 1

# salvar banda em arquivo GeoTIFF
# definir nome do arquivo
filename_output = "./raster/crop-1-ndvi-threshold.tif"
# definir driver
driver = gdal.GetDriverByName('GTiff')
# copiar tipo de dados da banda já existente
data_type = crop_1_band_5.DataType
# criar novo dataset
dataset_output = driver.Create(filename_output, colunas, linhas, bandas, data_type)
# copiar informações espaciais da banda já existente
dataset_output.SetGeoTransform(dataset_crop_1_band_5.GetGeoTransform())
# copiar informações de projeção
dataset_output.SetProjection(dataset_crop_1_band_5.GetProjectionRef())
# escrever dados da matriz NumPy na banda
dataset_output.GetRasterBand(1).WriteArray(numpy_output)
# salvar valores
dataset_output.FlushCache()
# fechar dataset
dataset_output = None