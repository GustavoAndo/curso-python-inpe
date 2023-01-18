import matplotlib.pyplot as plt
import numpy as np

# criando arrays de númeors aleatórios (100 numeros de 0 a 2)
t = np.linspace(0.0, 2.0, 100)

# criando novo array multiplicando os valores aleatórios por pi
f = np.sin(np.pi*t)

# tamanho da figura
plt.figure( figsize=(10, 8) )

# criando grafico (eixo x, eixo y, cor, tamanho da linha)
plt.plot(t, f, "orange", linewidth=2.0)

# limites de valores que apareceram na figura (primeiro do eixo x (xlim) e depois do eixo y (ylim))
plt.xlim([0.0, 2.0])
plt.ylim([-1.0, 1.0])

# titulo dos eixos
plt.xlabel(r"$t$", fontsize=16)
plt.ylabel(r"$f(t)$", fontsize=16)

# titulo
plt.title(r"$f(t)=\sin(\pi \times t)$", fontsize=24)

# detalhes do fundo
# color -> cor
# linestyle -> estilo da linha
# linewidth -> espessura da linha
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()