def grados(x):
    a=int(input("1: De celsius a farenheit || 2: De fahrenheit a celsius "))
    if a == 1:
        b=x*1.8 + 32
        return print(b)
    elif a == 2:
        b= (x-32)*5/9
        return print(b)
    else:
        print("Dato invalido")

gra=float(input("Ingrese el valor a covertir "))
if gra!=int:
    print("Dato invalido")
else:
    grados(gra)