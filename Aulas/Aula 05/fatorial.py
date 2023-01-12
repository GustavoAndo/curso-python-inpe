while True:
    n = int(input("Digite um número de 1 a 10: "))

    if n < 1 or n > 10: print('Número inválido!')
    else: break

f = 1
for i in range(1, n+1):
    f *= i

print(f)
