from persona import Persona
from deportista import Deportista

def main():
    persona_1 = Persona('Hector Tuga', 44)
    deportista = Deportista('Pepe Nava', 33, 'Natación')

    print(f'''Datos de la persona:
{persona_1}''')
    print('-'*30)
    print(f'''Datos del deportista:
{deportista}''')

    deportista.entrenar()
    deportista.hablar('Listo para ganar una medalla.')

if __name__ == '__main__':
    main()