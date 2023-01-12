n = int(input("Digite um número de 0 a 10: "))

if 0 <= n <= 10:
    if n % 2 == 0: print("O número é par!")
    else: print("O número é ímpar!")
else: print("Número fora do intervalo de 0 a 10")