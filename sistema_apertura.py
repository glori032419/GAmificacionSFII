def get_codigo(file, tripulante):

    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if tripulante in directory:
            return directory[tripulante]
        else:
            return('¡El tripulante ' + tripulante + ' no existe!\n')


def add_codigo(file, tripulante, codigo):
   
    try: 
        f = open(file, 'a')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        f.write(tripulante + ',' + codigo + '\n')
        f.close()
        return('El nuevo codigo se ha añadido.\n')

def remove_codigo(file, tripulante):
   
    try: 
        f = open(file, 'r')
    except FileNotFoundError:
        return('¡El fichero ' + file + ' no existe!\n')
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(',')) for line in directory])
        if tripulante in directory:
            del directory[tripulante]
            f = open(file, 'w')
            for nombre, codigo in directory.items():
                f.write(nombre + ',' + codigo)
            f.close()
            return ('¡El tripulante se ha eliminado.!\n')
        else:
            return('¡El tripulante  ' + tripulante + ' no existe!\n')


def create_directory(file):
    
    import os
    if os.path.isfile(file):
        answer = input('El fichero ' + file + ' ya existe. ¿Desea vaciarlo (S/N)? ')
        if answer == 'N': 
            return 'No se ha creado el fichero porque ya existe.\n'
    f = open(file, 'w')
    f.close()
    return 'Se ha creado el fichero.\n'
     

def menu():
    '''
    Función que presenta un menú con las operaciones disponibles sobre un listín telefónico y devuelve la opción seleccionada por el usuario.
    Devuelve:
        La opción seleccionada por el usuario.
    '''
    print('Sistema de apertura.')
    print('============================')
    print('1 - Consultar codigo de identificacion.')
    print('2 - Añadir codigo de un sistema nuevo.')
    print('3 - Eliminar codigo de un sistema.')
    print('4 - Crear el listín')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def directory():
    '''
    Función que lanza la aplicación para la gestión del listín telefónico.
    '''
    file = 'listin.txt' 
    while True:
        option = menu()
        if option == '1':
            nombre = input('Introduce el nombre del tripulante: ')
            print(get_codigo(file, nombre))
        elif option == '2':
            nombre = input('Introduce el nombre del tripulante: ')
            codigo = input('Introduce el codigo del tripulante: ')
            print(add_codigo(file, nombre, codigo))
        elif option == '3':
            nombre = input('Introduce el nombre del tripulante: ')
            print(remove_codigo(file, nombre))
        elif option == '4':
            print(create_directory(file))
        else:
            break
    return

directory()