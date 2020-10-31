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
        print(separador)
        nombre=(input("Dime como quieres que se llame tu Base de Datos : "))
        nombrefinal=(nombre + ".db")
        listabase.append(nombrefinal)
        crear(nombrefinal)
        print("1=SI\n2=NO")
        opcion=int(input("Deseas seguir ejecutando el codigo creador de Base de Datos ? : "))
        print("")
    

         #Agregar tablas a la base de datos ya creada ("EL ESQUELETO ")
    elif menu ==2:
        print(separador)
        for base in listabase :
            print(f"Estas son las Base de Datos que ya estan creadas : {base} \n")
            contador=contador+1
        
        #Si tengo una base de datos ya creada con el ciclo
        if contador!=0:
            print(separador)
            agre=("CREATE TABLE IF NOT EXISTS ")
            parentesis=("(")
            parentesis2=(")")
            puntoycoma=(";")
            nombrebase=input("Dime el nombre de la Base de Datos : ")
            nombrefinal=(nombrebase +".db")
            print(separador)
            tabla=input("Dime el nombre de la Tabla a crear : ")
            print("")
            tipos(separador)
            print("")
            clave=input("Dime el nombre del atributo clave con su tipo de dato  : ")
            print(separador)
            cuantos=int(input("Dime cuantos atributos va a tener : "))
            print(separador)
            fin=(agre+tabla+parentesis+clave+" PRIMARY KEY"+",")
            
            # 1 ATRIBUTO
            if cuantos==1:
                tipos(separador)
                atributo=input("Dime el nombre del atributo y su tipo de dato que va almacenar: ")
                listaatributos.append(atributo)
                caracter="".join(listaatributos)
                final =(fin+caracter+parentesis2+puntoycoma)
                agregar(nombrefinal,final)
                print("1=SI\n2=NO")
                opcion=int(input("Deseas seguir ejecutando el codigo creador de Base de Datos ? : "))
                print("")
                
            # MAS DE 1 ATRIBUTO
            elif cuantos>1:
                tipos(separador)
                print("")
            
                for x in range(1,cuantos+1):
                    if x != cuantos:
                        atributo=input("Dime el nombre del atributo y su tipo de dato que va almacenar y al final pon una coma  : ")
                        listaatributos.append(atributo)
            
                    else:
                        print(separador)
                        atributo=input("Dime el nombre del atributo y su tipo de dato que va almacenar sin coma al final :)  : ")
                        listaatributos.append(atributo)

                caracter="".join(listaatributos)
                final =(fin+caracter+parentesis2+puntoycoma)
                agregar(nombrefinal,final)
                print("1=SI\n2=NO")
                opcion=int(input("Deseas seguir ejecutando el codigo creador de Base de Datos ? : "))
                print("")
         
          #Si no tengo una base de datos creada por el cicio
        elif contador==0:
            print("No has registrado ninguna Base de Datos en el Ciclo :(")
            print("Ingresa bien el nombre de la base de datos porque si no lo ingresas bien te va a crear una nueva con el nombre que le des :)")
            
            print(separador)
            agre=("CREATE TABLE IF NOT EXISTS ")
            parentesis=("(")
            parentesis2=(")")
            puntoycoma=(";")
            nombrebase=input("Dime el nombre de la Base de Datos : ")
            nombrefinal=(nombrebase+".db")
            print(separador)
            tabla=input("Dime el nombre de la Tabla a crear : ")
            print("")
            tipos(separador)
            print("")
            clave=input("Dime el nombre del atributo clave con su tipo de dato  : ")
            print(separador)
            cuantos=int(input("Dime cuantos atributos va a tener : "))
            print(separador)
            fin=(agre+tabla+parentesis+clave+" PRIMARY KEY"+",")
          
            # 1 ATRIBUTO
            if cuantos==1:
                print("")
                tipos(separador)
                print("")
                atributo=input("Dime el nombre del atributo y su tipo de dato que va almacenar: ")
                listaatributos.append(atributo)
                caracter="".join(listaatributos)
                final =(fin+caracter+parentesis2+puntoycoma)
                agregar(nombrefinal,final)
                print("1=SI\n2=NO")
                opcion=int(input("Deseas seguir ejecutando el codigo creador de Base de Datos ? : "))
                print("")
            
            # MAS DE 1 ATRIBUTO
            elif cuantos>1:
                print("")
                tipos(separador)
                print("")
            
                for x in range(1,cuantos+1):
                    if x != cuantos:
                        atributo=input("Dime el nombre del atributo y su tipo de dato que va almacenar y al final pon una coma  : ")
                        listaatributos.append(atributo)
            
                    else:
                        print(separador)
                        atributo=input("Dime el nombre del atributo y su tipo de dato que va almacenar sin coma al final :)  : ")
                        listaatributos.append(atributo)

                caracter="".join(listaatributos)
                final =(fin+caracter+parentesis2+puntoycoma)
                agregar(nombrefinal,final)
                print("1=SI\n2=NO")
                opcion=int(input("Deseas seguir ejecutando el codigo creador de Base de Datos ? : "))
                print("")
                
    elif menu == 3:
        listadatos=[]
        contador10=1
        contador11=0
        listatipo=[]
        print(separador)
        nombrebase=input("Dime el nombre de la Base de Datos : ")
        nombrebase1=(nombrebase+".db")
        print(separador)
        tabla=input("Dime el nombre de la Tabla : ")
        print(separador)
        cuantos=int(input("Cuantos atributos tienes en esta tabla :"))
        print(separador)
        tipos(separador)

        for x in range(cuantos):
            dato=input(f"Dime el nombre del atributo {contador10} : ")
            contador10=contador10+1
            print(separador)
            listadatos.append(dato)

        for x in range (cuantos):
            tipo=input(f"Dime que tipo de dato es, el atributo {listadatos[contador11]} de esta tabla : ")
            contador2=contador2+1
            contador11=contador11+1
            print(separador)
            listatipo.append(tipo)

        registros=int(input("Cuantos registros quieres resgistrar : "))
        print(separador)
        print("")
        print("-"*30 + "Bienvenido a los Registros :)" + "-"*30)
        insertar(nombrebase1,tabla,cuantos,contador3,separador,listatipo,registros,listadatos)
        
        print("1=SI\n2=NO")
        opcion=int(input("Deseas seguir ejecutando el codigo creador de Base de Datos ? : "))
        print("")
    

