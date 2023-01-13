g = float(input("Insira o valor de gain: "))
o = float(input("Insira o valor de offset: "))
i = 20

r = i * g + o

if r > 250: r = 250
elif r < 0: r = 0

print(r)