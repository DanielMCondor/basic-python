#funciones de orden superior (programacion funcional)

edades = [12, 11, 24, 36, 8, 6, 10, 41, 32, 58, 14, 50, 7]

def mayor_edad(edad):
    return edad >= 18

list_mayores_edad = list(filter(mayor_edad, edades))
print(list_mayores_edad)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{0} tiene {1} años.".format(self.nombre, self.edad)

personas = [
    Persona("Alberto", 30),
    Persona("Juan", 20),
    Persona("Mario", 35),
    Persona("Maria", 23),
    Persona("Daniel", 50),
    Persona("Diana", 40),
]

list_personas_mayores_edad = list(filter(lambda persona: persona.edad >= 18, personas))

for persona in list_personas_mayores_edad:
    print(persona) 