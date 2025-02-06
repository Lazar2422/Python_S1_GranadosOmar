import json
def abrirJSON():
    dicFinal={}
    with open("./d.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./d.json",'w') as outFile:
        json.dump(dic,outFile)
f=True
d={}
while f==True:
    d=abrirJSON()
    print("que desea hacer")
    print("1. ver los contactos")
    print("2. añadir contactos")
    print ("3. actualizar un contacto")
    print("4. eliminar un contacto")
    opcion=int(input(": "))
    if opcion==1:
        for i in range(len(d)):
            z=str(i)
            nombre1=d[z][0]
            telefono1=d[z]
            correo_electronico1=d[z]
            direccion1=d[z]
            fecha_de_nacimiento1=d[z]
            print(nombre1["Nombre Completo"])