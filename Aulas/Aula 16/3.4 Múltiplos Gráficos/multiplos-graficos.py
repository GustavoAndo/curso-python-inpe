import matplotlib.pyplot as plt
import numpy as np

# criando arrays de númeors aleatórios (100 numeros de 0 a 2)
t = np.linspace(0.0, 2.0, 100)

# criando quatro novos arrays multiplicando os valores aleatórios por pi, pi * 2, pi * 4 e pi * 8 e conseguindo o valor de seno
f1 = np.sin(np.pi*t)
f2 = np.sin(2*np.pi*t)
f3 = np.sin(4*np.pi*t)
f4 = np.sin(8*np.pi*t)

# tamanho da figura
plt.figure( figsize=(10, 8) )

# criando primeiro gráfico
plt.subplot(221, facecolor="#FFFFEA")
plt.plot(t, f1, "orange")
plt.title(r"$f(t)=sin(\pi \times t)$")

# criando segundo gráfico
plt.subplot(222)
plt.plot(t, f2, "purple")
plt.title(r"$f(t)=sin(2 \times \pi \times t)$")

# criando terceiro gráfico
plt.subplot(223)
plt.plot(t, f3, "salmon")
plt.title(r"$f(t)=sin(4 \times \pi \times t)$")

# criando quarto gráfico
plt.subplot(224, facecolor="#FEEEEE")
plt.plot(t, f4, "Crimson")
plt.title(r"$f(t)=sin(8 \times \pi \times t)$")

# título superior de todos os gráficos
plt.suptitle("Senoides", fontsize=24)

# mostrar grafico
plt.show()