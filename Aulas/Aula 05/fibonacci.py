while True:
    n = int(input("Digite um número maior que 1: "))

    if n < 2: print('Número inválido!')
    else: break

f0 = 0
print(f0)

f1= 1
print(f1)

for i in range(1, n):
    f = f0 + f1
    print(f)

    f0 = f1
    f1 = f