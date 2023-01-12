print("0 Lucas\n1 Pell\n2 Triangular\n3 Square\n4 Pentagonal")

n = int(input("Qual série você deseja computar? "))

if n < 0 or n > 4: print("Valor inválido!")
elif n == 0: e = "Lucas"
elif n == 1: e = "Pell"
elif n == 2: e = "Triangular"
elif n == 3: e = "Square"
else: e = "Pentagonal"

print(f'Você escolheu computar a série "{e}"!')