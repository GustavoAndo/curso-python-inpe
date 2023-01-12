n = int(input("Digite um número maior que 0: "))

if n > 0:
    if n % 2 == 0 and n % 3 == 0: print("O número é divisível por 2 e 3!")
    elif n % 2 == 0: print("O número é divisível por 2!")
    elif n % 3 == 0: print("O número é dívisel por 3!")
    else: print("O número não é divisível por 2 e 3!")
else:
    print("Você digitou um número menor que 0!")