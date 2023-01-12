cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Ouro Preto"]
print(cidades)

# Ordenando a lista
cidades.sort()
print(cidades)

# Gera uma nova lista "ordenada ao contrário"
nova_lista = sorted(cidades, reverse=True)
print(nova_lista)
print(cidades)

# Adicionar item no final da lista
cidades.append("São José dos Campos")
print(cidades)

# Remover item
del cidades[1]
print(cidades)

# Adicionar itens de uma lista no fim de outra
cidades.extend( ["Ouro Preto", "Mariana"] )
print(cidades)

# Inverte a lista
cidades.reverse()
print(cidades)

# Outras formas de construir uma lista:

l_letras = list( "Gilberto" )
print(l_letras)

primos = list( (1, 2, 3, 5, 7) )
print(primos)

seq1 = list( range(10) )
print(seq1)

seq2 = list( range(3, 10) )
print(seq2)

# List Comprehension

f_ident = [ x for x in range(0, 10) ]
print(f_ident)

f_quad = [ x**2 for x in range(0, 10) ]
print(f_quad)

f_exp = [ 2**x for x in range(0, 10) ]
print(f_exp)