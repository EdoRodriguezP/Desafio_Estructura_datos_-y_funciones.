import sys

def validar_argumentos():       # Funcion para validar ingreso de 4 argumentos sino imprime y cierra programa
    if len(sys.argv) != 5:
        print("Error: Debe ingresar 4 argumentos")
        print("Uso: python conversiones.py [sol] [peso_arg] [dolar] [Monto_peso_chileno]")
        sys.exit(1)         # Termina con codigo de error.
        
def conversion_monedas(monto, tasas):     # Funcion para la conversion de monedas
    conversiones = {                      # Diccionario con las conversiones multiplica el monto por cada tasa
        "soles": monto * tasas["sol"],
        "peso_arg": monto * tasas["peso_arg"],
        "dolar": monto * tasas["dolar"]
    }
    return conversiones            # Retorna Diccionario conversiones con calculos ya realizados.

def ingreso_tasas_monto():   # Funcion para ingreso y muestra de resultados
    validar_argumentos()     # Se verifican argumentos
    try:
        tasas = {                # Convierte los argumentos a números flotantes y los almacena en un diccionario
            "sol": float(sys.argv[1]),
            "peso_arg": float(sys.argv[2]),
            "dolar": float(sys.argv[3])
        }
        monto_clp = float(sys.argv[4])    # Convierte monto a flotante
        
        resultado = conversion_monedas(monto_clp, tasas) # Llama a la variable conversion y la guarda en resultados
        
        print(f"Los {monto_clp:.0f} pesos equivalen a:")   # Imprime los resultados
        print(f"{resultado['soles']:.1f} Soles")
        print(f"{resultado['peso_arg']:.1f} Pesos Argentinos")
        print(f"{resultado['dolar']:.1f} Dólares")
        
    except ValueError:        # Maneja error si los argumentos no son numeros validos
        print("Error: Todos los argumentos deben ser números")
        sys.exit(1)

if __name__ == "__main__":    # Para que este código solo se ejecute cuando el script es el programa principal
    ingreso_tasas_monto()     # Llama a la función para ejecutar