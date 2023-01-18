import matplotlib.pyplot as plt
import numpy as np

# criando arrays de númeors aleatórios (100 numeros de 0 a 2)
t = np.linspace(0.0, 2.0, 100)

# criando dois novos arrays multiplicando os valores aleatórios por pi e por pi * 2 e conseguindo o valor de seno
f1 = np.sin(np.pi*t)
f2 = np.sin(2*np.pi*t)

# tamanho da figura
plt.figure( figsize=(10, 8) )

# adicionando primeira e segunda linha no gráfico
# t -> eixo x
# f1 e f2 -> eixo y
# orange, purple -> cor
# linewidth -> espessura da linha
# label -> legenda
plt.plot(t, f1, "orange", linewidth=2.0,
         label=r"$f_1(t)=sin(\pi \times t)$")
plt.plot(t, f2, "purple", linewidth=2.0,
         label=r"$f_2(t)=sin(2 \times \pi \times t)$")

# adicionando limites no eixo
plt.xlim([0.0, 2.0])
plt.ylim([-1.0, 1.0])

# adicionando titulo nos eixos
plt.xlabel(r"$t$", fontsize=16)
plt.ylabel(r"$f(t)$", fontsize=16)

# titulo do grafico
plt.title("Senoides", fontsize=24)

# colocando legenda (nesse caso, como o parametro label foi adicionado em plot, será utilizado automaticamente o que está na label como o texto da legenda)
plt.legend()

# detalhes do fundo
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# mostrar gráfico
plt.show()