import sys

def validar_argumento ():                 #  Funcion para validar argumentos
    if len(sys.argv) != 2:                # Se revisa que sean 2 argumentos ingresados de lo contrario imprime y cierra el programa
        print("\nError: Se debe ingresar 2 argumentos")
        print("Uso: python word_county.py [archivo]\n")
        sys.exit(1)
    return sys.argv[1]                      # Retorna nombre de archivo que se ingreso como argumento


def contar_palabras_letras (archivo):   # Funcion para contar letras y palabras del texto
    with open(archivo, "r") as f:       # Archivo en modo lectura
        texto = f.read()                # Se lee contenido como string

    palabras_distintas = set(texto.split())  # Se separa el texto en palabras y se crea variable para guardar las distintas
    letras_distintas = set(texto)           # Se crea variable de letras distintas
        
    print(f"\nEl número de palabras distintos es: {len(palabras_distintas)}")     # Imprime las cantidades de palabras y letras.
    print(f"El número de caracteres distintos es: {len(letras_distintas)}\n")
        

if __name__ == "__main__":          # Para que este código solo se ejecute cuando el script es el programa principal
    archivo = validar_argumento()   # Llama a la función para validar y obtener el nombre del archivo
    contar_palabras_letras(archivo)  # Llama a la función para contar palabras y letras distintas en el archivo