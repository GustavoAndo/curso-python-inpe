import numpy as np

a = np.array([2,3,4])
print(a)
# array([2, 3, 4])

print(a.dtype)
# dtype('int32')

b = np.array([1.2, 3.5, 5.1])
print(b.dtype)
# dtype('float64')

# transformação automática de sequências de sequências em 2D - array
b = np.array([(1.5,2,3), (4,5,6)])
print(b)
# array([[ 1.5, 2. , 3. ],
#       [ 4. , 5. , 6. ]])

# as funções zeros/ones criam arrays contendo zeros/uns

print(np.zeros( (3,4) ))
#array([[ 0.,  0.,  0.,  0.],
#       [ 0.,  0.,  0.,  0.],
#       [ 0.,  0.,  0.,  0.]])

print(np.ones( (2,3) ))
#array([[ 1.,  1.,  1.],
#      [ 1.,  1.,  1.]])

# a função arange cria números em sequência
# iniciando em 10
# finalizando em 30
# pulando de 5 em 5
print(np.arange( 10, 30, 5 ))
# array([10, 15, 20, 25])

# de 0 a 2, pulando de 0.3 em 0.3
print(np.arange( 0, 2, 0.3 ))         
# array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8]

# a função linspace gera um intervalo de números com um tamanho específico
from numpy import pi

# iniciando em 0
# finalizando em 2
# tamanho 9
print(np.linspace( 0, 2, 9 )) 
# array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])

# 100 números entre 0 e 2pi
x = np.linspace( 0, 2*pi, 100 )

# seno de todos os números, calculados de uma só vez
f = np.sin(x)