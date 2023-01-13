numeros = input("Digite uma sequência de números separadas por vírgula (Exemplo: 1,-1,0,2.1): ")

numeros.replace(" ", "")
s = 0
c = 0
for n in numeros.split(","):
    s += float(n)
    c += 1

print("A média da sequência de números é:", s/c)