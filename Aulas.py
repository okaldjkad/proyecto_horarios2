import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import Parte_principal
#Hecho por Javier Correa Y contribuciones de Tobias Bonanno
def botones_aulas():
    global ventana,imagen_eliminar,imagen_aula_ver,imagen_lab_ver,imagen_taller_ver,imagen_volver,imagen_taller_añadir,imagen_aula_añadir,imagen_lab_añadir
    ventana = tk.Tk()
    ventana.geometry("800x600")
    ventana.title("Pantalla Principal")
    ventana.iconbitmap("Imagenes/Colegio_logo.ico")
    imagen_eliminar = ImageTk.PhotoImage(Image.open("Imagenes/eliminar.png").resize((15,15)))
    imagen_lab_ver=ImageTk.PhotoImage(Image.open("Imagenes/lab_ver.png").resize((20,20)))
    imagen_aula_ver=ImageTk.PhotoImage(Image.open("Imagenes/aula_ver.png").resize((20,20)))
    imagen_taller_ver=ImageTk.PhotoImage(Image.open("Imagenes/taller_ver.png").resize((20,20)))
    imagen_lab_añadir=ImageTk.PhotoImage(Image.open("Imagenes/agregar_lab.png").resize((20,20)))
    imagen_aula_añadir=ImageTk.PhotoImage(Image.open("Imagenes/prueba.png").resize((20,20)))
    imagen_taller_añadir=ImageTk.PhotoImage(Image.open("Imagenes/taller_agregar_prueba.png").resize((20,20)))
    imagen_volver=ImageTk.PhotoImage(Image.open("imagenes/volver.png").resize((20,20)))
    
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)
    ventana.rowconfigure(1, weight=1)
    ventana.rowconfigure(2, weight=1)
        # Crear un frame para contener los perfiles de usuario
        
    frame_lab = ttk.LabelFrame(ventana, text="aulas")
    frame_lab.grid(sticky="new", pady=2, padx=2,column=0,row=0)


    frame_lab.columnconfigure(0, weight=1)
    frame_lab.columnconfigure(1, weight=1)
    frame_lab.columnconfigure(2, weight=1)
    frame_lab.rowconfigure(0, weight=1)
    frame_lab.rowconfigure(1, weight=1)
    frame_lab.rowconfigure(2, weight=1)  
    ttk.Button(ventana, text="Volver",image=imagen_volver,compound="left", command=lambda: volver_al_menu(ventana)).grid(row=0, column=0, padx=2, pady=2)
        
    ttk.Button(frame_lab, text="Ver laboratorios",image=imagen_lab_ver,compound="left", command=lambda:ver_aula(("Tipo de aula","Ubicacion","Numero"),("""SELECT * FROM aulas WHERE tipo_de_aula = "Laboratorio" """))).grid(row=0, column=0, padx=2, pady=2,sticky="ew")
            

    añadir_lab = ttk.Button(frame_lab, text="Añadir laboratorios",image=imagen_lab_añadir,compound="left", command=lambda: agregar_aulas(("Tipo de aula", "Ubicacion", "Numero"), """SELECT * FROM aulas WHERE tipo_de_aula = "Laboratorio" """, "Laboratorio"))
    añadir_lab.grid(row=0, column=1, padx=2, pady=2, sticky="ew")

        
    ttk.Button(frame_lab, text="Ver aulas",image=imagen_aula_ver,compound="left", command=lambda:ver_aula(("Tipo de aula","Ubicacion","Numero"),("""SELECT * FROM aulas WHERE tipo_de_aula = "Aula" """))).grid(row=1, column=0, padx=2, pady=2,sticky="ew")
            
            
    añadir_aula=ttk.Button(frame_lab, text="Añadir aulas",image=imagen_aula_añadir,compound="left", command=lambda: agregar_aulas(("Tipo de aula", "Ubicacion", "Numero"), """SELECT * FROM aulas WHERE tipo_de_aula = "Aula" """, "Aula"))
    añadir_aula.grid(row=1, column=1, padx=2, pady=2,sticky="ew")            
        

            
    ttk.Button(frame_lab, text="Ver talleres",image=imagen_taller_ver,compound="left", command=lambda:ver_aula(("Tipo de aula","Ubicacion","Numero"),("""SELECT * FROM aulas WHERE tipo_de_aula = "taller" """))).grid(row=2, column=0, padx=2, pady=2,sticky="ew")
            
            
    añadir_taller= ttk.Button(frame_lab, text="Añadir talleres",image=imagen_taller_añadir,compound="left", command=lambda: agregar_aulas(("Tipo de aula", "Ubicacion", "Numero"), """SELECT * FROM aulas WHERE tipo_de_aula = "Taller" """, "Taller"))
    añadir_taller.grid(row=2, column=1, padx=2, pady=2,sticky="ew")
            

