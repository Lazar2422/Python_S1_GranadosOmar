import json
def abrirJSON():
    hola123={}
    with open("./dbb.json",'r') as openFile:
        hola123=json.load(openFile)
    return hola123

def guardarJSON(dic):
    with open("./dbb.json",'w') as outFile:
        json.dump(dic,outFile)
f=True
d={}
while f==True:
    d=abrirJSON()
    print("Que desea hacer?")
    print("Para buscar inmuebles por precio presione 1")
    print("Para crear inmuebles presione 2")
    print("Informacion inmuebles presione 3")
    print("Para actualizar inmuebles presione 4")
    print("Para eliminar inmuebles presione 5")
    print("Para salir presione 6")
    x=int(input(": "))
    if x==3:
        for i in range(len(d["0"])):
            y=str(0)
            met1=d[y][i]
            hab1=d[y][i]
            gar1=d[y][i]
            año1=d[y][i]
            zon1=d[y][i]
            met=met1["metros"]
            hab=hab1["habitaciones"]
            gar=gar1["garaje"]
            año=año1["aÃo"]
            zon=zon1["zona"]
            print("Inmueble: ", i+1, " año: ", año, " metros: ", met, " habitaciones: ", hab, " garaje: ", gar, " zona: ", zon)
    elif x==1:
        pre=float(input("Ingrese el presupuesto: "))
        for i in range(len(d)):
            y=str(0)
            h=d[y]
            met1=h[i]
            hab1=h[i]
            gar1=h[i]
            año1=h[i]
            zon1=h[i]
            met=met1["metros"]
            hab=hab1["habitaciones"]
            gar=gar1["garaje"]
            año=año1["aÃo"]
            zon=zon1["zona"]
            if gar=="True":
                gar2=1
            elif gar=="False":
                gar2=0
            if zon=="A":
                p=(met*1000+hab*5000+gar2*15000)*(1-((2025-año)/100))
            elif zon=="B":
                p=(met*1000+hab*5000+gar2*15000)*(1-((2025-año)/100))*1.5
            if p<=pre:
                print("El inmueble ", i+1, " es accesible a su presupuesto")
                print("El valor del imnueble ", i+1, " es de: $",p)
    elif x==2:
        año=int(input("Ingrese el año desde que se creo el inmueble: "))
        met=float(input("Ingrese los metros del nuevo inmueble: "))
        hab=int(input("Ingrese el numero de habitaciones del inmueble: "))
        gar=int(input("Escriba 1 si cuenta con garaje || escriba 2 si no cuenta con garaje: "))
        zon=input("Ingrese la zona del inmueble (A o B): ")
        if gar==1:
            gar1="True"
        elif gar==2:
            gar1="False"
        b=str(0)
        i=len(d[b])
        h=d[b]
        h[i]=({"a\u00c3o":año,"metros":met,"habitaciones":hab,"garaje":gar1,"zona":zon})
        d[b].extend(h[i])
        guardarJSON(d)
    elif x==4:
        x=int(input("Ingrese el numero del inmobiliario a actualizar: "))
        año=int(input("Ingrese el año desde que se creo el inmueble: "))
        met=float(input("Ingrese los metros del nuevo inmueble: "))
        hab=int(input("Ingrese el numero de habitaciones del inmueble: "))
        gar=int(input("Escriba 1 si cuenta con garaje || escriba 2 si no cuenta con garaje: "))
        zon=input("Ingrese la zona del inmueble (A o B): ")
        if gar==1:
            gar1="True"
        elif gar==2:
            gar1="False"
        b=x-1
        y=str(b)
        d[y]=[{"a\u00c3o":año,"metros":met,"habitaciones":hab,"garaje":gar1,"zona":zon}]
        guardarJSON(d)
    elif x==5:
        x=int(input("Ingrese el numero del inmobiliario a eliminar: "))
        b=x-1
        c=d["0"]
        del c[b]
        guardarJSON(d)
    elif x==6:
        f=False