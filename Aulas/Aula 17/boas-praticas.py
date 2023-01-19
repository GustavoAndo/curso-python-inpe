from osgeo import gdal
from gdalconst import *

gdal.UseExceptions()

# criar o dataset abrindo o arquivo para leitura
filename = "./raster/crop_rapideye.tif"
dataset = gdal.Open(filename, GA_ReadOnly)

# fechar o dataset e liberar memória
dataset = None 

# biblioteca de funções relacionadas ao sistema
# sys: System-specific parameters and functions
import sys

filename_erro = "teste/" + filename
print ("Tentar abrir", filename_erro)

try:
    dataset = gdal.Open(filename_erro, GA_ReadOnly)
    print ("Arquivo aberto com sucesso!")
except:
    print("Erro na abertura do arquivo!")
    
print ("Tentar abrir" + filename)
try:
    dataset = gdal.Open(filename, GA_ReadOnly)
    print ("Arquivo aberto com sucesso!")
except:
    print("Erro na abertura do arquivo!")