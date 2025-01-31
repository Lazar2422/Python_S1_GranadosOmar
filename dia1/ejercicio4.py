## empezamos :D
print("Ingrese el numero ", 1, ": ")
a=float(input())
## aclaramos lo que el algoritmo va a retornar
b=a
## hacemos una variable que sea igual al numero ingresado
for i in range(2,11):
    ## hacemos el ciclo
    print("Ingrese el numero: ", i)
    c=float(input())
    ## indicamos que ingrese un valor para cada ciclo
    if c>=a:
        ## hacemos un condicional
        ma=c
        ## si c es mayor al numero indicado anteriormente entonces el mayor pasa a ser c
        a=c
        ## para seguir con las comparaciones el actual mayor numero pasa a ser "a"
    elif c<=b:
        ## hacemos otro condicional por si no se cumple la anterior condicion
        me=c
        ## si el numero ingresado es menor al primer numero entonces el menor sera c
        b=c
        ## para seguir con las comparaciones b toma el valor del menor numero

print("El mayor es: ", ma)
print("El menor es: ", me)
## se imprime el mayor y el menor de los numeros ingresados en la comparacion

## Algoritmo diseñado por: Omar Fernando Granados Parra