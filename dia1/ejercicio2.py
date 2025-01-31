## iniciamos el algoritmo
n = int(input("Ingrese el numero de la serie que desea ver: "))
## preguntamos al usuario el numero de la serie
a=0
b=0
## aclaramos el valor de las variables a usar
for i in range(1,n+1):
    ## creamos el ciclo
    if i % 2 ==0:
        ## creamos el condicional
        a=a-(1/i)
        ## si cumple con la condicion se guarda en la variable
    else:
        b=b+(1/i)
        ## si no cumple con la condicion se guarda en la anterior variable
c=a+b
## hacemos la operacion
print("el resultado de la serie es: ", c)
## retornamos el valor de la serie

## algoritmo diseñado por: Omar Fernando Granados Parra