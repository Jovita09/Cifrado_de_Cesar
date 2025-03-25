# CIFRADOR DEL CÉSAR.

import os

def main(): #Función principal que solicita datos al usuario y ejecuta el cifrado o descifrado.
    while True:  # Bucle infinito para repetir el proceso
        message = input("Introducir Mensaje: ") # Solicitamos mensaje al usuario
        key     = int(input("Key [1-27]: ")) #Solicita clave numérica para el cifrado/descifrado (debe estar entre 1 y 26)
        mode    = input("Cifrar o Descifrar [c/d]: ").strip().lower() # Solicita modo de operación: 'c' para cifrar, 'd' para descifrar

        if mode.startswith('c'):
            mode = "cifrar"
        elif mode.startswith('d'):
            mode = "descifrar"
        else:
            print("Opción no válida. Usa 'c' para cifrar o 'd' para descifrar.")
            return  #Termina la ejecución si la opción es inválida

        #Llamar a la función de cifrado/descifrado y mostrar el resultado
        translated = encdec(message, key, mode)

        if mode == "cifrar":
            print("Mensaje Cifrado:", translated)
        elif mode == "descifrar":
            print("Mensaje Descifrado:", translated)

        # Preguntar si quiere repetir el proceso
        again = input("\n¿Quieres cifrar/descifrar otro mensaje? (s/n): ").strip().lower()
        if again != 's':  # Si el usuario no escribe 's', el programa termina
            print("Saliendo del programa...Bai Bai, :D")
            break

def encdec(message, key, mode): #Función que cifra o descifra un mensaje utilizando el Cifrado César."""
    
    message = message.upper()#Convertir el mensaje a mayúsculas para manejar solo un conjunto de caracteres
    translated = "" #Variable para almacenar el mensaje cifrado o descifrado
    letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #Definir el alfabeto permitido en el cifrado

    # Recorrer cada carácter del mensaje
    for symbol in message:
        if symbol in letters:  #Verificar si el carácter es una letra
            num = letters.find(symbol)  #Obtener el índice de la letra en el alfabeto

            # Aplicar el desplazamiento según el modo seleccionado
            if mode == "cifrar":
                num = num + key  #Desplazar hacia adelante para cifrar
            elif mode == "descifrar":
                num = num - key  #Desplazar hacia atrás para descifrar

            #Ajustar si el índice excede los límites del alfabeto
            num %= len(letters)  #Permite que las letras roten correctamente

            # Agregar el carácter cifrado/descifrado a la cadena de salida
            translated += letters[num]
        else:
            #Si el carácter no es una letra (espacio, número, símbolo), se mantiene igual
            translated += symbol
    
    return translated  #Retornar el mensaje procesado
main()

 