def validar50(P):
    valor = laboratorio_numero.get()
    if valor:

        numero = int(P)
        if  numero == 1 or numero <= 100:
            return True
        else:
            messagebox.showerror("Error", "El número no puede ser mayor que 100 ni menor que 1.")
            spinbox.set(1)
            return False
       
   

def agregar_aulas(columnas_aula,query,Tipo_aula):
        global clicked, clicked2, laboratorio_numero, arriba, tree_aula, spinbox    
        ventana.destroy()
        ver_aula = tk.Tk()
        conectar_base_de_datos()
        cursor = cnx.cursor()
        treeview_aula=ttk.Labelframe(ver_aula, text="Aulas")
        treeview_aula.grid(padx=10, pady=10, row=1, column=0, sticky="nsew")

        
        scrollbar = ttk.Scrollbar(treeview_aula)
        scrollbar.pack(side="right", fill="y")
        tree_aula = ttk.Treeview(treeview_aula, yscrollcommand=scrollbar.set, selectmode="extended")
        tree_aula.pack(expand=True, fill="both")
        scrollbar.config(command=tree_aula.yview)
        
        tree_aula["columns"]=(columnas_aula)
        tree_aula.column("#0", width=0,)
        for columna in columnas_aula:
            tree_aula.column(columna, anchor="center")
            tree_aula.heading(columna, text=columna)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        for index, values in enumerate(data):
            tree_aula.insert(parent='', index='end', iid=index, values=values)
        tree_aula.pack()
        arriba = ttk.LabelFrame(ver_aula, text="Añadir")
        arriba.grid(padx=10, pady=10, row=0, column=0, sticky="nsew")
        ttk.Button(arriba, text="Volver", command=lambda: volver_aulas(ver_aula)).grid(row=1, column=3, padx=2, pady=2)
        boton_de_eliminaraulas = ttk.Button(arriba, text="Eliminar", command=lambda: opciones_aula(2)).grid(row=2, column=3, padx=2, pady=2)
        clicked = tk.StringVar()
        
    
        menu_tipo_texto= ttk.Label(arriba, text="Tipo de aula:")
        menu_tipo_texto.grid(column=0, row=0, padx=5, pady=5)
        
        clicked2 = tk.StringVar()
        clicked2.set("Planta_alta")
        
        ttk.OptionMenu(arriba, clicked2, "Planta_alta", "Planta_baja", "Planta_alta").grid(column=1, row=1, padx=5, pady=5)
        
        
    
        
        menu_ubicacion_texto= ttk.Label(arriba, text="Ubicacion:")
        menu_ubicacion_texto.grid(column=1, row=0, padx=5, pady=5)
        
        laboratorio_numero= tk.IntVar()
        
        spinbox=ttk.Spinbox(arriba, width=10, textvariable=laboratorio_numero,from_=1,to=100,increment=1,validate="key", state="readonly")
        spinbox.grid(column=2, row=1, padx=5, pady=5)
        spinbox.set(1)
        


        
        entry_numero_texto= ttk.Label(arriba, text="Numero:")
        entry_numero_texto.grid(column=2, row=0, padx=5, pady=5)
        
        boton_de_agregaraulas = ttk.Button(arriba, text="Agregar", command=lambda:opciones_aula(1))
        boton_de_agregaraulas.grid(column=3, row=0, padx=5, pady=5)
        try:
            menu_tipo_laboratorio= [Tipo_aula,Tipo_aula]
            
            ttk.OptionMenu(arriba, clicked,*menu_tipo_laboratorio).grid(column=0, row=1, padx=5, pady=5)
        
        except:    
            menu_tipo_laboratorio= ["Laboratorio", "Aula", "Taller","Laboratorio"]
            ttk.OptionMenu(arriba, clicked,*menu_tipo_laboratorio).grid(column=0, row=1, padx=5, pady=5)
        ver_aula.columnconfigure(0, weight=1)
        ver_aula.rowconfigure(1, weight=1)
        treeview_aula.columnconfigure(0, weight=1)
        treeview_aula.rowconfigure(1, weight=1)
        arriba.rowconfigure(0, weight=1)
        for x in range(3):
            arriba.columnconfigure(x, weight=1)
        cerrar_base_de_datos()
    
        
   
  
