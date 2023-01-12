f = input("Digite uma frase (Não coloque acentos e caracteres especiais): ")
nf = f.lower()
r = (" ", ",", ".", "!", "-")
for c in r:
    nf = nf.replace(c, "")

if nf == nf[::-1]: print(f, "é palíndromo")
else: print(f, "não é palíndromo")