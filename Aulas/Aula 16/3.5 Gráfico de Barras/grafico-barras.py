import matplotlib.pyplot as plt

# valores dos eixos
ano = [ 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 ]
num_focos = [ 123201, 123120, 249198, 132893, 193600, 115046, 183424, 236066, 188044, 260051 ]

# posições das barras
x_pos = [ x for x in range( len(ano) ) ]

# tamanho da figura
plt.figure( figsize=(10, 8) )

# criando gráfico de barras na vertical
# x_pos -> posição das barras
# num_focos -> valores do eixo y
# align -> alinhamento
# color -> cor
# linewidth -> espessura da borda
# edgecolor -> cor da borda
plt.bar(x_pos, num_focos, align='center',
        color='Crimson', linewidth=2, edgecolor='black')
# Obs: para criar na horizontal, utiliza-se hbar

# adicionando rótulos dos eixos
plt.yticks([ 0, 75000, 150000, 225000, 300000 ],
           [ "0", "75 mil", "150 mil", "225 mil", "300 mil" ] )
plt.xticks(x_pos, ano, rotation=45) 
# rotation -> serve para deixar o rotulo inclinado de acordo com o grau colocado, nesse caso em 45 graus

# titulo
plt.title("Focos de Queimadas - Brasil")

# titulo dos eixos
plt.xlabel("Ano")
plt.ylabel("Número de Focos Detectados")

# detalhes do fundo
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# mostrar gráfico
plt.show()