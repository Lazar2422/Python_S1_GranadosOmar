from b import *
nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]
apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
t=True
while t==True:
    print("Presione 1 para ver estudiantes")
    print("Presione 2 para editar estudiante")
    print("Presione 3 para eliminar estudiante")
    print("Presione 4 para añadir estudiante")
    print("Presione 5 para salir")
    b=int(input(":" ))
    if b==2:
        f=True
        while f==True:
            n=int(input("Ingrese el numero del estudiante a editar: "))
            n=n-1
            nombrenuevo=input("Ingrese el nuevo nombre para el estudiante: ")
            apellidonuevo=input("Ingrese el apellido nuevo para el estudiante: ")
            lista(nombres,n,nombrenuevo,apellidos,apellidonuevo)
            y=int(input("Desea seguir editando? (1=si || 2=no) "))
            if y==2:
                f=False
    elif b==4:
        f=True
        while f==True:
            nombrenuevo=input("Ingrese el nombre del estudiante nuevo: ")
            apellidonuevo=input("Ingrese el apellido del estudiante nuevo: ")
            añadir(nombres,nombrenuevo,apellidos,apellidonuevo)
            y=int(input("Desea seguir añadiendo estudiantes? (1=si || 2=no) "))
            if y ==2:
                f=False
    elif b==3:
        f=True
        while f==True:
            n=int(input("Ingrese el numero del estudiante a eliminar: "))
            n=n-1
            delete(nombres,n,apellidos)
            y=int(input("Desea seguir eliminando estudiantes? (1=si || 2=no) "))
            if y == 2:
                f=False
    elif b==1:
        nom(nombres,apellidos)
    elif b==5:
        t=False