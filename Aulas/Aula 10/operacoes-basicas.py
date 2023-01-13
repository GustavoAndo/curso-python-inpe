import numpy as np

# as operações aritméticas se aplicam sobre cada elemento do array, gerando um novo array de resultado
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print(b)
# array([0, 1, 2, 3])
c = a - b
print(c)
# array([20, 29, 38, 47])
print(b**2)
# array([0, 1, 4, 9])
print(10*np.sin(a))
# array([ 9.12945251, ­9.88031624,  7.4511316 , ­2.62374854])
print(a<35)
# array([ True, True, False, False])

# Operações básicas com arrays o operador * calcula o produto por elemento, e não por matriz (para isso usas­se a função dot)
A = np.array([[1,1],
              [0,1]])
B = np.array([[2,0],
              [3,4]])
print(A*B) 
# array([[2, 0],
#        [0, 4]])
print(A.dot(B))
# array([[5, 4],
#        [3, 4]])
 
# operações como += e *= modificam a própria matriz
a = np.ones((2,3))
a *= 3 # é o mesmo que a = a * 3
print(a)
# array([[3, 3, 3],
#        [3, 3, 3]])
b = np.random.random((2,3))
b += a
print(b)
# array([[ 3.417, 3.720, 3.001],
#       [ 3.302, 3.146, 3.092]])

# Operações básicas com arrays as funções sum, min e max funcionam para ndarrays
a = np.random.random((2,3))
print(a)
# array([[ 0.186, 0.345, 0.396],
#       [ 0.538, 0.419, 0.685]])
print(a.sum())
# 2.571
print(a.min())
# 0.186
print(a.max())
# 0.685

# a função reshape altera a estrutura do ndarray
b = np.arange(12).reshape(3,4)
print(b)
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
print(b.sum(axis=0))
# array([12, 15, 18, 21])
print(b.sum(axis=1))
# array([ 6, 22, 38])
print(b.min(axis=1))
# array([0, 4, 8])
# soma cumulativa
print(b.cumsum(axis=1))
# array([[ 0,  1,  3,  6],
#        [ 4,  9, 15, 22],
#        [ 8, 17, 27, 38]]