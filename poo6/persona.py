class Persona:
    def __init__(self, nombre='', edad=None):
        self._nombre = nombre
        self._edad = edad

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

    def __str__(self):
        return f'''Nombre: {self.nombre}
Edad: {self.edad}'''