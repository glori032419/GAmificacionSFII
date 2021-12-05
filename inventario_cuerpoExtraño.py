from os.path import exists

""" Debemos desarrollar un programa que contenga una funcion que pida un numero 
entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese numero
donde n es el numero introducido, y la muestre por pantalla. Si el fichero no existe
debe mostrar un mensaje por pantalla informando de ello.
"""

def read_table_multiplicar():
    n=int(input("Introduzca un numero entero entre 1 y 10: "))# introducimos un numero int entre 1 al 10
    file_name="tabla-n" + str(n) + ".txt"  #creamos txt

    try:
        f=open(file_name,"r")
    except FileNotFoundError:
        print("No existe el fichero con la tabla del: ",n)#le damos este mensaje si el archivo no existe
    else:
        print(f.read())#leemos el archivo existente

read_table_multiplicar()