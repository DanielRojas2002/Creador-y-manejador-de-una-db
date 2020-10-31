def tipos(separador):
    print(separador)
    print("Tipos de Datos: ")
    print("*text\n*integer")
    print(separador)


# Funcion de insertar 
def insertar(nombrebase1,tabla,cuantos,contador3,separador,listatipo,registros):
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
                contador3=1
                contador5=1
                for elemento in listatipo:
                    if cuantos!=contador5:
                        if elemento=="text":
                            valor=input(f"Dime el valor {contador3} de esta tabla : ")
                            print(separador)
                            valorfin=("'"+valor+"'"+",")
                            listainsertar.append(valorfin)
                            contador3=contador3+1
                            contador5=contador5+1
                            
                        elif elemento=="integer":
                            valor=input(f"Dime el valor {contador3} de esta tabla  : ")
                            print(separador)
                            listainsertar.append(valor+",")
                            contador3=contador3+1
                            contador5=contador5+1
                        
                    elif elemento==listatipo[-1]:
                        if elemento=="text":
                            valor=input(f"Dime el valor {contador3} de esta tabla  : ")
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
                            valor=input(f"Dime el valor {contador3} de esta tabla  : ")
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
            message = "Ya se registraron los resgistros  :) ",
            timeout=15,
            )
            
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")