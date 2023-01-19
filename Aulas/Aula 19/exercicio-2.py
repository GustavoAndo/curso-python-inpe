# dados dois rasters de 1 banda cada (1 mapa temático, 1 mapa de referência), calcule a taxa de acerto da classificação do mapa temático e salve um arquivo GeoTIFF contendo um mapa de concordância entre as imagens

from osgeo import gdal
import numpy as np
from matplotlib import pyplot as plt
from gdalconst import *
import salvar_banda as s

# abrir as imagens
filename_reference = "./raster/area_urbana_referencia.tif"
filename_classification = "./raster/area_urbana_classificacao.tif"

try:
    dataset_reference = gdal.Open(filename_reference, GA_ReadOnly) 
    dataset_classification = gdal.Open(filename_classification, GA_ReadOnly) 
except:
    print ("Erro na abertura de algum arquivo!")

# verificar compatibilidade de metadados
if (dataset_reference.GetProjectionRef() != dataset_classification.GetProjectionRef()):
    print("Sistemas de referência diferentes")
elif (dataset_reference.GetGeoTransform() != dataset_classification.GetGeoTransform()):
    print("Metadados espaciais diferentes")
else:
    # obter metadados
    linhas = dataset_reference.RasterYSize
    colunas = dataset_reference.RasterXSize

    # obter as bandas
    band_reference = dataset_reference.GetRasterBand(1)
    band_classification = dataset_classification.GetRasterBand(1)

    # gerar matrizes de pixels
    numpy_reference = band_reference.ReadAsArray()
    numpy_classification = band_classification.ReadAsArray()

    # gerar matriz de comparação
    numpy_comparison = (numpy_reference == numpy_classification)
    accuracy = 100 * numpy_comparison.sum() / (linhas * colunas)

    # plotar resultados
    plt.figure(figsize=(15, 4))

    plt.subplot(131)
    plt.imshow(numpy_reference)
    plt.title('Imagem de referência')

    plt.subplot(132)
    plt.imshow(numpy_classification)
    plt.title('Imagem classificada')

    plt.subplot(133)
    plt.imshow(numpy_comparison)
    plt.title('Imagem de comparação, ' + str(accuracy) + '% de acurácia')

# salvar imagem de concordância
nome_do_arquivo = "./raster/comparacao.tif"
s.salvar_banda(numpy_comparison, nome_do_arquivo, dataset_reference)

# fechar imagens
dataset_reference = None
dataset_classification = None