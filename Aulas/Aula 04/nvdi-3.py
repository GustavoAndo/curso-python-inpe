ndvi = float( input("NDVI: ") )
 
if (ndvi < -1.0) or (ndvi > 1.0):
    print("NDVI fora do intervalo!")
elif (ndvi > 0.3) and (ndvi < 0.8):
    print("vegetação densa!")
else:
    print("pouca vegetação!")
 
print("NDVI: ", ndvi)