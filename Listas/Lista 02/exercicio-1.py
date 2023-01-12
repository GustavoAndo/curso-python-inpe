a = float(input("Digite o valor do primeiro número: "))
b = float(input("Digite o valor do segundo número: "))
c = float(input("Digite o valor do terceiro número: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

print('O maior número é:', maior)
print('O menor número é:', menor)