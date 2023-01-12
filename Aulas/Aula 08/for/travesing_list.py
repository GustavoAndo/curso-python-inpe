print("Conversão de F -> C")
 
fahr = [ 0, 20, 40, 60, 80, 100 ]
 
celsius = [ 5*(x-32)/9 for x in fahr ]
 
for f, c in zip(fahr, celsius):
    print(f, c)
 
print("Fim!")