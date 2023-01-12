A = 3
B = -2
C = -6
 
print("Digite as coordenadas: ")
x = float(input('x: '))
y = float(input('y: '))

y0 = (-A*x - C) / B
 
if y > y0:
    print("Acima!")
elif y < y0:
    print("Abaixo!")
else:
    print("Sobre a reta!")