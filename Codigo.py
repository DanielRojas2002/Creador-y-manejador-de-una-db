import sys
import sqlite3
from sqlite3 import Error
from plyer import notification

from funciones import tipos
from funciones import insertar
from funciones import crear
from funciones import agregar

contador2=1
contador3=1
separador=("*"*40)
opcion=1
listaatributos=[]
listabase=[]
contador=0

#Menu principal
while opcion==1:
    print(separador + "Bienvenido al creador de Base de Datos :)"+ separador)
    print("-"*20+"MENU PRINCIPAL"+"-"*20)
    print("")
    print("1=Quiero crear una base de datos nueva\n2=Quiero agregar tablas a mi Base de Datos \n3=Quiero agregarle registros a mi Base de Datos ")
    menu=int(input("Que opcion eliges : "))

    # Crear base de datos        
    if menu==1:
        nombre=(input("Dime como quieres que se llame tu Base de Datos : "))
        nombrefinal=(nombre + ".db")
        listabase.append(nombrefinal)
        crear(nombrefinal)
        print("1=SI\n2=NO")
        opcion=int(input("Deseas seguir ejecutando el codigo creador de Base de Datos ? : "))