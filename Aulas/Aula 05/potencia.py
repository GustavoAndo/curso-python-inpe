x = int(input("Digite um número da base: "))
y = int(input("Digite um número do expoente: "))

p = 1
if y < 0:
    x = 1 / x
    for i in range(y * -1):
        p *= x   
else:
    for i in range(y):
        p *= x

print(p)