import string
import random
longitud=int(input("Ingrese la longitud de la cadena "))
pasword=string.ascii_uppercase + string.ascii_lowercase + "!#$%&/()=¿?*+-{}[]" + "0123456789"
cadena=" "
for _ in range (longitud):
    cadena += random.SystemRandom().choice(pasword)
print(cadena)