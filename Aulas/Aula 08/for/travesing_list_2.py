print("Conversão de F -> C -> K")
 
fahr = [ 0, 20, 40, 60, 80, 100 ]
 
celsius = [ 5*(x-32)/9 for x in fahr ]
 
kelvin = [ x+273 for x in celsius ]
 
for f, c, k in zip(fahr, celsius, kelvin):
    print(f, c, k)
 
print("Fim!")