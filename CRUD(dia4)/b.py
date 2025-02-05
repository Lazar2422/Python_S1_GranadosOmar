def lista(a,b,e,f,g):
    a[b]=e
    f[b]=g
def añadir(a,b,e,f):
    a.append(b)
    e.append(f)
def delete(a,b,e):
    del a[b]
    del e[b]
def nom(a,b):
    for i in range(len(a)):
        print("Estudiante ", i+1, " ".join(a[i]), " ".join(b[i]))