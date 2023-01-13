import numpy as np

# NumPy oferece uma série de funções para geração de números aleatórios

# np.random.rand(d0, d1, ..., dn)
# numeros aleatorios no intervalo de 0 a 1 de acordo com o shape informado
print(np.random.rand(3,2))
# array([[ 0.14022471,  0.96360618], 
#       [ 0.37601032,  0.25528411],
#       [ 0.49313049,  0.94909878]])

# np.random.randn(d0, d1, ..., dn)
# números aleatórios que faz parte da tablea de distribuicão normal
print(np.random.randn(3,2))
# array([[ 1.79741389,  0.06386413],
#        [-1.16275488,  1.0615288 ],
#        [-0.02802567, -0.02323773]])

# np.random.randint(low, high=None, size=None, dtype=int)
# numeros aleatorios inteiros, de um numero menor (inclusive) até um maior (exclusive)
print(np.random.randint(2, 10, size=10))
# array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])

# random.random(size=None)
# numeros aleatorios no intervalo de 0 a 1 para apenas um array simples
print(np.random.random(size=4))
# array([0.76193465, 0.67579061, 0.41575374, 0.47477983])