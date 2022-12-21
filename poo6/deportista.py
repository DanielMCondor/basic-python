from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre='', edad=None, deporte=''):
        super().__init__(nombre, edad)
        self._deporte = deporte

    @property
    def deporte(self):
        return self._deporte
    
    @deporte.setter
    def deporte(self, value):
        self._deporte = value

    @deporte.deleter
    def deporte(self):
        del self._deporte

    def entrenar(self):
        print(f'{self.nombre} está entrenando {self.deporte}')

    def __str__(self):
        return f'''{super().__str__()}
Deporte: {self.deporte}'''