import math

lat1 = float(input("Digite a latitude da primeira coordenada: "))
long1 = float(input("Digite a longitude da primeira coordenada: "))

lat2 = float(input("Digite a latitude da segunda coordenada: "))
long2 = float(input("Digite a longitude da segunda coordenada: "))

lat1 = math.radians(lat1)
lat2 = math.radians(lat2)

long1 = math.radians(long1)
long2 = math.radians(long2)

r = 6371

d = 2 * r * math.asin(math.sqrt(math.sin((lat2 - lat1)/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((long2 - long1)/2)**2))

print(d)
