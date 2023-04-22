import random, string, bcrypt, sys
from time import sleep

def output(string):
    for i in string:
        print(i, end="")
        sys.stdout.flush()
        sleep(0.04)
    print("\n")
def footer():
    output("---------------------------Hecho con Amor por Fabián---------------------------")
def config_contraseña(longitud_contraseña):
    while True:
        config = input("¿Cómo quieres que sea tu contraseña (Sólo digitos/Sólo letras/Alfanumérica)?: ")
        if  config.lower() == 'sólo dígitos' or config.lower() == 'solo digitos' or config.lower() == 'sólo digitos' or config.lower() == 'solo dígitos':
            output(generar_contraseña(longitud=longitud_contraseña, letras=False))
            break
        elif config.lower() == 'sólo letras' or config.lower() == 'solo letras':
            output(generar_contraseña(longitud=longitud_contraseña, digitos=False))
            break
        elif config.lower() == 'alfanumerica' or config.lower() == 'alfanumérica':
            output(generar_contraseña(longitud=longitud_contraseña))
            break
        else:
            output("Lo siento, no entendí lo que quisiste decir.")
            continue

def generar_contraseña(longitud=12, digitos=True, letras=True):
    password = ""
    posiciones = [1,2]
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





