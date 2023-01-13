import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
# a =
# array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14]])

# tupla de inteiros indicando o tamanho da array em cada dimensão
print(a.shape)
# (3, 5)

# número de axes da array:
print(a.ndim)
# 2

# descrevendo o tipo dos elementos no array:
print(a.dtype.name)
# 'int32'

# é o tamanho em bytes de cada elemento no array
print(a.itemsize)
# 4

# o total de elementos no array 
print(a.size)
# 15

# uffer contendo os elementos do array, geralmente não é usado dessa forma pois temos facilidades de indexação
print(a.data)
# <memory at 0x0000027ABF3E56C0>

print(type(a))
# <class 'numpy.ndarray'>

b = np.array([6, 7, 8])
print(b)
# array([6, 7, 8])

print(type(b))
# <class 'numpy.ndarray'>
