import sys
import sqlite3
from sqlite3 import Error
from plyer import notification


def tipos(separador):
    print(separador)
    print("Tipos de Datos: ")
    print("*text=tipo texto\n*integer=tipo numerico\n*not null = no permite valores vacios")
    print("-"*15)
    print("EJEMPLOS: ")
    print("matricula integer")
    print("nombre text")
    print("telefono integer not null ")
    print("apellido_paterno text not null")
    print(separador)


# Funcion de insertar 
def insertar(nombrebase1,tabla,cuantos,contador3,separador,listatipo,registros,listadatos):
    try:
        with sqlite3.connect(nombrebase1) as conn:
            cursor_mini = conn.cursor()
            cadena1=("INSERT INTO ")
            cadena2=(" values ")
            cadena3=("(")
            cadena4=(")")
            fin=(cadena1+tabla+cadena2+cadena3)
                
            contador6=0
            contador7=1
            while registros!=contador6:
                listainsertar=[]
                print("")
                print("-"*20+f"REGISTRO{contador7}:"+"-"*20)
                contador3=0
                contador5=1
                for elemento in listatipo:
                    if cuantos!=contador5:
                        if elemento=="text":
                            valor=input(f"Dime el valor de {listadatos[contador3]} en esta tabla : ")
                            print(separador)
                            valorfin=("'"+valor+"'"+",")
                            listainsertar.append(valorfin)
                            contador3=contador3+1
                            contador5=contador5+1
                            
                        elif elemento=="integer":
                            valor=input(f"Dime el valor de {listadatos[contador3]} en esta tabla : ")
                            print(separador)
                            listainsertar.append(valor+",")
                            contador3=contador3+1
                            contador5=contador5+1
                        
                    elif elemento==listatipo[-1]:
                        if elemento=="text":
                            valor=input(f"Dime el valor de {listadatos[contador3]} en esta tabla : ")
                            print(separador)
                            valorfin=("'"+valor+"'")
                            listainsertar.append(valorfin)
                            contador3=contador3+1
                            contador5=contador5+1
                            contador6=contador6+1
                            contador7=contador7+1
                            caracter="".join(listainsertar)
                            final =(fin+caracter+cadena4)
                            cursor_mini.execute(final)
                            
                        elif elemento=="integer":
                            valor=input(f"Dime el valor de {listadatos[contador3]} en esta tabla : ")
                            print(separador)
                            listainsertar.append(valor)
                            contador3=contador3+1
                            contador5=contador5+1
                            contador6=contador6+1
                            contador7=contador7+1
                            caracter="".join(listainsertar)
                            final =(fin+caracter+cadena4)
                            cursor_mini.execute(final)
            
            notification.notify(
            title="NOTIFICACION",
            message = "Ya se registraron los registros  :) ",
            timeout=15,
            )
            
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")


# Funcion de crear Base de Datos
def crear(nombrefinal):
    try:
        with sqlite3.connect(nombrefinal) as conn:
            print("-"*20)
            print("Ya esta creada tu base de datos : ) ")
            print("-"*20)
            notification.notify(
            title="NOTIFICACION",
            message = "Ya esta creada tu base de datos :) ",
            timeout=15,
            )
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")


# Funcion de agregar tablas al principio 
def agregar(nombrefinal,final):
    try:
        with sqlite3.connect(nombrefinal) as conn:
            cursor_mini = conn.cursor()
            cursor_mini.execute(final)
            print("-"*20)
            print("Se agregaron las tablas exitosamente ")
            print("-"*20)
            notification.notify(
            title="NOTIFICACION",
            message = "Se agregaron las tablas exitosamente :) ",
            timeout=15,
            )
            
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")