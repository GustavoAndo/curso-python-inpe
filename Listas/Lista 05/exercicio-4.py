import math

def interceptam(r, s):
    x1 = r[0][0]
    y1 = r[0][1]
    x2 = r[1][0]
    y2 = r[1][1]

    x3 = s[0][0]
    y3 = s[0][1]
    x4 = s[1][0]
    y4 = s[1][1]

    num1 = (y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)
    num2 = (y2 - y1) * (x4 - x1) - (x2 - x1) * (y4 - y1)

    if num1 == 0 and num2 == 0:
        if x1 == x2:
            r = (min(y1, y2) <= max(y3, y4)) and (min(y3, y4) <= max(y1, y2))
        else:
            r= (min(x1, x2) <= max(x3, x4)) and (min(x3, x4) <= max(x1, x2))
    else: 
        num3 = (y4 - y3) * (x1 - x3) - (x4 - x3) * (y1 - y3)

        num4 = (y4 - y3) * (x2 - x3) - (x4 - x3) * (y2 - y3)

        r = ((num3 * num4) <= 0.0) and ((num3 * num4) <= 0.0)
    
    return r

 
print("Digite as coordenadas do primeiro ponto da primeira reta (P1):")
x1 = float( input("x: ") )
y1 = float( input("y: ") )
 
print("Digite as coordenadas do segundo ponto da primeira reta (P2):")
x2 = float( input("x: ") )
y2 = float( input("y: ") )

r = ((x1, y1), (x2, y2))
 
print("Digite as coordenadas do primeiro ponto da segunda reta (P3):")
x3 = float( input("x: ") )
y3 = float( input("y: ") )
 
print("Digite as coordenadas do segundo ponto da segunda reta (P4):")
x4 = float( input("x: ") )
y4 = float( input("y: ") )

s = ((x3, y3), (x4, y4))

print(interceptam(r, s))