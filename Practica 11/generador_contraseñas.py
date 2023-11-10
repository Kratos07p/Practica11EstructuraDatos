import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña