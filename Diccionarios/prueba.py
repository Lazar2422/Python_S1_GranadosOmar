numeros = [1,2,3,4,5,6,7,8,9,10]
letras = ["a","b"]
numeros.extend(letras)
print(numeros)
print(numeros[2])

del numeros[4]
print(numeros)

print(numeros[0:3])
for a in numeros:
    print(a)

p=[1,2]
p += [3,4,5]
print(p)

for p, b in enumerate(numeros):
    print(p,b)
h=numeros.count(2)
print(h)

z = numeros[7]
print(z)
numeros.remove(7)
z = numeros[7]
del numeros
numeros = []
numeros.append(z)
print(numeros)
## print(z)
## print(numeros)
## numeros.reverse()
## print(numeros)
## print(numeros[2])
x=["hola", "profesional", "mundo", "amazing"]
print(x)
x.sort()
print(x)