recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]


recordatorios.append(['2021-02-02', "06:00", "Empezar el Año"])  # Se agrega nuevo recordatorio a la lista

for evento in recordatorios:                # Bucle para buscar y modificar la fecha
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'
        

recordatorios = [x for x in recordatorios if x[0] != '2021-05-01']  # Crea una lista sin el elemento que coincida
        
        
recordatorios.append(['2021-12-24', "22:00", "Cena Navidad"])       # Se agregan nuevos eventos al calendario
recordatorios.append(['2021-12-31', "22:00", "Cena Año Nuevo"])
recordatorios.sort()                     # Se reordena lista en orden ascendente

print("\nLista final de recordatorios:")      # Bucle para imprimir en orden         
for evento in recordatorios:
    print(f"Fecha: {evento[0]}, Hora: {evento[1]}, Evento: {evento[2]}")