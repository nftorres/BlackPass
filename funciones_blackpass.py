"""
Este módulo contiene las funciones para mejorar la estética del programa y también para generar, 
hashear y guardar las contraseñas de BlackPass.
"""
import random, string, bcrypt, sys, subprocess
from time import sleep

def escribir(cadena, salto=True):
    """
    La función "escribir" imprime una cadena determinada carácter por carácter con un pequeño retraso
    entre cada carácter y un salto de línea opcional al final.
    
    :param cadena: La cadena de entrada que debe imprimirse
    :param salto: Un parámetro booleano que determina si agregar o no un salto de línea después de
    imprimir la cadena. Si se establece en Verdadero, se agregará un salto de línea. Si se establece en
    False, no se agregará ningún salto de línea, defaults to True (optional)
    """
    for i in cadena:
        print(i, end="")
        sys.stdout.flush()
        sleep(0.04)
    if salto:
        print("\n")
def mostrar_creditos():
    escribir("---------------------------Hecho con Amor por Fabián---------------------------")
def config_contraseña(longitud_contraseña):
    """
    Esta función solicita al usuario que elija un tipo de contraseña (solo dígitos, solo letras o
    alfanumérica) y genera una contraseña de la longitud especificada según la elección del usuario.
    
    :param longitud_contraseña: La longitud de la contraseña que el usuario quiere generar
    :return: una contraseña generada basada en la entrada del usuario para el tipo de contraseña deseado
    (solo dígitos, solo letras o alfanumérico) y la longitud deseada de la contraseña.
    """
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
            escribir("Lo siento, no entendí lo que quisiste decir.")
            continue

def generar_contraseña(longitud=12, digitos=True, letras=True):
    """
    Esta función genera una contraseña aleatoria de una longitud específica con una combinación de
    letras y/o dígitos.
    
    :param longitud: La longitud de la contraseña que se va a generar. De forma predeterminada, se
    establece en 12 caracteres, defaults to 12 (optional)
    :param digitos: Un valor booleano que indica si incluir o no dígitos en la contraseña generada. Si
    es Verdadero, se incluirán los dígitos. Si es Falso, no se incluirán, por defecto el valor es True (opcional)
    :param letras: Un parámetro booleano que determina si incluir o no letras en la contraseña generada.
    Si se establece en Verdadero, la contraseña incluirá letras; si se establece en False, la contraseña
    solo incluirá dígitos, por defecto el valor es True(opcional)
    :return: una contraseña generada aleatoriamente como una cadena. La longitud de la contraseña está
    determinada por el parámetro `longitud`, y los caracteres utilizados en la contraseña están
    determinados por los parámetros `digitos` y `letras`. Si `digitos` es True, la contraseña puede
    contener dígitos (0-9), y si `letras` es True, la contraseña puede contener letras(A-Z) tanto mayúsculas como en minúsculas
    """
    contraseña = ""
    posiciones = [1,2]
    while len(contraseña) < longitud:
        tipo_caracter = random.choice(posiciones)
        if digitos and letras:
            if tipo_caracter == 1:
                contraseña += random.choice(string.digits)
            else:
                contraseña += random.choice(string.ascii_letters)
        elif digitos:
            contraseña += random.choice(string.digits)
        else:
            contraseña += random.choice(string.ascii_letters)
    return contraseña

def hashear(contraseña):
    """
    La función "hashear" toma una contraseña, la codifica, genera una sal, procesa la
    contraseña con la sal usando bcrypt y devuelve el hash de contraseña resultante.
    
    :param contraseña: El parámetro "contraseña" es una cadena que representa una contraseña que debe
    cifrarse mediante el algoritmo bcrypt
    :return: la versión hash de la contraseña de entrada utilizando la biblioteca bcrypt.
    """
    contraseña = contraseña.encode()
    sal = bcrypt.gensalt()
    hash_contraseña = bcrypt.hashpw(contraseña,sal)
    return hash_contraseña

def generar_id():
    """
    La función genera una identificación aleatoria de 10 dígitos usando dígitos del módulo string.
    """
    id = ""
    for i in range(10):
        id += random.choice(string.digits)
    return id

def guardar_hash(hash_contraseña):
    """
    Esta función guarda un hash de contraseña en un archivo, genera una ID para él y confirma y envía
    los cambios a un repositorio de Git.
    
    :param hash_contraseña: La contraseña hash que debe guardarse en un archivo
    :return: la identificación generada para el hash de contraseña que se guardó en el archivo
    'Credenciales.txt' y se comprometió con el repositorio de Git.
    """
    id = generar_id()
    f = open('Credenciales.txt','a')
    f.writelines(f'id:{id} -> {hash_contraseña}\n')
    f.close()
    subprocess.run(["git", "add", "Credenciales.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "commit", "-m", "Add new password"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "push"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return id





