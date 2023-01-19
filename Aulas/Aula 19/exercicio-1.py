# Abrir duas imagens (crop-1-band-5.tif e crop-1-band-7.tif), realizar uma aritmética de bandas (usar NDVI) e aplicar um fatiamento (pixels > 0.5)

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

# todas as imagens possuem uma banda cada
crop_1_band_5 = dataset_crop_1_band_5.GetRasterBand(1)
crop_1_band_7 = dataset_crop_1_band_7.GetRasterBand(1)

# para se realizar cálculos com as bandas, usamos a conversão para matriz numpy
numpy_crop_1_band_5 = crop_1_band_5.ReadAsArray()
numpy_crop_1_band_7 = crop_1_band_7.ReadAsArray()

# criar banda de índice de vegetação e aplicar fatiamento
numpy_crop_1_ndvi = (numpy_crop_1_band_7 - numpy_crop_1_band_5) / (numpy_crop_1_band_7 + numpy_crop_1_band_5)
numpy_output = numpy_crop_1_ndvi > 0.5

print(numpy_crop_1_ndvi)
print(numpy_output)

# fechar dataset
dataset_output = None