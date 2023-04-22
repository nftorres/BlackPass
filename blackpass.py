from funciones import *

def blackpass():
    output("---------------------------BlackPass V1-Español---------------------------")
    output("Generador de contraseñas :)")
    while True:
        longitud_contraseña = int(input("Longitud de la contraseña: "))
        if longitud_contraseña > 0 and longitud_contraseña < 4:
            config_contraseña(longitud_contraseña)
            output(f"Esta contraseña es mala porque sólo contiene {longitud_contraseña} caracteres...")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                continue
            else:
                footer()
                break
        elif longitud_contraseña >= 4 and longitud_contraseña <= 9:
            config_contraseña(longitud_contraseña)
            output(f"Esta contraseña es insegura, un hacker podía adivinarla facilmente...")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                continue
            else:
                footer()
                break
        elif longitud_contraseña > 9 and longitud_contraseña <= 15:
            config_contraseña(longitud_contraseña)
            output(f"Esta contraseña es segura!")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                continue
            else:
                footer()
                break
        elif longitud_contraseña > 15 and longitud_contraseña <= 40:
            config_contraseña(longitud_contraseña)
            output(f"¡Felicidades!, Esta contraseña es muy segura")
            cambiar = input("¿Quieres generar otra?: ")
            if 'si' in cambiar.lower():
                continue
            else:
                footer()
                break
        else: 
            output("Lo siento, escribiste una longitud negativa o fuera del rango. Vuelve a intentarlo")
            continue
blackpass()