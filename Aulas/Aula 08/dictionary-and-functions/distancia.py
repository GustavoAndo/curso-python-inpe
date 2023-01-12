import math
 
def Distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
 
    d2 = dx**2 + dy**2
 
    d = math.sqrt(d2)
 
    return d