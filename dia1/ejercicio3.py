## comienzo
print("Los numeros que cumplen con la expresion (p^3 + q^4 -2*p^2) < 680 son: ")
## escribimos lo que el algoritmo va a retornar
p=0
q=0
## damos valor a las variables que vamos a usar
for i in range(10):
    ## hacemos el ciclo
    a=(p**3 + q**4 -2*p**2)
    if a < 680:
        ## hacemos el condicional
        print(p," ", q)
        ## los numeros que cumplan con el condicional se imprimen
    p=p+1
    q=q+1
    ## autoincrementamos p y q para que no siempre retorne el mismo valor

## algoritmo diseñado por: Omar Fernando Granados Parra