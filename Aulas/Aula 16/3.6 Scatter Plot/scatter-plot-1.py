import matplotlib.pyplot as plt

# valores dos eixos
ano = [ 1900, 1920, 1940, 1960, 1970, 1980, 1990, 2000, 2010 ]
populacao = [ 17.438, 30.635, 41.236, 51.944, 70.992, 121.150, 146.917, 169.590, 190.755 ]

# tamanho da figura
plt.figure( figsize=(10, 8) )

# criando gráfico de pontos
plt.scatter(ano, populacao)

# titulo dos eixos
plt.xlabel("Ano")
plt.ylabel("Estimativa da População")

# titulo do grafico
plt.title("Evolução da População Brasileira")

# rotulos do eixo y
plt.yticks([ 50, 100, 150, 200 ],
           [ '50M', '100M', '150M', '200M' ] );

# detalhes do fundo
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# mostra grafico
plt.show()