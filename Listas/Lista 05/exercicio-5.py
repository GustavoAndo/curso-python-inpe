def ndwi(xgreen, xnir):
    return (xgreen - xnir)/(xgreen + xnir)

def ndvi(xred, xnir):
    return (xnir - xred)/(xnir + xred)

xgreen = float(input("Xgreen: "))
xnir = float(input("Xnir: "))
xred = float(input("Xred: "))

print(ndwi(xgreen, xnir))
print(ndvi(xred, xnir))