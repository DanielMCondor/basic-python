import json

#json.dumps() -> convertir informacion en formato json
#json.loads() -> convertir de formato json a formato python (estructura o a tipo de datos en python)
#json.load() -> permite leer informacion de un archivo
#json.dump() -> permite enviar informacion asia un archivo

entero = 33
json_entero = json.dumps(entero)
print(json_entero)
print(type(json_entero))
python_entero = json.loads(json_entero)
print(python_entero)
print(type(python_entero))
cadena = 'hola mundo'
json_cadena = json.dumps(cadena)
print(json_cadena)
python_cadena = json.loads(json_cadena)
print(python_cadena)
lista = [1,2,'tres']
json_lista = json.dumps(lista)
print(json_lista)
python_lista = json.loads(json_lista)
print(python_lista)
diccionario = {'entero':1, 'cadena':'hola', 'lista': [1,2,'tres',4.4] }
json_diccionario = json.dumps(diccionario)
print(json_diccionario)
python_diccionario = json.loads(json_diccionario)
print(python_diccionario)
#####################################################3
with open('archivo_json.json', 'w') as archivo:
    json.dump(diccionario, archivo)

with open('archivo_json.json', 'r') as archivo:
    datos = json.load(archivo)
print(datos)