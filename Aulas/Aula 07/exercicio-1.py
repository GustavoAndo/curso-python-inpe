serie_ndvi = [0.3, -0.3, 0.2, None, 0.9, 0.8, 0.8, None, 0.2, 0.2]

print("Lista: ", serie_ndvi)
invalidos = serie_ndvi.count(None)
print("Quantidade de valores inválidos:", invalidos)
print("Quantidade de valores válidos:", len(serie_ndvi) - invalidos)