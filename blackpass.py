from funciones import *

def blackpass():
    output("---------------------------BlackPass V1-Español---------------------------")
    output("Generador de contraseñas :)")
    while True:
        longitud_contraseña = int(input("Longitud de la contraseña: "))
        if longitud_contraseña > 0 and longitud_contraseña < 4:
            password = config_contraseña(longitud_contraseña)
            print()
            output("Contraseña Generada: ", salto="")
            output(password)
            output(f"Esta contraseña es mala porque sólo contiene {longitud_contraseña} caracteres...")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                output("-----------------------")
                print()
                continue
            else:
                output("------------------------------------------------------------------")
                output("Información de la contraseña:")
                output("Contraseña: ", salto="")
                output(password)
                password_hash = hashear(password)
                id = guardar_hash(password_hash)
                output("id: ", salto="")
                output(id)
                output("Hash: ", salto="")
                print(password_hash,end="\n\n")
                output("Función de Hash: bcrypt")
                output("Destino: 'Credenciales.txt'")
                footer()
                break
        elif longitud_contraseña >= 4 and longitud_contraseña <= 9:
            password = config_contraseña(longitud_contraseña)
            print()
            output("Contraseña Generada: ", salto="")
            output(password)
            output(f"Esta contraseña es insegura, un hacker podía adivinarla facilmente...")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                output("-----------------------")
                print()
                continue
            else:
                output("------------------------------------------------------------------")
                output("Información de la contraseña:")
                output("Contraseña: ", salto="")
                output(password)
                password_hash = hashear(password)
                id = guardar_hash(password_hash)
                output("id: ", salto="")
                output(id)
                output("Hash: ", salto="")
                print(password_hash,end="\n\n")
                output("Función de Hash: bcrypt")
                output("Destino: 'Credenciales.txt'")
                footer()
                break
        elif longitud_contraseña > 9 and longitud_contraseña <= 15:
            password = config_contraseña(longitud_contraseña)
            print()
            output("Contraseña Generada: ", salto="")
            output(password)
            output(f"Esta contraseña es segura!")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                output("-----------------------")
                print()
                continue
            else:
                output("------------------------------------------------------------------")
                output("Información de la contraseña:")
                output("Contraseña: ", salto="")
                output(password)
                password_hash = hashear(password)
                id = guardar_hash(password_hash)
                output("id: ", salto="")
                output(id)
                output("Hash: ", salto="")
                print(password_hash,end="\n\n")
                output("Función de Hash: bcrypt")
                output("Destino: 'Credenciales.txt'")
                footer()
                break
        elif longitud_contraseña > 15 and longitud_contraseña <= 40:
            password = config_contraseña(longitud_contraseña)
            print()
            output("Contraseña Generada: ", salto="")
            output(password)
            output(f"¡Felicidades!, Esta contraseña es muy segura")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                output("-----------------------")
                print()
                continue
            else:
                output("------------------------------------------------------------------")
                output("Información de la contraseña:")
                output("Contraseña: ", salto="")
                output(password)
                password_hash = hashear(password)
                id = guardar_hash(password_hash)
                output("id: ", salto="")
                output(id)
                output("Hash: ", salto="")
                print(password_hash,end="\n\n")
                output("Función de Hash: bcrypt")
                output("Destino: 'Credenciales.txt'")
                footer()
                break
        else: 
            output("Lo siento, escribiste una longitud negativa o fuera del rango. Vuelve a intentarlo")
            continue
blackpass()