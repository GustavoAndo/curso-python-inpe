# importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
# criando conjuntos de pontos aleatórios (500 pontos 2D)
azuis = np.random.random(size=(2,500))
verdes = np.random.random(size=(2,300)) + 0.5
# criando gráfico 2D
plt.figure()
plt.scatter(azuis[0], azuis[1], c = 'blue')
plt.scatter(verdes[0], verdes[1], c = 'green')
plt.show()