def lucas(n):
    print("Lucas: ", end="")
    a = 2
    print(a, end="")
    b = 1
    if n > 0: print(",", b, end="")
    for i in range (2, n+1):
        l = b + a
        print(",", l, end="")
        a = b
        b = l
    print()

def pell(n):
    print("Pell: ", end="")
    a = 0
    print(a, end="")
    b = 1
    if n > 0: print(",", b, end="")
    for i in range (2, n+1):
        p = 2 * b + a
        print(",", p, end="")
        a = b
        b = p
    print()

def triangular(n):
    print("Triangular: ", end="")
    a = 0
    print(a, end="")
    for i in range (1, n+1):
        t = (i * (i + 1)) // 2
        print(",", t, end="")
    print()

def square(n):
    print("Square: ", end="")
    a = 0
    print(a, end="")
    for i in range (1, n+1):
        s = i * i
        print(",", s, end="")
    print()

def pentagonal(n):
    print("Pentagonal: ", end="")
    a = 0
    print(a, end="")
    for i in range (1, n+1):
        p = (3 * i**2 - i) // 2
        print(",", p, end="")
    print()


while True:
    n = int(input("Digite um número natural: "))
    if n >= 0: 
        lucas(n)
        pell(n)
        triangular(n)
        square(n)
        pentagonal(n)
        break
    else: print("Número inválido!")
print()