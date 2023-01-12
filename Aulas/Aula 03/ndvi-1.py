# definir valores de NIR e Red
NIR = 0.5
Red = 0.3

# mostrar dados de entrada na tela
print("NIR: ", NIR)
print("Red: ", Red)

# calcular NDVI
NDVI = (NIR - Red) / (NIR + Red)

# mostrar resultado na tela
print("NDVI: ", NDVI)
