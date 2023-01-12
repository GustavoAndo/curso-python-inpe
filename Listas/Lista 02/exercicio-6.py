n = input("Digite um conceito final em uma disciplina hipotética: ")

if n == "A+": print("Excepcional!")
elif n == "A" or n == "A-": print("Excelente!")
elif n == "B+" or n == "B" or n == "B-": print("Bom!")
elif n == "C+" or n == "C" or n == "C-": print("Regular!")
elif n == "D": print("Reprovação!")
else: print("Conceito inválido!")