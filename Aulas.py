import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import Parte_principal
#Hecho por Javier Correa Y contribuciones de Tobias Bonanno y valentino signorello
def eliminar(ventana):
        for elemento in ventana.winfo_children():
            elemento.destroy()
def botones_aulas(ventana,menuFunc,tipoCuenta,nombreCuenta):
    global imagen_eliminar,imagen_aula_ver,imagen_lab_ver,imagen_taller_ver,imagen_volver,imagen_taller_añadir,imagen_aula_añadir,imagen_lab_añadir,menufunc,tipodecuenta,nombrecuenta
    ventana.title("Pantalla Principal")
    ventana.iconbitmap("Imagenes/Colegio_logo.ico")
    menufunc=menuFunc
    tipodecuenta=tipoCuenta
    nombrecuenta=nombreCuenta
    
    nuevo_color = "#c9daf8"  # Puedes cambiar esto al color que desees
    style = ttk.Style()
    style.configure("TFrame", background=nuevo_color)  # Cambia el fondo del tema TFrame
    imagen_eliminar = ImageTk.PhotoImage(Image.open("Imagenes/eliminar.png").resize((15,15)))
    imagen_lab_ver=ImageTk.PhotoImage(Image.open("Imagenes/lab_ver.png").resize((20,20)))
    imagen_aula_ver=ImageTk.PhotoImage(Image.open("Imagenes/aula_ver.png").resize((20,20)))
    imagen_taller_ver=ImageTk.PhotoImage(Image.open("Imagenes/taller_ver.png").resize((20,20)))
    imagen_lab_añadir=ImageTk.PhotoImage(Image.open("Imagenes/agregar_lab.png").resize((20,20)))
    imagen_aula_añadir=ImageTk.PhotoImage(Image.open("Imagenes/prueba.png").resize((20,20)))
    imagen_taller_añadir=ImageTk.PhotoImage(Image.open("Imagenes/taller_agregar_prueba.png").resize((20,20)))
    imagen_volver=ImageTk.PhotoImage(Image.open("imagenes/volver.png").resize((20,20)))
    frame_pe = ttk.Frame(ventana)
    frame_pe.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Configurar filas y columnas para centrar los botones en el medio
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)
    ventana.rowconfigure(0, weight=1)
    ventana.rowconfigure(1, weight=1)
    ventana.rowconfigure(2, weight=1)
    ventana.rowconfigure(3, weight=1)
    tk.Label(ventana,text="Pestaña de aulas",bg="#c9daf8",font=("Monaco", 24, "bold")).grid(row=0,column=0,columnspan=2,padx=10,pady=10)

    tk.Button(ventana, text="Volver",borderwidth=1,relief="solid",height=30,width=150,image=imagen_volver, compound="left", command=lambda: volver_al_menu(ventana)).grid(row=0, column=0,columnspan=2, padx=5, pady=5,sticky="nw" )
    tk.Button(ventana, text="Ver laboratorios",borderwidth=1,relief="solid", image=imagen_lab_ver, compound="left", command=lambda: ver_aula(("Tipo de aula", "Ubicacion", "Numero"), ("""SELECT * FROM aulas WHERE tipo_de_aula = "Laboratorio" """))).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    añadir_lab = tk.Button(ventana, text="Añadir laboratorios",borderwidth=1,relief="solid", image=imagen_lab_añadir, compound="left", command=lambda: agregar_aulas(("Tipo de aula", "Ubicacion", "Numero"), """SELECT * FROM aulas WHERE tipo_de_aula = "Laboratorio" """, "Laboratorio", (ventana)))
    añadir_lab.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    tk.Button(ventana, text="Ver aulas", image=imagen_aula_ver,borderwidth=1,relief="solid", compound="left", command=lambda: ver_aula(("Tipo de aula", "Ubicacion", "Numero"), ("""SELECT * FROM aulas WHERE tipo_de_aula = "Aula" """))).grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    añadir_aula = tk.Button(ventana, text="Añadir aulas",borderwidth=1,relief="solid", image=imagen_aula_añadir, compound="left", command=lambda: agregar_aulas(("Tipo de aula", "Ubicacion", "Numero"), """SELECT * FROM aulas WHERE tipo_de_aula = "Aula" """, "Aula", (ventana)))
    añadir_aula.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    tk.Button(ventana, text="Ver talleres", image=imagen_taller_ver,borderwidth=1,relief="solid", compound="left", command=lambda: ver_aula(("Tipo de aula", "Ubicacion", "Numero"), ("""SELECT * FROM aulas WHERE tipo_de_aula = "taller" """))).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    añadir_taller = tk.Button(ventana, text="Añadir talleres",borderwidth=1,relief="solid", image=imagen_taller_añadir, compound="left", command=lambda: agregar_aulas(("Tipo de aula", "Ubicacion", "Numero"), """SELECT * FROM aulas WHERE tipo_de_aula = "Taller" """, "Taller", (ventana)))
    añadir_taller.grid(row=3, column=1, padx=5, pady=5, sticky="ew")


    BG2color = "#6D9EEB"
    BG2 = tk.Frame(ventana, bg=BG2color, width=512, height=32)
    BG2.place(relx=0.0, rely=1.0, anchor='sw', relwidth=1.0, relheight=0.07)
    etiqueta_derecha = tk.Label(BG2, text="©5to1ra & 5to3ra - 2023", bg=BG2color,font=("Helvetica", 16))
    etiqueta_derecha.place(relx = 1.0, rely = 0.5, anchor ='e')
    if tipodecuenta==1:
        añadir_aula.configure(state="disabled")
        añadir_taller.configure(state="disabled")
        añadir_lab.configure(state="disabled")
    
