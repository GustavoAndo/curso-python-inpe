# Dadas 2 imagens (raster_alvo e raster_entrada), encontrar a localização da imagem raster_alvo dentro da imagem raster_entrada e plotar o resultado (raster_entrada com um x sobreposto na localização)

from osgeo import gdal
import numpy as np
from matplotlib import pyplot as plt
from gdalconst import *
import salvar_banda as s

# definir onde estao as imagens
raster_entrada = './raster/american-anticipation-audience-163368.jpg'
raster_alvo = './raster/target_2.jpg'

# gerar datasets gdal
dataset_entrada = gdal.Open(raster_entrada, GA_ReadOnly)
dataset_alvo = gdal.Open(raster_alvo, GA_ReadOnly)

# obter as bandas
banda_entrada = dataset_entrada.GetRasterBand(1).ReadAsArray()
banda_alvo = dataset_alvo.GetRasterBand(1).ReadAsArray()

# obter metadados da imagem de entrada
Linhas_entrada = dataset_entrada.RasterYSize
Colunas_entrada = dataset_entrada.RasterXSize

# obter metadados da imagem de alvo
Linhas_alvo = dataset_alvo.RasterYSize
Colunas_alvo = dataset_alvo.RasterXSize

# encontrar linha/coluna do alvo na imagem de entrada
linha = 0
coluna = 0
# criar variável para armazenar a região de maior semelhança
maior_semelhanca = 0
for r in range(Linhas_entrada - Linhas_alvo):
    for c in range(Colunas_entrada - Colunas_alvo):
        # criar janela com recorte do mesmo tamanho da banda_alvo
        janela = banda_entrada[r:r+Linhas_alvo, c:c+Colunas_alvo]
        # comparar quantos pixels são iguais entre as duas janelas
        pixels_iguais = (banda_alvo == janela)
        somatorio = pixels_iguais.sum()
        if (somatorio > maior_semelhanca):
            linha = r
            coluna = c
            maior_semelhanca = somatorio

# apresentar resultado
plt.imshow(banda_alvo, cmap = 'gray')
plt.title('Imagem de alvo')

# obter as bandas em forma de array para visualização em cores
array_rgb = np.zeros((Linhas_entrada, Colunas_entrada, 3), dtype=np.uint8)
array_rgb[:,:,0] = dataset_entrada.GetRasterBand(1).ReadAsArray()
array_rgb[:,:,1] = dataset_entrada.GetRasterBand(2).ReadAsArray()
array_rgb[:,:,2] = dataset_entrada.GetRasterBand(3).ReadAsArray()

plt.figure(figsize=(16,9))
# plt.imshow(banda_entrada, cmap = 'gray', aspect='auto')
plt.imshow(array_rgb, aspect='auto')
plt.title('Imagem de entrada')
plt.plot(coluna+Colunas_alvo/2, linha+Linhas_alvo/2,
         marker='o', markersize=30, markeredgewidth=3, 
         markeredgecolor='yellow', markerfacecolor='none')
         
plt.show()

# fechar os arquivos
dataset_entrada = None
dataset_alvo = None