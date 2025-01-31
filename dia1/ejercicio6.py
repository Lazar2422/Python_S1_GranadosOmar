n=int(input("Ingrese el numero de empleados: "))
## indicamos al usuario que ingrese el numero de empleados
jh=0
hj=0
tsb=0
teps=0
tsn=0
tpens=0
nome=""
nomm=""
men=0
may=0
## definimos dos variables de comparacion
for i in range(1, n+1):
    ## hacemos el ciclo
    print("Ingrese el nombre del empleado ", i)
    nom=input("")
    ## indicamos al usuario que ingrese el nombre del empleado
    print("Ingrese el numero de horas trabajadas para el empleado ", i)
    h=float(input())
    ## indicamos al usuario que ingrese el numero de horas trabajadas
    sb=h*20000
    ## sueldo bruto
    tsb=tsb+sb
    ## total sueldo bruto
    eps=sb*0.4
    ## eps
    pens=eps
    ## pension
    sn=sb-eps-pens
    ## sueldo neto
    teps=teps+eps
    ## total eps
    tpens=teps
    ## total pension
    tsn=tsn+sn
    ## total sueldo neto
    if h<=hj:
        hj=h
        nome=nom
        men=sn
    if h>jh:
        ## un condicional
        nomm=nom
        hj=jh
        jh=h
        may=sn
        ## si cumplen con el condicional las variables toman el valor indicado
        ## si cumplen con el otro condicional las variables toman el valor indicado
print("El total de salario bruto es: ", tsb)
print("El total de pension es: ", tpens)
print("El total de eps es: ", teps)
print("El total del salario neto es: ", tsn)
print("El nombre del empleado que mas sueldo gano fue: ",nomm," con un salario neto de: ",may)
print("El nombre del empleado que menos sueldo gano fue: ",nome," con un salario neto de: ",men)
print("El promedio de los salarios brutos es de: ", (tsb/n))
print("El promedio de los salarios netos es de: ", (tsn/n))
## se retorna el valor para cada uno de los datos calculados añadiendo el empleado que mas gano y el que menos gano

## alogritmo diseñado por: Omar Fernando Granados Parra