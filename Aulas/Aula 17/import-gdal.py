# importar biblioteca
from osgeo import gdal

# importar constantes
from gdalconst import *

# informar o uso de exceções
gdal.UseExceptions()

# mostrar versão instalada
print (gdal.__version__)