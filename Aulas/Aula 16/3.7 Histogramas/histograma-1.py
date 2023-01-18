import matplotlib.pyplot as plt
import numpy as np

# criando array com tamanho 100 com valores aleatorios da distribuição normal (200 e 25)
μ = 200
σ = 25
values = np.random.normal(μ, σ, size=100)

# tamanho da figura
plt.figure( figsize=(8, 8) )

# criando histograma
# values -> eixo y
# bins -> quantidade de barras
# density -> densidade
# align -> alinhamento
# facecolor -> cor das barras
# edgecolor -> cor da borda
# linewidth -> espessura da borda
# alpha -> alfa
plt.hist(values, bins=10, density=True, align='left',
         facecolor='green', edgecolor='black', linewidth=1.2, alpha=0.65);

# titulo do grafico
# r -> trata-se de uma forma especial de construir uma string sem que o caracter \ seja tratado como uma sequência de escape. Chamamos este tipo de literal string de raw string, sendo muito útil quando criamos strings contendo sequências de caractere de expressões LaTeX.
# $\mu=200$ -> μ = 200
# $\sigma=25$ -> σ = 25
plt.title(r"Distribuição Normal: $\mu=200$ e $\sigma=25$")

# titulo dos eixos
plt.xlabel("Valor")
plt.ylabel("Frequência")

# mostrar grafico
plt.show()