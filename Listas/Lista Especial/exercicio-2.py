def soma_digitos(txt):
    s = 0
    for l in txt:
        s += int(l)
    return s

numero_txt = input("Digite um conjunto de digitos: ")

print(f'O valor da soma dos digitos de "{numero_txt}" é {soma_digitos(numero_txt)}') 