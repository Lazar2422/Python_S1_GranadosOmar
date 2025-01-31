print("hello world!")

## num1 = float(input("Ingresa el primer numero "))
## num2 = float(input("Ingresa el primer numero "))
## 
## suma = num1 + num2
## print("el resultado de la suma es: ", suma)

for i in range(1,5):
    print(i)


si=False

while(si == False):
    print(si)
    si=True

def funcion1():
    print("5x30")

funcion1()

def funcion2():
    return 5
print("su numero es:", funcion2())


def funcion3(nombre, apellido):
    print("Su nombre es: ", nombre, " ", apellido)
funcion3("5x", "30")

def funcion4(a,b):
    c=a**b
    return c

funciona=int(input("Ingrese el numero base: "))
funcionb=int(input("Ingrese el numero a elevar: "))


print("el resultado de la potencia es: ", funcion4(funciona, funcionb))