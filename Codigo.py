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