def volver_al_menu(ventana,menuFunc,tipoCuenta,nombreCuenta):
    eliminar(ventana)
    menuFunc(tipoCuenta,nombreCuenta)    

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
       
   

def agregar_aulas(columnas_aula,query,Tipo_aula,ver_aula):
        global clicked, clicked2, laboratorio_numero, arriba, tree_aula, spinbox
        eliminar(ver_aula)
        
        conectar_base_de_datos()
        cursor = cnx.cursor()
        frame_pe = ttk.Frame(ver_aula)
        frame_pe.place(x=0, y=0, relwidth=1, relheight=1)
        treeview_aula=ttk.Labelframe(frame_pe, text="Aulas")
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
        for index, values in enumerate(data):
            tree_aula.insert(parent='', index='end', iid=index, values=values)
        tree_aula.pack()
        arriba = ttk.LabelFrame(frame_pe, text="Añadir")
        arriba.grid(padx=10, pady=10, row=0, column=0, sticky="nsew")
        imagen_eliminar =ImageTk.PhotoImage(Image.open("imagenes/eliminar.png").resize((20, 20), Image.LANCZOS))
        imagen_volver=ImageTk.PhotoImage(Image.open("imagenes/volver.png").resize((20,20)))
        style = ttk.Style()
        style.configure("TButton", background="black",width=40)         
        ttk.Button(arriba, text="Volver",image=imagen_volver,compound="left",width=21, command=lambda: volver_aulas(ver_aula)).grid(row=1, column=3, padx=2, pady=2)
        boton_de_eliminaraulas = tk.Button(arriba, text="Eliminar",width=150,image=imagen_eliminar,compound="left",fg="white",bg="#960000", command=lambda: opciones_aula(2)).grid(row=2, column=3, padx=2, pady=2)
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
        frame_pe.columnconfigure(0, weight=1)
        frame_pe.rowconfigure(1, weight=1)
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
    database='tecnica_2023'
    )
    # Crear un cursor para ejecutar consultas
    cursor = cnx.cursor()
def cerrar_base_de_datos():
    cursor.close()
    cnx.close()    
    
def volver_aulas(ventana):
    eliminar(ventana)
    botones_aulas(ventana,menufunc,tipodecuenta,nombrecuenta)

if __name__ == "__main__":
    tkw=tk.Tk()
    botones_aulas(tkw)
    tkw.mainloop()
