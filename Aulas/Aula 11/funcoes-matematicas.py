import numpy as np

# exemplos de funções que se aplicam a cada elemento de um ndarray
B = np.arange(3)
print(B)
# array([0, 1, 2])

print(np.exp(B))
# array([ 1. , 2.71828183, 7.3890561])

# raiz quadrada
print(np.sqrt(B))
# array([ 0. , 1. , 1.41421356])

# para acessar os elementos do array, podemos usar um índice por eixo
b = np.arange(12).reshape(3,4)
print(b)
# array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])
print(b[1,2])
# 6
print(b[3,4])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: index 3 is out of bounds 
# for axis 0 with size 3
print(b[-1])
# array([ 8,  9, 10, 11]