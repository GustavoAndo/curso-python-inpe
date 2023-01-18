# import
import matplotlib.pyplot as plt

# valores do eixo-x
ano = [ 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 ]

# valores do eixo-y
num_focos = [ 123, 123, 249, 133, 194, 115, 183, 236, 188, 260 ]

# tamanho da figura
plt.figure( figsize=( 10, 8 ) )

# ano -> valores do eixo x
# num_focos -> valores do eixo y
# color -> cor
# linestyle -> estilo da linha (dashed, solid, dotted)
# linewidth -> espessura da linha
# marker -> estilo da marcação (o -> circular, s -> quadrado (square), etc.)
# markersize -> tamanho da marcação
# mew -> tamanho da borda da marcação
# mec ->  cor da borda da marcação
# mfc -> cor da marcação
plt.plot(ano, num_focos,
         color="red", linestyle="dashed", linewidth=3,
         marker='s', markersize=20,
         mew=5, mec='blue', mfc='lightblue')

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