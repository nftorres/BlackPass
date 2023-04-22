import random
import string
import bcrypt
def generar_contraseña(longitud=12, digitos=True, letras=True):
    password = ""
    posiciones = [1,2]
    while longitud >= 4 and longitud <= 40:
        while len(password) < longitud:
            tipo_caracter = random.choice(posiciones)
            if digitos and letras:
                if tipo_caracter == 1:
                    password += random.choice(string.digits)
                else:
                    password += random.choice(string.ascii_letters)
            elif digitos:
                password += random.choice(string.digits)
            else:
                password += random.choice(string.ascii_letters)
        break
    return password

def hashear(password):
    password = password.encode()
    sal = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password,sal)
    print(password_hash)
    return password_hash

def guardar_hash(password_hash):
    f = open('Credenciales.txt','a')
    f.writelines(f'Hash: {password_hash}\n')
    f.close()




