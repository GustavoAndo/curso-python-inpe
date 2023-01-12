import math
 
print("Digite as coordenadas do primeiro ponto da reta:")
x1 = float( input("x1: ") )
y1 = float( input("y1: ") )
 
print("Digite as coordenadas do segundo ponto da reta:")
x2 = float( input("x2: ") )
y2 = float( input("y2: ") )
 
print("Digite a coordenada do ponto que deseja calcular a distância:")
x = float( input("x: ") )
y = float( input("y: ") )

d = math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )
 
if d > 0: 
    num = abs( (y2 - y1) * (x - x1) - (x2 - x1) * (y - y1) )

    h = num / d
 
    print(h)
else:
    print('Coordenadas inválidas!') 