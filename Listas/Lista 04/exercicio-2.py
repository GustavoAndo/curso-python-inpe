senha = input("Digite uma senha: ")

minusculo = False
maiusculo = False

for i in senha:
    if i.islower(): minusculo = True
    elif i.isupper(): maiusculo = True 

if minusculo and maiusculo and len(senha) >= 8: print("Senha forte!")
else: print("Senha fraca.")