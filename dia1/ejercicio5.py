print("secuencia: 1,1,2,-1,1,-2,?") 
## mostramos la secuencia de los numeros
a=1
b=1
## definimos los dos primeros numeros
print("secuencia")
print("paso 1: 1")
print("paso 2: 1")
for i in range (1,6):
## realizamos un bucle para la secuencia
    if i%2==0:
        c=a-b
        a=b
        b=c
        ## hacemos un condicional que si se cumple el siguiente numero de la secuencia es c
    else:
        c=a+b
        a=b
        b=c
        ## hacemos una alternativa al condicional anterior por si no se cumple
    print("paso ",i+2,": ",c)
    ## imprimimos el numero del paso con el numero correspondiente a ese pasoe n la secuencia

## Algoritmo diseñado por Omar Fernando Granados Parra
