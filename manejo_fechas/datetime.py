from datetime import datetime, timedelta, date

fecha_actual = datetime.now()
print(fecha_actual)

fecha = datetime(2020,11,5)
print(fecha)

fecha_hora = datetime(2022,12,6,15,38,1)
print(fecha_hora)

fecha_actual2 = datetime.strftime(fecha_actual, '%d/%m/%Y %H:%M:%S')
print(fecha_actual2)

fecha_actual3 = datetime.strftime(fecha_actual, '%b %d %Y %I:%M:%S %p')
print(fecha_actual3)

# https://strftime.org/

fecha_text = 'Dec 06 2020 12:56:11'
fecha_actual4 = datetime.strptime(fecha_text, '%b %d %Y %H:%M:%S')
print(fecha_actual4)

dia6 = datetime.strftime(fecha_actual4, '%-d')
dia06 = datetime.strftime(fecha_actual4, '%d')
print(dia6)
print(dia06)

hora_actual = datetime.strftime(fecha_actual, '%I:%M:%S %p')
print(hora_actual)

fecha_pasada = datetime(2022, 5, 12)
diferencia = fecha_actual - fecha_pasada

print(diferencia)
print(diferencia.days)
print(diferencia.total_seconds())

print("######################")
# dia_delta = timedelta(days=5) #Suma fechas
dia_delta = timedelta(days=-5) #Resta fechas
fecha_inicial = date.today()
print(fecha_inicial)
fecha_futura = fecha_inicial + dia_delta
print(fecha_futura)

print("###################################")
fecha_iso = datetime.now().isoformat()
print(fecha_iso)