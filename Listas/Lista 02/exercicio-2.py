a = float(input("Digite o valor do primeiro lado do triângulo: "))
b = float(input("Digite o valor do segundo lado do triângulo: "))
c = float(input("Digite o valor do terceiro lado do triângulo: "))

if b + c <= a or a + b <= c or a + c <= b: print("Não é possível formar um triângulo!")
elif a == b == c: print("O triângulo é equilátero!")
elif a == b or b == c or a == c: print("O triângulo é isóceles!")
else: print("O triângulo é escaleno!")