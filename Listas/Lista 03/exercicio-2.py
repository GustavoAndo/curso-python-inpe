continuar = True
while continuar:
    n1 = float(input("Digite o primeiro número operando: "))
    n2 = float(input("Digite o segundo número operando: "))

    val = True
    while val:  
        o = input("Digite o operador(+, -, * ou /): ")

        val = False
        if o == "+": print(n1, "+", n2, "=", n1 + n2)
        elif o == "-": print(n1, "-", n2, "=", n1 - n2)
        elif o == "*": print(n1, "*", n2, "=", n1 * n2)
        elif o == "/": print(n1, "/", n2, "=", n1 / n2)
        else: 
            print("Operação inválida")
            val = True
    
    while True:
        c = input("Deseja continuar?(S/N) ")
        if c != "S" and c != "N": print("Valor inválido. Digite S ou N!")
        elif c == "N": 
            continuar = False
            break
        else: break