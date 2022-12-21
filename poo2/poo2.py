class Persona:
    def __init__(self):
        self._nombre = None
        self._edad = None

    # declare metodos de interfaz
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @nombre.deleter
    def nombre(self):
        del self.nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, value):
        self._edad = value

    @edad.deleter
    def edad(self):
        del self._edad

    # declare comportamientos de la persona
    def hablar(self, mensaje):
        print(f'{self.nombre}: {mensaje}')

    def comer(self, alimento):
        print(f'{self.nombre} está comiendo {alimento}')

def main():
    persona_1 = Persona()
    persona_2 = Persona()

    persona_1.nombre = 'Alberto'
    persona_1.edad = 25

    persona_2.nombre = 'Steven'
    persona_2.edad = 21

    print('Datos de la primera persona')
    print(f'Nombre: {persona_1.nombre}')
    print(f'Edad: {persona_1.edad}')
    
    print('############################')
    
    print('Datos de la segunda persona')
    print(f'Nombre: {persona_2.nombre}')
    print(f'Edad: {persona_2.edad}')
    print('\n')
    persona_1.hablar(f'Hola {persona_2.nombre} ¿Como estas?')
    print('----------------------------------------------')
    persona_2.hablar(f'Hey {persona_1.nombre} ¡Que gusto de verte! :D')
    print('\n')
    persona_1.comer('arroz con pato')
    print('----------------------------------------------')
    persona_2.comer('ceviche')
    

if __name__ == '__main__':
    main()