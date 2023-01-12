xgreen = float(input("Xgreen: "))
xnir = float(input("Xnir: "))
xred = float(input("Xred: "))

NDWI = (xgreen - xnir)/(xgreen + xnir)
NDVI = (xnir - xred)/(xnir + xred)

print(NDWI)
print(NDVI)