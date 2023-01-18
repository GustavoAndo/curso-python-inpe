import matplotlib.pyplot as plt
import numpy as np

# 80 números será gerados aleatoriamente
N = 80

# vamos sortear N valores no intervalo [0, 1) para cada eixo.
x = np.random.rand(N)
y = np.random.rand(N)

# vamos sortear N valores no intervalo [0, 1) para associar a cores.
colors = np.random.rand(N)

# cada elemento será um círculo de raio entre 0 e 20 pontos.
area = np.pi * (20 * np.random.rand(N))**2

# tamanho da figura
plt.figure( figsize=(10, 8) )

# criando gráfico (eixo x, eixo y, tamanho, cores, alpha)
plt.scatter(x, y, s=area, c=colors, alpha=0.5)

# mostrar grafico
plt.show()