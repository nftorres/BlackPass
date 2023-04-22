import random, string, bcrypt, sys, subprocess
from time import sleep

def output(string, salto="\n"):
    for i in string:
        print(i, end="")
        sys.stdout.flush()
        sleep(0.04)
    if salto == '\n':
        print(salto)
def footer():
    output("---------------------------Hecho con Amor por Fabián---------------------------")
def config_contraseña(longitud_contraseña):
    while True:
        print()
        config = input("¿Cómo quieres que sea tu contraseña (Sólo digitos/Sólo letras/Alfanumérica)?: ")
        if  config.lower() == 'sólo dígitos' or config.lower() == 'solo digitos' or config.lower() == 'sólo digitos' or config.lower() == 'solo dígitos':
            return generar_contraseña(longitud=longitud_contraseña, letras=False)
        elif config.lower() == 'sólo letras' or config.lower() == 'solo letras':
            return generar_contraseña(longitud=longitud_contraseña, digitos=False)
        elif config.lower() == 'alfanumerica' or config.lower() == 'alfanumérica':
            return generar_contraseña(longitud=longitud_contraseña)
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
    return password_hash

def generar_id():
    id = ""
    for i in range(10):
        id += random.choice(string.digits)
    return id

def guardar_hash(password_hash):
    id = generar_id()
    f = open('Credenciales.txt','a')
    f.writelines(f'id:{id} -> {password_hash}\n')
    f.close()
    subprocess.run(["git","add", "Credenciales.txt"])
    subprocess.run(["git","commit", "-m", "'Add new password'"])
    subprocess.run(["git","push"])
    return id





