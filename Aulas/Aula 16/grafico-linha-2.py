# import
import matplotlib.pyplot as plt

# valores do eixo-x
ano = [ 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 ]

# valores do eixo-y
num_focos = [ 123, 123, 249, 133, 194, 115, 183, 236, 188, 260 ]

# criar grafico de linha
# r -> red (vermelho)
# o -> marcação em círculo
# - -> estilo da linha sólida
# linewidth -> espessura da linha
plt.plot(ano, num_focos, "ro-", linewidth=2.0)

# titulos dos eixos x e y (fontsize -> tamanho da fonte)
plt.xlabel("Ano", fontsize=16)
plt.ylabel("Número de Focos", fontsize=16)

# titulo do grafico
plt.title("Focos de Queimadas - Brasil", fontsize=24)

# rotulos do eixo y (valores que aparecerão no eixo y)
# plt.yticks([ 100, 140, 180, 220, 260 ])
plt.yticks([ 100, 140, 180, 220, 260 ],
           [ '100 mil', '140 mil', '180 mil', '220 mil', '260 mil' ] )

# mostrar grafico
plt.show()