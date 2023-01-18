import matplotlib.pyplot as plt
import numpy as np

# criando arrays de númeors aleatórios (100 numeros de 0 a 2)
t = np.linspace(0.0, 2.0, 100)

# criando dois novos arrays multiplicando os valores aleatórios por pi e por pi * 2 e conseguindo o valor de seno
f1 = np.sin(np.pi*t)
f2 = np.sin(2*np.pi*t)

# tamanho da figura
plt.figure( figsize=(10, 8) )

# forma alternativa de adicionar duas linhas no gráfico:
plt.plot(t, f1, "orange",
         t, f2, "purple",
         linewidth=2.0)

# adicionando limites no eixo
plt.xlim([0.0, 2.0])
plt.ylim([-1.0, 1.0])

# adicionando titulo nos eixos
plt.xlabel(r"$t$", fontsize=16)
plt.ylabel(r"$f(t)$", fontsize=16)

# titulo do grafico
plt.title("Senoides", fontsize=24)

# colocando legenda (nesse caso, como o parametro label não foi adicionado em plot, o texto da legenda de cada linha deverá ser implementada)
plt.legend([r"$f_1(t)=sin(\pi \times t)$", 
            r"$f_2(t)=sin(2 \times \pi \times t)$"])

# detalhes do fundo
plt.grid( color='gray', linestyle='--', linewidth=0.5)

# mostrar grafico
plt.show()