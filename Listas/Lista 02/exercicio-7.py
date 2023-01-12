n1 = float(input("Digite o primeiro operando: "))
n2 = float(input("Digite o segundo operando: "))

o = input("Digite o operador(+, -, * ou /): ")

if o == "+": print(n1, "+", n2, "=", n1 + n2)
elif o == "-": print(n1, "-", n2, "=", n1 - n2)
elif o == "*": print(n1, "*", n2, "=", n1 * n2)
elif o == "/": print(n1, "/", n2, "=", n1 / n2)
else: print("Operação inválida")