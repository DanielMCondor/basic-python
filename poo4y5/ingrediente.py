class Ingrediente:
    def __init__(self, nombre='', cantidad=None, unidad_medida=''):
        self._nombre = nombre
        self._cantidad = cantidad
        self._unidad_medida = unidad_medida

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    @cantidad.deleter
    def cantidad(self):
        del self._cantidad

    @property
    def unidad_medida(self):
        return self._unidad_medida

    @unidad_medida.setter
    def unidad_medida(self, value):
        self._unidad_medida = value

    @unidad_medida.deleter
    def unidad_medida(self):
        del self._unidad_medida

    def __str__(self):
        return f'''Nombre: {self.nombre}
Cantidad: {self.cantidad} {self.unidad_medida}'''