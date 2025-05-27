recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Output
print("\nLista inicial de recordatorios:")
for evento in recordatorios:
    print(f"Fecha: {evento[0]}, Hora: {evento[1]}, Evento: {evento[2]}")

recordatorios.append(['2021-02-02', "06:00", "Empezar el Año"])
recordatorios.sort()

for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'
        
recordatorios = [evento for evento in recordatorios if evento[2] != '2021-05-01']
        
recordatorios.append(['2021-12-24', "22:00", "Cena Navidad"])
recordatorios.append(['2021-12-31', "22:00", "Cena Año Nuevo"])
recordatorios.sort()

print("\nLista final de recordatorios:")
for evento in recordatorios:
    print(f"Fecha: {evento[0]}, Hora: {evento[1]}, Evento: {evento[2]}")