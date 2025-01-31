import math
def primo(x):
    a=0
    if x%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")
    for i in range(1,x+1):
        ## preguntar
        if x%i==0:
            a=a+i
    if a==x+1:
        print("El numero es primo")
    else:
        print("Es un numero compuesto")
    b=float(math.sqrt(x))
    if x%b==0:
        print("El numero es un cuadrado perfecto")
    else:
        print("El numero no es un cuadrado perfecto")

n=int(input("Ingrese un numero para averiguar si es par, si es primo y si es un cuadrado perfecto "))
primo(n)