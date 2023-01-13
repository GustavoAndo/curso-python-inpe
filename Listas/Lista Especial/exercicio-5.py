lista_palavras = []

repetir = True
while repetir:
    palavra = input("Digite uma palavra: ")
    lista_palavras.append(palavra)

    while True:
        continuar = input("Deseja digitar outra palavra?(S/N) ")
        if continuar == "S": break
        elif continuar == "N":
            repetir = False
            break
        else: print("Erro! Digite S (para sim) ou N (para não)!")

print("\nAs palavras digitadas foram:")
for p in lista_palavras:
    print(p)