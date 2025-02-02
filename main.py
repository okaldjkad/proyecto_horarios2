#main.py

#pip install tk
#pip install mysql-connector-python
#pip install datetime
#pip install tkcalendar
#pip install Pillow

#login.py


# ---TIPO DE CUENTAS---
#  1 = Maestro
#  2 = Preceptor
#  3 = Administrador



#Importar Librerias

from tkinter import *
from tkinter import ttk
#from PIL import ImageTk, Image
#from tkcalendar import Calendar
from login import login1
from menu import menu1
import mysql.connector
from datetime import datetime
#Importar Modulos
#import login as login2
with open('database.txt', 'r') as archivo:
    database_var = archivo.read()

print (database_var)

#conectar con mysql
try:
    sql = mysql.connector.connect(user='root',#usuario registrado en el mysql
                                  password='', #contraseña del usuario
                                  host='127.0.0.1', #IP del server mysql (en este caso localhost)
                                  autocommit=True, #automaticamente aplicar cambios
                                  database=database_var #Base de datos que se usara
                                  )
    cursor = sql.cursor()
except:
    print("No se pudo conectar con la base de datos, asegurece que XAMPP este abierto junto a MYSQL y Apache y que se haya ingresado un usuario valido.")
    exit()



#Auto Crear Base de datos y tabla
#cursor.execute("create database if not exists tecnica_2023")
#sql.database = "tecnica_2023"




#ventana principal
tk=Tk()
tk.title("TecBoletines")
tk.geometry("712x480")
#tk.resizable(0,0)
tk.minsize(tk.winfo_width(), tk.winfo_height())

#--ARREGLO BUG DE TKINTER--
def fixed_map(option):
    return [elm for elm in style.map('Treeview', query_opt=option) if
      elm[:2] != ('!disabled', '!selected')]
style = ttk.Style()
style.map('Treeview', foreground=fixed_map('foreground'),
  background=fixed_map('background'))


for columna in range(10):
    tk.grid_columnconfigure(columna,weight=1)
    print("a")
for fila in range(10):
    tk.grid_rowconfigure(fila,weight=1)
    print("b")

login=login1()
menu=menu1(tk,sql,cursor)

#print(login2.tipoCuenta)


def cerrarSesion():
    login.crear(tk,sql,cursor,menuFunc)

def menuFunc(tipoCuenta,nombreCuenta):
    menu.crear(tk, sql, cursor, tipoCuenta, nombreCuenta, cerrarSesion, menuFunc)
login.crear(tk,sql,cursor,menuFunc)


tk.mainloop()
