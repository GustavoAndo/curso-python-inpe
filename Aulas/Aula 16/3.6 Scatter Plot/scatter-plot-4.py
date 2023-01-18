import matplotlib.pyplot as plt

# valores dos eixos
ano = [ 1900, 1920, 1940, 1960, 1970, 1980, 1990, 2000, 2010 ]
populacao = [ 17.438, 30.635, 41.236, 51.944, 70.992, 121.150, 146.917, 169.590, 190.755 ]

# cores numerados de 0 a 8
cores = [ x for x in range( len( ano ) ) ]

# tamanho da figura
plt.figure( figsize=(10, 8) )

# criando o grafico
# utilizando o jargão cmap com o atributo raibow para fazer os pontos ficarem coloridos igual ao arco-íris
plt.scatter(ano, populacao, marker="s", s=50, c=cores, cmap="rainbow")

# titulo dos eixos
plt.xlabel("Ano")
plt.ylabel("Estimativa da População")

# titulo do grafico
plt.title("Evolução da População Brasileira")

# rotulos do eixo y
plt.yticks([ 50, 100, 150, 200 ],
           [ '50M', '100M', '150M', '200M' ] );

# mostra grafico
plt.show()