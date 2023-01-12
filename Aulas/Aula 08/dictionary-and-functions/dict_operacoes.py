# Localização de "São José dos Campos"
sjc = {
    "longitude": -45.88, 
    "latitude": -23.17
}
 
# Localização de "Ouro Preto"
ouro_preto = {
    "longitude": -43.50, 
    "latitude": -20.38
}
 
print(sjc)
 
print(sjc["longitude"])
 
sjc["latitude"] = -20.379
 
for key, value in sjc.items():
    print( "key: {}; value: {}".format(key, value) )