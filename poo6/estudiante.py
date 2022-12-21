from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre='', edad=None, promedio=None, codigo=''):
        super().__init__(nombre, edad)
        self._promedio = promedio
        self._codigo = codigo

    @property
    def promedio(self):
        return self._promedio

    @promedio.setter
    def promedio(self, value):
        if self._promedio == 0.00:
            self._promedio = None
            return        
        self._promedio = value

    @promedio.deleter
    def promedio(self):
        del self._promedio

    @property
    def codigo(self):
        return self._codigo
        
    @codigo.setter
    def codigo(self, value):
        self._codigo = value
        
    @codigo.deleter
    def codigo(self):
        del self._codigo

    def estudiar(self, materia):
        print(f'{self.nombre} se encuentra estudiando {materia}')

    def __str__(self):
        return f'''{super().__str__()}
Promedio: {self.promedio}
Codigo: {self.codigo}'''