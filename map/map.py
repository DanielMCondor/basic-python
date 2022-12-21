


def elevar_cuadrado(num):
    #return num * num
    return pow(num, 2)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11)) #1 al 10
numero_elevados = list(map(elevar_cuadrado, numeros))
# print(numero_elevados)

mi_dict = {'name': 'prueba', 'result': [1,2,3,5]}
result = list((filter(None , mi_dict['result'])))
# print(result)

dicts = [
    { "name": "Tom", "age": 10 },
    { "name": "Mark", "age": 5 },
    { "name": "Pam", "age": 7 },
    { "name": "Dick", "age": 12 }
]

response = next(item for item in dicts if item["name"] == "Pam")
# print(response)
response1 = next((item for item in dicts if item["name"] == "Pam"), None)
# print(response1)
response2 = next((i for i, item in enumerate(dicts) if item["name"] == "Pam"), None)
# print(response2)

people = [
{'name': "Tom", 'age': 10},
{'name': "Mark", 'age': 5},
{'name': "Pam", 'age': 7}
]

response = list(filter(lambda person: person['name'] == 'Pam', people))
# print(response)


mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)
