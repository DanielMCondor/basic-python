import json

class Libro:
    def __init__(self, isbn='',titulo='',autor=''):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor

    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @isbn.deleter
    def isbn(self):
        del self._isbn
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @titulo.deleter
    def titulo(self):
        del self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, value):
        self._autor = value

    @autor.deleter
    def autor(self):
        del self._autor

    def __str__(self):
        ESPACIOS = 8
        return f'''{"isbn: " : <{ESPACIOS}}{self.isbn}
{"Título: " : <{ESPACIOS}}{self.titulo}
{"Autor: " : <{ESPACIOS}}{self.autor}'''


class Libro_Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Libro):
            return {'isbn':obj.isbn, 'titulo':obj.titulo, 'autor':obj.autor}
        return json.JSONEncoder.default(self, obj)

def desde_json(diccionario):
    return Libro(diccionario['isbn'], diccionario['titulo'], diccionario['autor'])