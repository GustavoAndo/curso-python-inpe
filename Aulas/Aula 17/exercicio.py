from osgeo import gdal
from gdalconst import *

filename = "./raster/crop_rapideye.tif"
dataset = gdal.Open(filename, GA_ReadOnly)
banda_nir = dataset.GetRasterBand(5)
banda_red = dataset.GetRasterBand(3)

gdal.UseExceptions()

# quantidade de bandas
bandas = dataset.RasterCount

for i in range(bandas):
    print ("Mínimos e máximos da banda", i + 1)
    print (dataset.GetRasterBand(i + 1).ComputeRasterMinMax())

# obtencao dos arrays numpy das bandas
array_red = banda_red.ReadAsArray()
array_nir = banda_nir.ReadAsArray()

# geracao de array derivado das bandas
array_ndvi = (array_nir - array_red) / (array_nir + array_red)

# mostrar dimensoes da matriz de saida
print(array_ndvi.shape)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.subplot(131)
plt.title("Banda RED")
plt.imshow(array_red, cmap='gray')

plt.subplot(132)
plt.title("Banda NIR")
plt.imshow(array_nir, cmap='gray')

plt.subplot(133)
plt.title("NDVI")
plt.imshow(array_ndvi, cmap='gray')

plt.show()

dataset = None 