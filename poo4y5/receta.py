from ingrediente import Ingrediente
import os

class Receta:
    OPC_AGREGAR_INGREDIENTE = 1
    OPC_CONSULTAR_INGREDIENTES = 2
    OPC_AGREGAR_PASO = 3
    OPC_CONSULTAR_PASOS = 4
    OPC_SALIR = 0

    def __init__(self, nombre=''):
        self._nombre = nombre
        self._ingredientes = []
        self._pasos = []

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
    def ingredientes(self):
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self, value):
        self._ingredientes = value

    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes

    @property
    def pasos(self):
        return self._pasos

    @pasos.setter
    def pasos(self, value):
        self._pasos = value

    @pasos.deleter
    def pasos(self):
        del self._pasos

    def __str__(self):
        s = f'                  {self.nombre}\n'
        s += 'Ingredientes: \n'
        for ingrediente in self.ingredientes:
            s += f'{ingrediente}\n'

        s += '\nPasos: \n'
        for i, paso in enumerate(self.pasos):
            i+= 1
            s += f'{i}. {paso}\n'
        return s

    def menu(self):
        continuar = True
        while continuar:
            os.system('clear')
            print(f'''                      {self.nombre}
{self.OPC_AGREGAR_INGREDIENTE}) Agregar Ingrediente
{self.OPC_CONSULTAR_INGREDIENTES}) Consultar Ingredientes
{self.OPC_AGREGAR_PASO}) Agregar Paso
{self.OPC_CONSULTAR_PASOS}) Consultar Pasos
{self.OPC_SALIR}) Salir''')
            opc = int(input('Selecciona una opción: '))
            if opc == self.OPC_AGREGAR_INGREDIENTE:
                self.agregar_ingrediente()
            elif opc == self.OPC_CONSULTAR_INGREDIENTES:
                self.consultar_ingredientes()
            elif opc == self.OPC_AGREGAR_PASO:
                self.agregar_paso()
            elif opc == self.OPC_CONSULTAR_PASOS:
                self.consultar_pasos()
            elif opc == self.OPC_SALIR:
                continuar = False
            else:
                print('Opción no válida...')

            input('Presiona enter para continuar...')
        print('Nos vemos...')
    
    def agregar_ingrediente(self):
        continuar = True
        while continuar:
            os.system('clear')
            print('                    Agregar Ingredientes')
            nombre = input('Nombre: ')
            cantidad = -1
            while cantidad <= 0:
                cantidad = input('Cantidad: ')
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0

            unidad_medida = input('Unidad de medida: ')
            ingrediente = Ingrediente(nombre, cantidad, unidad_medida)
            self.ingredientes.append(ingrediente)
            respuesta = input('¿Desea agregar otro ingrediente?(s/n): ')
            if respuesta.lower() == 'n':
                continuar = False


    def consultar_ingredientes(self):
        os.system('clear')
        print('                      Ingredientes')
        if len(self.ingredientes) == 0:
            print('no hay ingredientes registrados')
            return

        for ingrediente in self.ingredientes:
            print(f'{ingrediente}')

    def agregar_paso(self):
        continuar = True
        while continuar:
            os.system('clear')
            print('                    Agregar Ingredientes')
            paso = input('Paso: ')
            self.pasos.append(paso)
            respuesta = input('¿Desea agregar otro paso?(s/n): ')
            if respuesta.lower() == 'n':
                continuar = False 

    def consultar_pasos(self):
        os.system('clear')
        print('                      Pasos')
        if len(self.pasos) == 0:
            print('no hay pasos registrados')
            return

        for i, paso in enumerate(self.pasos):
            i += 1
            print(f'{i}. {paso}')