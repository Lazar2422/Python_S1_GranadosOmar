def intsimple(x,b,a):
    m=x*(1+b*a)
    return print("El valor final del interes es de: ",m)
def intcom(x,b,a):
    cf=x*(1+b)**a
    x=cf
    return print("El valor final del interes es de: $", cf)

f=int(input("Para interes simple presione 1, para interes compuesto presione 2 "))
if f==1:
    c=float(input("Ingrese el valor del capital inicial "))
    p=float(input("Ingrese la tasa de interes "))
    n=int(input("Indique el numero de periodos que se generaran los intereses "))
    intsimple(c,p,n)
elif f==2:
    c=float(input("Ingrese el valor del capital inicial "))
    p=float(input("Ingrese la tasa de interes "))
    n=int(input("Indique el numero de periodos que se generaran los intereses "))
    intcom(c,p,n)

