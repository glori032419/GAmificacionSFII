""" desarrollar un programa que contenga una funcion
que pida un numero entero entre 1 y 10 y guarde en un fichero con el nombre 
tabla-n.txt a tabla de multiplicar de ese numero, donde n es el numero
introducido. """

def table_mulplicar():
    n=int(input("Introduzca un numero entero entre 1 y 10: "))#Usamos un input int para introdicir un numero de 1 al 10

    file_name="tabla-n" + str(n) + '.txt' #creamos el archivo txt.
    f=open(file_name,"w") 

    for i in range(1,11):
        f.write(str(n) + 'x' + str(i) + "=" + str(n*i) + "\n") #rango (1,11) n*1 
    f.close()

table_mulplicar()
