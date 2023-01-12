s = input("Digite uma palavra (Não coloque acentos e caracteres especiais): ").lower().replace(" ", "")

if s == s[::-1]: print(s, "é palíndromo")
else: print(s, "não é palíndromo")