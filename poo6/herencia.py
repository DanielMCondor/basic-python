from estudiante import Estudiante

def main():
    nombre = input('Nombre del estudiante: ')
    edad = input('Edad del estudiante: ')
    promedio = float(input('Promedio: '))
    codigo = input('Codigo: ')

    estudiante = Estudiante(nombre, edad, promedio, codigo)
    print(f'''Los datos del estudiante son:
{estudiante}''')
    print('-'*30)
    estudiante.estudiar('matematicas')
    estudiante.estudiar('Ingles')

if __name__ == '__main__':
    main()