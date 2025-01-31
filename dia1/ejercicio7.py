x=int(input("Ingrese el primer numero: "))
y=int(input("Ingrese el segundo numero: "))
## Indicamos los datos que le vamos a pedir al usuario
a=0
b=0
for i in range(1,x+1):
    ## creamso un ciclo para el primer numero
    if x%i == 0:
        a=a+i
        ## si cumple con la condicion el numero se guarda en la variable
for i in range(1,y+1):
    ## creamos un ciclo para el segundo numero
    if y%i ==0:
        b=b+i
        ## si cumple con la condicion el numero se guarda en la variable
if a==b:
    print("Son numeros amigos")
    ## si cumple con la condicion retorna el texto
else:
    print("No son numero amigos")
    ## si no cumple con la condicion retorna el texto

## algoritmo diseñado por: Omar Fernando Granados Parra