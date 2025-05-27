import sys

def validar_argumentos():  
    if len(sys.argv) != 5:
        print("Error: Debe ingresar 4 argumentos")
        print("Uso: python conversiones.py [sol] [peso_arg] [dolar] [Monto_peso_chileno]")
        sys.exit(1)
        
def conversion_monedas(monto, tasas):
    conversiones = {
        "soles": monto * tasas["sol"],
        "peso_arg": monto * tasas["peso_arg"],
        "dolar": monto * tasas["dolar"]
    }
    return conversiones

def ingreso_tasas_monto():
    validar_argumentos()
    try:
        tasas = {
            "sol": float(sys.argv[1]),
            "peso_arg": float(sys.argv[2]),
            "dolar": float(sys.argv[3])
        }
        monto_clp = float(sys.argv[4])
        resultado = conversion_monedas(monto_clp, tasas)
        print(f"Los {monto_clp:.0f} pesos equivalen a:")
        print(f"{resultado['soles']:.1f} Soles")
        print(f"{resultado['peso_arg']:.1f} Pesos Argentinos")
        print(f"{resultado['dolar']:.1f} Dólares")
    except ValueError:
        print("Error: Todos los argumentos deben ser números")
        sys.exit(1)

if __name__ == "__main__":
    ingreso_tasas_monto()