palavras = ['significado', 'exceção', 'impressão', 'ciência','respeito', 'fato', 'maturidade', 'essencial','paradigma', 'propósito', 'viés', 'vereda' ]

repetir = True
while repetir:
    texto = input("Digite um texto: ")
    
    palavras_contidas = []
    contador = 0
    for p in texto.split():
        if p in palavras:
            palavras_contidas.append(p)
            contador += 1

    print(f"\nOcorreram {contador} palavras da lista")
    for p in palavras_contidas:
        print(p)

    while True:
        continuar = input("\nDeseja continuar?(S/N) ")
        if continuar == "S": break
        elif continuar == "N":
            repetir = False
            break
        else: print("Erro! Digite S (para sim) ou N (para não)!")