def opciones_aula(option):
    conectar_base_de_datos()
    if option == 1:
        global nuevo_valor, valor_actual
            
        obtenertipo = (clicked.get())  
        obtenerubicacion = (clicked2.get())  
        obtenernumero = laboratorio_numero.get()
        if not obtenernumero:
            messagebox.showerror("Error", "Debe ingresar todos los datos.")
            return False         
        try:
            obtenernumero = int(obtenernumero)
        except ValueError:
            messagebox.showerror("Error", "El número debe ser un valor numérico.")
            return
        


        # Verificar si la fila ya existe en la base de datos
        select_query = "SELECT * FROM aulas WHERE Tipo_de_aula = %s AND Ubicacion = %s AND Numero = %s"
        data_verificar = (obtenertipo, obtenerubicacion, obtenernumero)
                
        cursor = cnx.cursor()
        cursor.execute(select_query, data_verificar)
        existing_row = cursor.fetchone()
            
        if existing_row:
            messagebox.showerror("Error", "La fila ya existe en la base de datos.")
            return     
        valor_actual = int(laboratorio_numero.get())
        if valor_actual >= 1 or valor_actual == 99:
            nuevo_valor = valor_actual + 1
            laboratorio_numero.set(nuevo_valor)
            insert_query = "INSERT INTO aulas (Tipo_de_aula, Ubicacion, Numero) VALUES (%s, %s, %s)"
            dataagregar = (obtenertipo, obtenerubicacion, obtenernumero)
                    
                    
            cursor = cnx.cursor()
            cursor.execute(insert_query, dataagregar)
            cnx.commit()  # Importante: Confirmar los cambios en la base de datos
                    
            cursor.close()
            cnx.close()
        
            messagebox.showinfo("Aviso", "Aula agregada correctamente, para ver los cambios tiene que ir a la opción ver")
            
            tree_aula.insert(parent='', index='end', values=(obtenertipo, obtenerubicacion, obtenernumero)) 
            cerrar_base_de_datos()
        else:
            messagebox.showerror("Error", "El número no puede ser mayor a 100 ni menor a 1")
            return False






        
        
    elif option==2:
        
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar estos datos?")
        if respuesta:
            conectar_base_de_datos()
            eleccion = tree_aula.selection()
            if not eleccion:
                messagebox.showerror("Error", "Seleccione al menos un aula")
            else:
                try:
                    cursor = cnx.cursor()
                    for ele in eleccion:
                        obtenertipo = tree_aula.item(ele, "values")
                        cursor.execute("DELETE FROM aulas WHERE Tipo_de_aula = %s AND Ubicacion = %s AND Numero = %s",(obtenertipo[0], obtenertipo[1], obtenertipo[2]))
                        tree_aula.delete(ele)
                    cnx.commit()
                    cursor.close()
            
                    if len(eleccion) == 1:
                        messagebox.showinfo("eliminar", "eliminado exitosamente")
                    else:
                        messagebox.showinfo("eliminar", f"{len(eleccion)} opciones eliminadas exitosamente")
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error al eliminar: {str(e)}")
                finally:
                    cerrar_base_de_datos()

def ver_aula(columnas_aula,query):
    ver_aula = tk.Toplevel()
    conectar_base_de_datos()
    scrollbar = ttk.Scrollbar(ver_aula)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree_aula = ttk.Treeview(ver_aula, yscrollcommand=scrollbar.set, selectmode="extended")
    tree_aula.pack(expand=True, fill="both")
    scrollbar.config(command=tree_aula.yview)
    
    tree_aula["columns"]=(columnas_aula)
    tree_aula.column("#0", width=0, stretch=tk.NO)
    for columna in columnas_aula:
        tree_aula.column(columna, anchor=tk.CENTER)
        tree_aula.heading(columna, text=columna)
    cursor.execute(query)
    data = cursor.fetchall()
    try:
        data.sort(key=lambda x: x[2])
    except IndexError:
        pass
    for index, values in enumerate(data):
        tree_aula.insert(parent='', index='end', iid=index, values=values)
    tree_aula.pack()
    cerrar_base_de_datos()
    
def conectar_base_de_datos():
    global cursor
    global cnx
    cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='proyecto_colegio2'
    )
    # Crear un cursor para ejecutar consultas
    cursor = cnx.cursor()
def cerrar_base_de_datos():
    cursor.close()
    cnx.close()    
    
def volver_al_menu(ventana):
    ventana.destroy()
    Parte_principal.primer_menu()
def volver_aulas(ventana):
    ventana.destroy()
    Parte_principal.aulas()  