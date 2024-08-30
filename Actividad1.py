def cifrado_cesar(texto, corrimiento):
    resultado = ""

    # Iterar sobre cada carácter en el texto
    for caracter in texto:
        if caracter.isalpha():  # Verifica si el carácter es una letra
            ascii_offset = 65 if caracter.isupper() else 97
            # Realiza el desplazamiento y garantiza que esté en el rango alfabético
            nuevo_caracter = chr((ord(caracter) - ascii_offset + corrimiento) % 26 + ascii_offset)
            resultado += nuevo_caracter
        else:
            # Si no es una letra, se añade sin cambios
            resultado += caracter

    return resultado

# Ejemplo de uso
texto_a_cifrar = input("Ingresa el texto a cifrar: ")
corrimiento = int(input("Ingresa el corrimiento: "))

texto_cifrado = cifrado_cesar(texto_a_cifrar, corrimiento)
print("Texto cifrado:", texto_cifrado)
