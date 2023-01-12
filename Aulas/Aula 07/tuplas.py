# As tuplas são expressas através de uma sequência cujos itens são separados por vírgula e, delimitados ou não por parênteses.

# Coordenadas do centróide da Cidade de São Paulo/Brasil
centroide_sp = (-46.7165, -23.6830)

print(centroide_sp)
print("longitude: {} latitude: {}".format(*centroide_sp))
print( len(centroide_sp) )

longitude = centroide_sp[0]
latitude = centroide_sp[1]