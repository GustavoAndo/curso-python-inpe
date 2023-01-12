print("Gilberto" + "Ribeiro") 
# GilbertoRibeiro

print("Gilberto" * 3)
# GilbertoGilbertoGilberto

print("Ri" in "Gilberto Ribeiro de Queiroz")
# True
print("Rie" in "Gilberto Ribeiro de Queiroz")
# False

print("Ri" not in "Gilberto Ribeiro de Queiroz")
# False
print("Rie" not in "Gilberto Ribeiro de Queiroz")
# True

print(len("Gilberto Ribeiro de Queiroz"))
# 27

print("Gilberto Ribeiro de Queiroz"[0])
# G

print("Gilberto Ribeiro de Queiroz"[0:3])
# Gil
print("Gilberto Ribeiro de Queiroz"[:-24])
# Gil
print("Gilberto Ribeiro de Queiroz"[9:])
# Ribeiro de Queiroz

print("Alberto Queiroz".find("rto"))
# 4
print("Cassia Diniz".find("rto"))
# -1

print("-".join( ("Gilberto", "Ribeiro", "de", "Queiroz") ))
# Gilberto-Ribeiro-de-Queiroz
print(" ".join( ("Gilberto", "Ribeiro", "de", "Queiroz") ))
# Gilberto Ribeiro de Queiroz

print("Gilberto Ribeiro de Queiroz".split())
# ['Gilberto', 'Ribeiro', 'de', 'Queiroz']
print("Gilberto-Ribeiro-de-Queiroz".split("-"))
# ['Gilberto', 'Ribeiro', 'de', 'Queiroz']

print("Gilberto Ribeiro de Queiroz".replace("i", "@"))
# G@lberto R@be@ro de Que@roz
print("Gilberto Ribeiro de Queiroz".replace("i", "@", 2))
# G@lberto R@beiro de Queiroz

print('Gilberto'.isdigit())
# False
print('123'.isdigit())
# True

print("GilBerto".islower())
# False
print("gilberto".islower())
# True

print("GilBerto".isupper())
# False
print("GILBERTO".isupper())
# True

print("GilBerto".lower())
# gilberto

print("GilBerto".upper())
# GILBERTO