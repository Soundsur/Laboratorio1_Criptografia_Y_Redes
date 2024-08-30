from scapy.all import rdpcap, ICMP
from termcolor import colored

def descifrado_cesar(texto, corrimiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            nuevo_caracter = chr((ord(caracter) - ascii_offset - corrimiento) % 26 + ascii_offset)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado

def obtener_mensaje_cifrado(pcap_file):
    paquetes = rdpcap(pcap_file)
    mensaje_cifrado = ""
    
    for paquete in paquetes:
        if ICMP in paquete and paquete[ICMP].type == 8:  # ICMP echo request (type 8)
            carga_util = str(paquete[ICMP].load, 'utf-8', errors='ignore')
            mensaje_cifrado += carga_util
    
    return mensaje_cifrado

def es_mensaje_probable(mensaje):
    palabras_comunes = ["the", "and", "el", "la", "que", "de", "y", "en"]
    for palabra in palabras_comunes:
        if palabra in mensaje.lower():
            return True
    return False

def probar_todas_las_combinaciones(mensaje_cifrado):
    for corrimiento in range(26):
        mensaje_descifrado = descifrado_cesar(mensaje_cifrado, corrimiento)
        if es_mensaje_probable(mensaje_descifrado):
            print(colored(f"Corrimiento {corrimiento}: {mensaje_descifrado}", "green"))
        else:
            print(f"Corrimiento {corrimiento}: {mensaje_descifrado}")

if __name__ == "__main__":
    archivo_pcap = "ACT3_ICMP_1111.pcapng"  # Cambia esto por la ruta de tu archivo .pcapng
    mensaje_cifrado = obtener_mensaje_cifrado(archivo_pcap)
    
    print("Probando todas las combinaciones de corrimiento:")
    probar_todas_las_combinaciones(mensaje_cifrado)
