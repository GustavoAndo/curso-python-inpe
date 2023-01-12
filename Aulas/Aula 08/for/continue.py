#
# Dado um intervalo fornecido pelo usuário,
# escreva na tela todos os números pares dentro do intervalo.
#
 
menor = int(input("Digite o menor valor do intervalo:"))
maior = int(input("Digite o maior valor do intervalo:"))
 
for x in range(menor, maior + 1):
    if(x % 2):
        continue
 
    print(x)