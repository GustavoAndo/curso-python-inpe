def calcular_area(p):
    s = 0
    for c in range(len(p)):
        if c+1 == len(p): s += p[c][0] * p[0][1] + p[c][1] * p[0][0]
        else: s += p[c][0] * p[c+1][1] + p[c][1] * p[c+1][0]
    return s/2

quadrado = ( (0, 0), (10, 0), (10, 10), (0, 10) )
print(calcular_area(quadrado))