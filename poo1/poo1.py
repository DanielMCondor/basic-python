class Figura:
    def __init__(self):
        self._lados = None

    @property
    def lados(self):
        return self._lados

    @lados.setter
    def lados(self, value):
        if value < 3:
            self._lados = None
            return

        self._lados = value

    @lados.deleter
    def lados(self):
        del self._lados

def main():
    triangulo = Figura()
    cuadrado = Figura()

    triangulo.lados = -3
    cuadrado.lados = 4
    # del cuadrado.lados -> cuando se requiera eliminar un atributo

    print('el triangulo tiene {} lados.'.format(triangulo.lados))
    print('el cuadrado tiene {} lados.'.format(cuadrado.lados))

if __name__ == '__main__':
    main()
