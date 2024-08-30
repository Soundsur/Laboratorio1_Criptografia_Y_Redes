import os
import sys
from scapy.all import IP, ICMP, sr1

def cifrado_cesar(texto, corrimiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            nuevo_caracter = chr((ord(caracter) - ascii_offset + corrimiento) % 26 + ascii_offset)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado

def enviar_ping(mensaje, destino):
    for caracter in mensaje:
        paquete = IP(dst=destino) / ICMP() / caracter
        respuesta = sr1(paquete, timeout=1, verbose=0)
        if respuesta:
            print("Sent 1 packets.")
        else:
            print("No response received.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Uso: {sys.argv[0]} <destino> <mensaje> <corrimiento>")
        sys.exit(1)

    destino = sys.argv[1]
    mensaje = sys.argv[2]
    corrimiento = int(sys.argv[3])

    # Cifrar el mensaje
    mensaje_cifrado = cifrado_cesar(mensaje, corrimiento)

    # Enviar el mensaje cifrado
    enviar_ping(mensaje_cifrado, destino)