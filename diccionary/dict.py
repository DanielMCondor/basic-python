import os

SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
MODIFICAR = 4
ELIMINAR = 5

def mostrar_menu():
    os.system('clear')
    print(f'''                         Mi Agenda
{AGREGAR}) Agregar contacto
{MOSTRAR}) Mostrar contactos
{BUSCAR}) Buscar contactos
{MODIFICAR}) Modificar contacto
{ELIMINAR}) Eliminar contacto
{SALIR}) Salir''')

def agregar_contactos(agenda):
    os.system('clear')
    print('                             Agregar contacto')
    nombre = input('Nombre: ')
    if agenda.get(nombre):
        print('ya existe el contacto')
        return
    telefono = input('Telefono: ')
    email = input('Email: ')
    agenda.setdefault(nombre, (telefono, email))
    print('Contacto agregado con éxito.')

def mostrar_contactos(agenda):
    os.system('clear')
    print('                            Mis contactos')
    if len(agenda) > 0:
        for contacto, datos in agenda.items():
            print(f'Nombre: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('~'*50)
        return
    
    print('No hay contactos registrados')

def buscar_contacto(agenda):
    os.system('clear')
    print('                           Buscar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        encontrados = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'Email: {datos[1]}')
                print('~'*50)
                encontrados += 1

        print(f'Se encontraron {encontrados} contactos. ') if encontrados > 0 else print('No se encontró el contacto.')
        return
    
    print('No hay contactos registrados')

def modificar_contacto(agenda):
    os.system('clear')
    print('                           Modificar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            datos = agenda.get(nombre)
            print('Informacion actual: ')
            print(f'Nombre: {nombre}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('*'*50)
            print('Ingresa los nuevos datos: ')
            
            telefono = input('Telefono: ')
            email = input('Email: ')
            agenda[nombre] = (telefono, email)
            print('Datos actualizados con éxito.')
        else:
            print('No existe el contacto')

        return
    
    print('No hay contactos registrados')

def eliminar_contacto(agenda):
    os.system('clear')
    print('                       Eliminar Contacto')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        if agenda.get(nombre):
            agenda.pop(nombre)
            print('contacto Eliminado con éxito.')
        else:
            print('No existe el contacto.')

        return    
    print('No hay contactos registrados')

def main():
    continuar = True
    mi_agenda = {}
    while continuar:
        mostrar_menu()
        opc = int(input('Selecciona una opción: '))

        if opc == AGREGAR:
            agregar_contactos(mi_agenda)
        elif opc == MOSTRAR:
            mostrar_contactos(mi_agenda)
        elif opc == BUSCAR:
            buscar_contacto(mi_agenda)
        elif opc == MODIFICAR:
            modificar_contacto(mi_agenda)
        elif opc == ELIMINAR:
            eliminar_contacto(mi_agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opción no válida')
        input('Presiona enter para continuar...')
    print('Nos vemos...')

if __name__ == '__main__':
    main()