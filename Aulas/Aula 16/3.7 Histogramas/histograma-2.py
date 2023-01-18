import matplotlib.pyplot as plt
import numpy as np

# criando array com tamanho 100 com valores aleatorios da distribuição normal (200 e 25)
μ = 200
σ = 25
values = np.random.normal(μ, σ, size = 100)

# tamaho da figura
plt.figure( figsize=(8, 8) )

# criando gráfico histograma
count, bins, ignored = plt.hist(values, bins=30, density=True,
                                align='left', facecolor='lightblue',
                                edgecolor='black', linewidth=1.2,
                                alpha=0.65);

# titulo do grafico
plt.title(r"Distribuição Normal: $\mu=200$ e $\sigma=25$")

# titulos dos eixo
plt.xlabel("Valor")
plt.ylabel("Frequência")

# adicionando linha no gráfico
plt.plot( bins, 1 / ( σ * np.sqrt(2 * np.pi) ) *
                np.exp( - (bins - μ)**2 / (2 * σ**2) ),
          linewidth=1.5, color='r' )

plt.show()