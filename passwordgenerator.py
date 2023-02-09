# imports

""""
Falta:
Hacer funcion para generar letras, numeros, signos
Anadir mayusculas a la lista letters
Hacer que se llamen aleatoriamente las funciones de letras, numeros y signos aleatorios
Crearle una interfaz grafica
"""

import random
import os

letters = ['a','b','c','d','e','f','g','h','i','j','k','m','n','l','o','p','q','r','s','t','u','v','w','x','y','z']

def randLetter():
    pos = random.randint(1,25)
    return letters[pos]

password = []

def generate_password(opc, cant):

    # Si nos introduce una cantidad par
    if cant % 2 == 0:

        # elige solo letras
        if opc == 1:
            for i in range(1, cant+1):
                i = randLetter()
                password.append(i)

        # elige letras y numeros
        elif opc == 2:
            for i in range(1, int( ( cant / 2) + 1 ) ):
                i = randLetter()
                password.append(i)
                rn = random.randint(1, 9)
                password.append(str(rn))

    # Si nos introduce una cantidad impar
    elif cant % 2 == 1:

        # elige solo letras
        if opc == 1:
            for i in range(1, cant + 1):
                i = randLetter()
                password.append(i)

        # elige letras y numeros
        elif opc == 2:
            for i in range(1, int( ((cant + 1) / 2) + 1 ) ):
                i = randLetter()
                password.append(i)
                rn = random.randint(1, 9)
                password.append(str(rn))

            del(password[-1])




while True:
    # Limpieza de consola
    os.system('cls' if os.name == 'nt' else 'clear')

    print("||Bienvenido al generador de contraseñas||")
    print(
        """
        1 - Generar contraseña 
        2 - Salir                                               
        """
    )
    o = int(input("Digite la opcion que desea: "))


    if o == 1:
        # Limpieza de consola
        os.system('cls' if os.name == 'nt' else 'clear')

        # pedir opc
        print("||Seleccione el nivel de seguridad que desea||")
        print(
            """
            1 - Generar contraseña con letras (Fragil)
            2 - Generar contraseña con letras y numeros (normal)
            """
        )
        opc = int(input("Digite la opcion que desea: "))

        # Limpieza de consola
        os.system('cls' if os.name == 'nt' else 'clear')

        # pedir cantidad de caracteres
        print("||Cantidad de caracteres||")
        print(" Fragil[1-7]  Normal[8-12]  Fuerte[13-24]")
        cant = int(input("Digite la cantidad de caracteres que desea: "))

        # generar contrasena
        generate_password(opc, cant)
        p = ''.join(password)

        # mostrar la contrasena a el usuario
        print(f"Tu contraseña de {cant} caracteres es: {p}")
        # hacer una pausa
        input("Digite una tecla para continuar")

        # resetear contrasena
        password.clear()

    else:
        # Limpieza de consola
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Saliendo....")
        break