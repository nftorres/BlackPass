"""
Autor: Fabián Torres
Fecha de creación: 19 de abril de 2023
Última actualización: 23 de abril de 2023

Descripción:
Este módulo contiene la función blackpass que genera un contraseña aleatoria según las 
especificaciones del usuario, obtiene la versión de hash de la contraseña generada usando 
la librería bcrypt y lo almacena en un archivo de manera local y remota.
"""
from funciones_blackpass import *


def blackpass():
    escribir(
        "---------------------------BlackPass V1-Español---------------------------")
    escribir("Generador de contraseñas :)")
    while True:
        longitud_contraseña = int(input("Longitud de la contraseña(Min:1 - Max:40): "))
        if longitud_contraseña > 0 and longitud_contraseña < 4:
            contraseña = config_contraseña(longitud_contraseña)
            print()
            escribir("Contraseña Generada: ", salto=False)
            escribir(contraseña)
            escribir(f"Esta contraseña es mala porque sólo contiene {longitud_contraseña} caracteres...")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                escribir("-----------------------")
                print()
                continue
            else:
                escribir(
                    "------------------------------------------------------------------")
                escribir("Información de la contraseña:")
                escribir("Contraseña: ", salto=False)
                escribir(contraseña)
                hash_contraseña = hashear(contraseña)
                id = guardar_hash(hash_contraseña)
                escribir("id: ", salto=False)
                escribir(id)
                escribir("Hash: ", salto=False)
                print(hash_contraseña, end="\n\n")
                escribir("Función de Hash: bcrypt")
                escribir("Destino: 'Credenciales.txt'")
                mostrar_creditos()
                break
        elif longitud_contraseña >= 4 and longitud_contraseña <= 9:
            contraseña = config_contraseña(longitud_contraseña)
            print()
            escribir("Contraseña Generada: ", salto=False)
            escribir(contraseña)
            escribir(
                f"Esta contraseña es insegura, un hacker podía adivinarla facilmente...")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                escribir("-----------------------")
                print()
                continue
            else:
                escribir(
                    "------------------------------------------------------------------")
                escribir("Información de la contraseña:")
                escribir("Contraseña: ", salto=False)
                escribir(contraseña)
                hash_contraseña = hashear(contraseña)
                id = guardar_hash(hash_contraseña)
                escribir("id: ", salto="")
                escribir(id)
                escribir("Hash: ", salto=False)
                print(hash_contraseña, end="\n\n")
                escribir("Función de Hash: bcrypt")
                escribir("Destino: 'Credenciales.txt'")
                mostrar_creditos()
                break
        elif longitud_contraseña > 9 and longitud_contraseña <= 15:
            contraseña = config_contraseña(longitud_contraseña)
            print()
            escribir("Contraseña Generada: ", salto=False)
            escribir(contraseña)
            escribir(f"Esta contraseña es segura!")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                escribir("-----------------------")
                print()
                continue
            else:
                escribir(
                    "------------------------------------------------------------------")
                escribir("Información de la contraseña:")
                escribir("Contraseña: ", salto=False)
                escribir(contraseña)
                hash_contraseña = hashear(contraseña)
                id = guardar_hash(hash_contraseña)
                escribir("id: ", salto=False)
                escribir(id)
                escribir("Hash: ", salto=False)
                print(hash_contraseña, end="\n\n")
                escribir("Función de Hash: bcrypt")
                escribir("Destino: 'Credenciales.txt'")
                mostrar_creditos()
                break
        elif longitud_contraseña > 15 and longitud_contraseña <= 40:
            contraseña = config_contraseña(longitud_contraseña)
            print()
            escribir("Contraseña Generada: ", salto=False)
            escribir(contraseña)
            escribir(f"¡Felicidades!, Esta contraseña es muy segura")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                escribir("-----------------------")
                print()
                continue
            else:
                escribir(
                    "------------------------------------------------------------------")
                escribir("Información de la contraseña:")
                escribir("Contraseña: ", salto=False)
                escribir(contraseña)
                hash_contraseña = hashear(contraseña)
                id = guardar_hash(hash_contraseña)
                escribir("id: ", salto=False)
                escribir(id)
                escribir("Hash: ", salto=False)
                print(hash_contraseña, end="\n\n")
                escribir("Función de Hash: bcrypt")
                escribir("Destino: 'Credenciales.txt'")
                mostrar_creditos()
                break
        else:
            escribir(
                "Lo siento, escribiste una longitud negativa o fuera del rango. Vuelve a intentarlo")
            continue


blackpass()
