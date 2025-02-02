import tkinter as tk
import mysql.connector
from tkinter import messagebox
from CompletarAU import AutocompleteEntry
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import Parte_principal
import re
#Hecho por Javier Correa
def eliminar(ventana):
    for elemento in ventana.winfo_children():
        elemento.destroy()
        
def botones_docentes(ventana3):
    ventana3.geometry("800x600")
    ventana3.title("Pantalla Principal")
    ventana3.iconbitmap("Imagenes/Colegio_logo.ico")
    global frame_pe
    frame_pe = ttk.Frame(ventana3)
    frame_pe.place(x=0, y=0, relwidth=1, relheight=1)
    frame_pe.columnconfigure(0, weight=1)
    frame_pe.rowconfigure(0, weight=1)
    frame_pe.rowconfigure(1, weight=1)
    frame_pe.rowconfigure(2, weight=1)
        

    frame_docentes = ttk.LabelFrame(frame_pe, text="Profesores")
    frame_docentes.grid(sticky="new", pady=2, padx=2,column=0,row=2)
        
    frame_docentes.columnconfigure(0, weight=1)
    frame_docentes.columnconfigure(1, weight=1)
    frame_docentes.columnconfigure(2, weight=1)
    frame_docentes.rowconfigure(0, weight=1)
    frame_docentes.rowconfigure(1, weight=1)
    frame_docentes.rowconfigure(2, weight=1)
    ttk.Button(ventana3, text="Volver", command=lambda: volver_al_menu(ventana3)).grid(row=0, column=0, padx=2, pady=2)
    ttk.Button(frame_docentes, text="Ver profesores", command=lambda:ver_profes(("Id_profesor","Nombre", "Apellido", "Telefono", "Tipo_documento","Nro_de_documento", "Correo","Direccion","Altura","Departamento","Fecha_nacimiento"), ("""SELECT Id_profesor, Nombre, Apellido, Telefono, Tipo_documento,Nro_de_documento, Correo,Direccion,Altura,Departamento,Fecha_nacimiento FROM profesores ORDER BY Nombre ASC, Apellido ASC"""),(ventana3),1)).grid(row=0, column=0, padx=2, pady=2,sticky="ew")
        

    añadir_profes=ttk.Button(frame_docentes, text="Añadir profesores", command=lambda:agregar_profesores(( "Id_profesor","Nombre", "Apellido", "Telefono", "Tipo_documento","Nro_de_documento", "Correo","Direccion","Altura","Departamento","Fecha_nacimiento"), ("""SELECT Id_profesor,Nombre, Apellido, Telefono, Tipo_documento,Nro_de_documento, Correo,Direccion,Altura,Departamento,Fecha_nacimiento FROM profesores ORDER BY Nombre ASC, Apellido ASC"""),(ventana3)))
    añadir_profes.grid(row=0, column=1, padx=2, pady=2,sticky="ew")
    ttk.Button(frame_docentes, text="Ver materias", command=lambda:ver_aula(( "Nombre_materia", "Año", "Division", "Grupo", "Especialidad"), """SELECT nombre_materia, año, division, Grupo, Especialidad FROM espacio_curricular ORDER BY nombre_materia ASC""",(ventana3),(True)),).grid(row=1, column=0, padx=2, pady=2,sticky="ew")
        
    añadir_materia_boton=ttk.Button(frame_docentes, text="Añadir materias", command=lambda:agregar_materias(( "Nombre_materia", "Año", "Division", "Grupo", "Especialidad"), """SELECT nombre_materia, año, division, Grupo, Especialidad FROM espacio_curricular ORDER BY nombre_materia ASC""",(ventana3)))
    añadir_materia_boton.grid(row=1, column=1, padx=2, pady=2,sticky="ew")
        
   
def capitalize_first_letter(entry_widget):
    # Obtenemos el contenido actual del Entry
    try:
        current_text = entry_widget.get()

        # Capitalizamos la primera letra de cada palabra si el contenido no está vacío
        if current_text:
            capitalized_words = [word.capitalize() for word in current_text.split()]
            capitalized_text = " ".join(capitalized_words)
            entry_widget.delete(0, tk.END)  # Borramos el contenido actual
            entry_widget.insert(0, capitalized_text) 
            return True
    except:
        messagebox.showerror("Error", "No tiene mayuscula el inicio de los nombres")
        return False 

def validar_numeros(P):
    # Función de validación para permitir solo caracteres numéricos
    if all(c.isdigit() for c in P):
        return True
    else:
        messagebox.showerror("Error", "Solo se permiten números")
        return False
def validar_letras(P):
    
    # Esta función permite solo letras y números
    if all(c.isalpha() or c.isspace() for c in P):
        return True
    else:
        messagebox.showerror("Error", "Solo se permiten letras")
        return False 

def validar_letras_numeros(P):
    
    # Esta función permite solo letras y números
    if all(c.isalpha() or c.isspace() or c.isdigit() for c in P):
        return True
    else:
        messagebox.showerror("Error", "Solo se permiten letras y numeros")
        return False 


def arroba(event):
    contenido = entry_correo.get()
    # Utilizamos una expresión regular para verificar el formato del correo
    if contenido.count('.') > 3 or contenido.count('.') == 0 or contenido.count('@') != 1 or not re.match(r'^[\w-]+@', contenido):
        # Si el correo no cumple con el formato o tiene más de una "@", mostramos un mensaje de error
        tk.messagebox.showerror("Error", "Dirección de correo inválida su correo debe verse asi example@gmail.com")
        entry_correo.delete(0, tk.END)  # Borramos el contenido del Entry
        return False  
def limite(event):
    contenido = entry_dni.get()
    contenido2 = entry_telefono2.get()
    contenido3 = entry_correo.get()
    contenido4 = entry_direccion.get()
    contenido5 = entry_Altura.get()
    contenido6 = añadir_nombre.get()   
    contenido7 = añadir_apellido.get()
    
    if len(contenido) > 10:
        # Limitar el contenido a 11 caracteres
        nuevo_contenido = contenido[:10]
        entry_dni.delete(0, tk.END)
        entry_dni.insert(0, nuevo_contenido)
        messagebox.showerror("Error", "Solo se permiten 10 caracteres")
    elif len(contenido2) > 20:
        nuevo_contenido = contenido[:20]
        entry_telefono2.delete(0, tk.END)
        entry_telefono2.insert(0, nuevo_contenido)
        messagebox.showerror("Error", "Solo se permiten 20 caracteres")
    elif len(contenido3) > 100:
        nuevo_contenido = contenido[:100]
        entry_correo.delete(0, tk.END)
        entry_correo.insert(0, nuevo_contenido)
        messagebox.showerror("Error", "Solo se permiten 50 caracteres")
    elif len(contenido4) > 100:
        nuevo_contenido = contenido[:100]
        entry_direccion.delete(0, tk.END)
        entry_direccion.insert(0, nuevo_contenido)
        messagebox.showerror("Error", "Solo se permiten 50 caracteres")
    elif len(contenido5) > 6:
        nuevo_contenido = contenido[:6]
        entry_Altura.delete(0, tk.END)
        entry_Altura.insert(0, nuevo_contenido)
        messagebox.showerror("Error", "Solo se permiten 6 caracteres")
    elif len(contenido6)  > 100:
        nuevo_contenido = contenido[:100]
        añadir_nombre.delete(0, tk.END)
        añadir_nombre.insert(0, nuevo_contenido)
        messagebox.showerror("Error", "Solo se permiten 30 caracteres")
    elif len(contenido7) > 100:
        nuevo_contenido = contenido[:100]
        añadir_apellido.delete(0, tk.END)
        añadir_apellido.insert(0, nuevo_contenido)
        messagebox.showerror("Error", "Solo se permiten 30 caracteres")

def guardar_informacion(event):
    obtenerfecha = entry_fecha.get()
    
    # Verifica si la fecha es válida
    if not es_fecha_valida(obtenerfecha):
        messagebox.showerror("Error", "Debe seleccionar una fecha a traves del calendario.")
        entry_fecha.delete(0, tk.END)
        return False

def es_fecha_valida(fecha):
    try:
        datetime.strptime(fecha, "%Y/%m/%d")
        return True
    except ValueError:
        return False   
    
def validar_prefijo(event, entry_widget,ver_Profesores):
        entry_telefono.hide_listbox(ver_Profesores)
        widget_con_enfoque = entry_telefono.focus_get()
        if isinstance(widget_con_enfoque, tk.Listbox):
            return
        entrada = entry_widget.get()
        if not entrada in prefijos:
            messagebox.showerror("Error", "Por favor seleccionar la opcion del menu")
            entry_widget.delete(0, tk.END)


def toggle_entry_state():
    if check_var.get() == 0:
        entry_Altura.config(state=tk.NORMAL)  # Habilita el Entry
    else:
        entry_Altura.delete(0, tk.END)
        entry_Altura.config(state=tk.DISABLED)  # Deshabilita el Entry

def entrys(ver_Profesores):
    global añadir_nombre,check_departamento, check_departamento ,añadir_apellido, entry_telefono, entry_dni, entry_fecha, entry_correo, entry_direccion, entry_Altura, boton, check_var, variable4, arriba3, treeview_Profe, spin_piso, piso, departamento, prefijos, entry_telefono2, c_a, Opciones_departamento
    for x in range(7):
        arriba3.columnconfigure(x, weight=1)
    arriba3.rowconfigure(0, weight=1)
    arriba3.rowconfigure(1, weight=1)
    
    ttk.Button(arriba3, text="Volver", command=lambda: volver_docentes(ver_Profesores)).grid(row=1, column=7, padx=2, pady=2)
    ttk.Label(arriba3, text="Nombre:").grid(column=0, row=0)
    
    añadir_nombre=ttk.Entry(arriba3)
    añadir_nombre.grid(column=0, row=1)
    añadir_nombre.bind("<FocusOut>", lambda event: capitalize_first_letter(añadir_nombre))
    añadir_nombre.bind("<KeyRelease>", limite)
    añadir_nombre.bind('<Return>', lambda event: procesar_enter(event, añadir_apellido))
    añadir_nombre.focus_set()
    añadir_nombre.config(validate="key",validatecommand=(arriba3.register(validar_letras), "%P"))
    
    ttk.Label(arriba3, text="Apellido").grid(column=1, row=0)
    
    añadir_apellido=ttk.Entry(arriba3)
    añadir_apellido.grid(column=1, row=1,  padx=5, pady=5)
    añadir_apellido.config(validate="key",validatecommand=(arriba3.register(validar_letras), "%P"))
    añadir_apellido.bind("<FocusOut>", lambda event: capitalize_first_letter(añadir_apellido))
    añadir_apellido.bind("<KeyRelease>", limite)
    añadir_apellido.bind("<Up>", lambda event: flecha_arriba(event, añadir_nombre))
    
    
    valor_predeterminado = "+54 9"

# Crea una instancia de StringVar y establece el valor predeterminado
    string_var = tk.StringVar()
    string_var.set(valor_predeterminado)

    # Crea el Entry y enlaza su textvariabl
    ttk.Label(arriba3, text="Codigo de area:").grid(column=2, row=0)
    c_a = tk.Entry(arriba3, textvariable=string_var, state=tk.DISABLED, width=len(valor_predeterminado))
    c_a.grid(column=2, row=1)
    
    ttk.Label(arriba3, text="Prefijos:").grid(column=3, row=0)
    prefijos=[]
    with open('numero_codigo.txt', 'r') as archivo:
        for linea in archivo:
            numero = linea.strip()
            prefijos.append(numero)
    entry_telefono = AutocompleteEntry(prefijos,arriba3)
    entry_telefono.bind("<FocusOut>", lambda event: validar_prefijo(event, entry_telefono,ver_Profesores))
    entry_telefono.grid(row=1, column=3)
    
    ttk.Label(arriba3, text="Numero de telefono").grid(column=4, row=0)
    entry_telefono2 = ttk.Entry(arriba3, validate="key")
    entry_telefono2.config(validatecommand=(arriba3.register(validar_numeros), "%P"))
    entry_telefono2.bind("<KeyRelease>", limite)
    entry_telefono2.grid(row=1, column=4)
    
    ttk.Label(arriba3, text="Nro de documento").grid(column=6, row=0)
    
    
    entry_dni = ttk.Entry(arriba3, validate="key")
    entry_dni.config(validatecommand=(arriba3.register(validar_numeros), "%P"))
    entry_dni.bind("<KeyRelease>", limite)
    entry_dni.grid(row=1, column=6)
    

    ttk.Label(arriba3, text="Correo electronico:").grid(column=0, row=3)
    entry_correo = ttk.Entry(arriba3)
    entry_correo.bind("<KeyRelease>", limite)
    entry_correo.bind("<FocusOut>", arroba,)
    entry_correo.grid(row=4, column=0, pady=10)
    
    ttk.Label(arriba3, text="Dirección:").grid(column=1, row=3)
    entry_direccion = ttk.Entry(arriba3)
    entry_direccion.bind("<KeyRelease>", limite)
    entry_direccion.bind("<FocusOut>", lambda event: capitalize_first_letter(entry_direccion))
    entry_direccion.grid(row=4, column=1, pady=10, padx=5)
    
    ttk.Label(arriba3, text="Numero:").grid(column=2, row=3)
    entry_Altura = ttk.Entry(arriba3)
    entry_Altura.bind("<KeyRelease>", limite)
    entry_Altura.config(validate="key", validatecommand=(arriba3.register(validar_numeros), "%P"))
    entry_Altura.grid(row=4, column=2, pady=10)
    check_var = tk.IntVar()
    altura = ttk.Checkbutton(arriba3, text="Sin altura", variable=check_var, command=toggle_entry_state)
    altura.grid(row=5, column=2, pady=10)
    
    ttk.Label(arriba3, text="Piso(opcional)").grid(column=3, row=3)
    piso = tk.StringVar() 
    spin_piso = ttk.Spinbox(arriba3,textvariable=piso,from_=0,to=100,validate="key", state="readonly")
    spin_piso.grid(row=4, column=3, pady=10)
    spin_piso.config(validate="key", validatecommand=(arriba3.register(validar_letras_numeros), "%P"))
    spin_piso.config(validatecommand=(arriba3.register(validar50), "%P"))
    
    ttk.Label(arriba3, text="Departamento(opcional)").grid(column=4, row=3)
    Opciones_departamento=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    departamento = ttk.Combobox(arriba3, values=Opciones_departamento, state="readonly")

    departamento.grid (row=4, column=4, padx=20)
    ttk.Label(arriba3, text="Fecha de nacimiento:").grid(column=5, row=3)
    today = datetime.now()
    max_date = today - timedelta(days=365 * 18+4)
    check_departamento = tk.IntVar()
    check_departamento_button = ttk.Checkbutton(arriba3, text="Sin departamento", variable=check_departamento,  command=toggle_checkbutton)
    check_departamento_button.grid(row=5, column=4, padx=20)
    # Crea el widget DateEntry con la fecha máxima predefinida
    entry_fecha = DateEntry(arriba3, selectmode="day", year=2000, month=1, day=1,date_pattern="yyyy/mm/dd", mindate=None, maxdate=max_date)
    entry_fecha.grid(row=4, column=5, padx=20)
    entry_fecha.bind("<KeyRelease>", guardar_informacion)
    
def toggle_checkbutton():
    if check_departamento.get() == 0:
        spin_piso.config(state="readonly")
        departamento.set("")
        spin_piso.set("")
        departamento.config(state="readonly")

    else:    
        spin_piso.config(state=tk.DISABLED)
        spin_piso.set("")
        departamento.set("")
        departamento.config(state=tk.DISABLED)    
   

def agregar_numero():
    global numero
    numero = piso.get()
    if numero != 0:
        spin_piso.set(numero)
def validar50(P):
    global valor
    valor = piso.get()
    if valor:
        numero = int(P)
        if 1 <= numero <= 100:
            return True  
def ver_profes(columnas_aula,query,ver_Profesores,eliminar_b):
    global tree_Profe, treeview_Profe, tree_Profe,frame_pe
    if eliminar_b==1:
        print("anashe")
        eliminar(ver_Profesores)
        frame_pe = ttk.Frame(ver_Profesores)
        frame_pe.place(x=0, y=0, relwidth=1, relheight=1)
        
    ver_Profesores.title("Profesores")
    ver_Profesores.minsize(1000, 400)
    conectar_base_de_datos()
    cursor = cnx.cursor()
    treeview_Profe=ttk.Labelframe(frame_pe, text="Profesores")
    treeview_Profe.grid(padx=10, pady=10, row=1, column=0, sticky="nsew")

    
    scrollbar = ttk.Scrollbar(treeview_Profe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree_Profe = ttk.Treeview(treeview_Profe, yscrollcommand=scrollbar.set, selectmode="extended")
    tree_Profe.pack(expand=True, fill="both")
    tree_Profe.bind("<Double-1>", doble_click)
    scrollbar.config(command=tree_Profe.yview)
    tree_Profe["columns"]=("Id_profesor","Nombre", "Apellido", "Telefono", "Tipo_documento","Nro_de_documento", "Correo","Direccion","Altura","Departamento","Fecha_nacimiento") 
    tree_Profe.column("#0", width=0, stretch=0)
    tree_Profe.column("Id_profesor", anchor="n", width=1) 
    tree_Profe.column("Nombre", anchor="center", width=50)
    tree_Profe.column("Apellido", anchor="center", width=50)
    tree_Profe.column("Telefono", anchor="center", width=200)
    tree_Profe.column("Tipo_documento", anchor="center", width=50)
    tree_Profe.column("Nro_de_documento", anchor="center", width=30)
    tree_Profe.column("Correo", anchor="center", width=50)
    tree_Profe.column("Direccion", anchor="center", width=50)
    tree_Profe.column("Altura", anchor="center", width=10)
    tree_Profe.column("Departamento", anchor="center", width=20)
    tree_Profe.column("Fecha_nacimiento", anchor="center", width=20)
    columnas_aula = ("Id_profesor", "Nombre", "Apellido", "Telefono", "Tipo_documento", "Nro_de_documento", "Correo", "Direccion", "Altura","Departamento", "Fecha_nacimiento")
    for columna in columnas_aula:
        tree_Profe.column(columna, anchor="center", width=100)
        tree_Profe.heading(columna, text=columna)
    cursor.execute(query)
    data = cursor.fetchall()
    for index, values in enumerate(data):
        tree_Profe.insert(parent='', index='end', iid=index, values=values)
    tree_Profe.pack()
    treeview_Profe.columnconfigure(0, weight=1)
    treeview_Profe.rowconfigure(1, weight=1)
    frame_pe.columnconfigure(0, weight=1)
    frame_pe.rowconfigure(1, weight=1)
    
def agregar_profesores(columnas_aula,query,ver_Profesores):
    global añadir_nombre, añadir_apellido, entry_telefono,entry_dni,entry_fecha, entry_correo, entry_direccion, entry_Altura, check_var, variable4, arriba3, opciones_documento,tree_Profe, treeview_Profe, tree_Profe,frame_pe
    eliminar(ver_Profesores)
    frame_pe = ttk.Frame(ventana)
    frame_pe.place(x=0, y=0, relwidth=1, relheight=1)
    ver_profes(columnas_aula,query,ver_Profesores,0)
    arriba3 = ttk.LabelFrame(frame_pe, text="Añadir")
    arriba3.grid(row=0, column=0,sticky="nsew")
    ttk.Label(arriba3, text="Tipo de documento:").grid(column=5, row=0)
    variable4 = tk.StringVar(arriba3)
    opciones_documento =  ["DU","DNI","Libreta de enrolamiento", "Libreta civica", "Pasaporte", "Cedula de identidad"]
    division = ttk.OptionMenu(arriba3, variable4, opciones_documento[0], *opciones_documento)
    division.grid(column=5, row=1)
    ver_Profesores.protocol("WM_DELETE_WINDOW",lambda: volver_docentes(ver_Profesores))
    ttk.Button(arriba3, text="Agregar", command=lambda:  opciones_docentes(3)).grid(column=7, row=0, sticky="nsew")
    ttk.Button(arriba3, text="Eliminar", command=lambda:  opciones_docentes(4)).grid(column=7, row=3, sticky="nsew")
    ttk.Button(arriba3, text="Modificar", command=lambda:  opciones_docentes(7)).grid(column=7, row=4, sticky="nsew")
    entrys(ver_Profesores)
    for x in range(7):
        arriba3.rowconfigure(x, weight=1)
        arriba3.columnconfigure(x, weight=1)
    cerrar_base_de_datos()    



def funcionamiento2():
    messagebox.showinfo("Explicación","Como eliminar una fila: La tabla que aparece abajo es la tabla de profesores, para eliminar un profesor haga click y deje seleccionada la fila que quiera eliminar y luego haga click en el boton eliminar, si no se hace click en alguna fila abra un error.\n"
                        "\nComo eliminar varias filas: Para eliminar varias filas puede usar el comando shift+click manteniendolo apretado y seleccionando varios.\n" 
                        "\nEl boton de volver es para ir a la ventana anterior que seria la de los botones de ver añadir y eliminar")
def explicacion2():
    messagebox.showinfo("Explicación","Lo que se ve en la pantalla es la tabla de datos donde se ve la informacion guardada de cada profesor, para saber su funcionamiento haga click en el boton como funciona")



    
    
      
def letras(P):
    if all(c.isalpha() or c.isspace()or c=="_" for c in P):
        return True
    else:
        messagebox.showerror("Error", "Solo se permiten letras.")
        return False    

    # Obtener los valores actuales de las variables
   

def limite3(event):
    contenido = materia_nombre.get()
    contenido1 = entry_especialidad.get()
    if len(contenido) > 30:
        nuevo_contenido = contenido[:30]
        materia_nombre.delete(0, tk.END)
        materia_nombre.insert(0, nuevo_contenido)
        messagebox.showerror("Error", "Solo se permiten 30 caracteres")
    elif len(contenido1) > 30:
        nuevo_contenido1 = contenido1[:30]
        entry_especialidad.delete(0, tk.END)
        entry_especialidad.insert(0, nuevo_contenido1)
        messagebox.showerror("Error", "Solo se permiten 30 caracteres")
def borrar_entrys():
    entrys().delete(0, tk.END)
     
    


def doble_click(event):
    global values
    item = tree_Profe.selection()
    if item:
        values = tree_Profe.item(item, "values")
        añadir_nombre.delete(0, tk.END)
        añadir_nombre.insert(0, values[1])
        añadir_apellido.delete(0, tk.END)
        añadir_apellido.insert(0, values[2])

        # Divide la cadena en código de área, Teléfono1 y Teléfono2
        telefonos = values[3].split()



        if len(telefonos) >= 2:
            telefono1 = telefonos[2]
        else:
            telefono1 = ""

        if len(telefonos) >= 3:
            telefono2 = telefonos[3]
        else:
            telefono2 = ""
        

        entry_telefono.delete(0, tk.END)
        entry_telefono.insert(0, telefono1)

        entry_telefono2.delete(0, tk.END)
        entry_telefono2.insert(0, telefono2)

        entry_dni.delete(0, tk.END)
        entry_dni.insert(0, values[5])

        variable4.set(values[4])

        entry_correo.delete(0, tk.END)
        entry_correo.insert(0, values[6])

        entry_direccion.delete(0, tk.END)
        entry_direccion.insert(0, values[7])

        entry_Altura.delete(0, tk.END)
        entry_Altura.insert(0, values[8])


        # Obtén el valor del departamento si existe
        if check_departamento.get() == 0:
            departamento_completo = values[9]  # Por ejemplo, "Piso 1-B"
            partes = departamento_completo.split()  # Dividir por espacios
            if len(partes) >= 2:
                numero_piso = partes[1]  # El segundo elemento es el número de piso
                codigo_departamento = partes[2] if len(partes) > 2 else ""  # El tercer elemento es el código de departamento, si existe
            
                # Establecer los valores en los widgets correspondientes
                spin_piso.set(numero_piso)
            
                # Establecer el valor seleccionado en el Combobox
                departamento.set(codigo_departamento)   

            
            
        
        

        entry_fecha.delete(0, tk.END)
        entry_fecha.insert(0, values[10])
                
def funcionamiento():
    messagebox.showinfo("Explicación","Como modificar: La tabla que aparece abajo es la tabla de profesores, para modificar un profesor haga dobleclick en la fila que quiera modificar y luego haga click en el boton modificar, si no se hace doble click en alguna fila abra un error.\n"
                        "\nCada caja de entrada maneja un limite de caracteres que al soltar el teclado si el limite es superado se borra el contenido extra.\n" 
                        "\nEl boton de volver es para ir a la ventana anterior que seria la de los botones de ver añadir y eliminar")
def explicacion():
    messagebox.showinfo("Explicación","Lo que se ve en la pantalla son 2 sectores una con la seccion donde se ingresan los datos para modificar y otra con la tabla de datos donde se ve la informacion guardada de cada profesor, para saber su funcionamiento haga click en el boton como funciona")
  
def agregar_materias(columnas_aula,query,ver_Materias):
    global materia_nombre,entry_especialidad, tree_materias, año, division, variable2, variable1,opciones_division1, variable3, opciones_año, opciones_division, opciones_division2, opciones_divisionci
    eliminar(ver_Materias)
    frame_pe = ttk.Frame(ventana)
    frame_pe.place(x=0, y=0, relwidth=1, relheight=1)
    ver_Materias.title("Materias")
    ver_Materias.protocol("WM_DELETE_WINDOW",lambda: volver_docentes(ver_Materias))
    conectar_base_de_datos()
    treeview_Materias=ttk.Labelframe(frame_pe, text="Materias")
    treeview_Materias.grid(padx=10, pady=10, row=1, column=0, sticky="nsew")
    scrollbar = ttk.Scrollbar(treeview_Materias)
    scrollbar.pack(side="right", fill="y")
    tree_materias = ttk.Treeview(treeview_Materias, yscrollcommand=scrollbar.set, selectmode="extended")
    tree_materias.pack(expand=True, fill="both")
    scrollbar.config(command=tree_materias.yview)
    
    tree_materias["columns"]=(columnas_aula)
    tree_materias.column("#0", width=0,)
    for columna in columnas_aula:
        tree_materias.column(columna, anchor="center")
        tree_materias.heading(columna, text=columna)
    cursor.execute(query)
    data = cursor.fetchall()
    for index, values in enumerate(data):
        tree_materias.insert(parent='', index='end', iid=index, values=values)
    tree_materias.pack()
    
    arriba5 = ttk.LabelFrame(frame_pe, text="Añadir")
    arriba5.grid(padx=10, pady=10, row=0, column=0, sticky="nsew")
    ttk.Button(arriba5, text="Volver", command=lambda: volver_docentes(ver_Materias)).grid(row=2, column=4, padx=2, pady=2)
    ttk.Button(arriba5, text="Agregar", command=lambda: opciones_docentes(5)).grid(row=1, column=4, padx=2, pady=2)
    ttk.Button(arriba5, text="Eliminar", command=lambda:  opciones_docentes(6)).grid(column=4, row=3, sticky="ew")
    ttk.Label(arriba5, text="Nombre de la materia:").grid(column=0, row=0, sticky="nsew")
    opciones_division=[]
    materia_nombre=ttk.Entry(arriba5, width=10)
    materia_nombre.config(validate="key", validatecommand=(arriba5.register(letras), "%P"))
    materia_nombre.bind("<FocusOut>", lambda event: capitalize_first_letter(materia_nombre))
    materia_nombre.grid(column=0, row=1)
    materia_nombre.bind("<KeyRelease>", limite3)
    materia_nombre.focus_set()
    
    ttk.Label(arriba5, text="Año:").grid(column=1, row=0, sticky="nsew")
    variable1 = tk.IntVar(arriba5)
    variable1.trace("w", actualizar_division)
    opciones_año = [0,1,2,3,4,5,6,7]
    
    año = ttk.OptionMenu(arriba5, variable1, opciones_año[0], *opciones_año)
    año.grid(column=1, row=1)
    
    ttk.Label(arriba5, text="Division:").grid(column=2, row=0, sticky="nsew")
    variable2 = tk.StringVar(arriba5)
    opciones_division2 =  ["1", "2", "3", "4", "5", "6"] 
    opciones_division1 = ["A", "B", "C", "D", "E"]
    division = ttk.OptionMenu(arriba5,variable2, *opciones_division)
    division.grid(column=2, row=1, sticky="nsew")
    
    ttk.Label(arriba5, text="Grupo:").grid(column=3, row=0, sticky="nsew")
    variable3 = tk.StringVar(arriba5)
    opciones_grupo =  ["Ambos","A", "B", "C", "D", "E", "F", "G"]
    grupo = ttk.OptionMenu(arriba5, variable3, opciones_grupo[0], *opciones_grupo)
    grupo.grid(column=3, row=1, sticky="nsew")
    lista_especialidad=["Laboratorio programacion", "Maestro mayor de obras", "Informatica", ""]

    entry_especialidad = ttk.Combobox(arriba5, values=lista_especialidad, state="readonly")
  

    entry_especialidad.grid(column=0, row=3, padx=5, pady=5)
        
    
    treeview_Materias.columnconfigure(0, weight=1)
    treeview_Materias.rowconfigure(1, weight=1)
    frame_pe.columnconfigure(0, weight=1)
    frame_pe.rowconfigure(1, weight=1)
    for x in range(5):
        arriba5.rowconfigure(x, weight=1)
        arriba5.columnconfigure(x, weight=1)
def doble_click2(event):
    global values
    item = tree_materias.selection()
    if item:
        values = tree_Profe.item(item, "values")
        materia_nombre.delete(0, tk.END)
        materia_nombre.insert(0, values[1])
        variable1.set(values[2])
        variable2.set(values[3])
        variable3.set(values[4])
def actualizar_division(*args):
    global opciones_division
    año_seleccionado = variable1.get()
    variable2.set("")
    if año_seleccionado <= 3:
        opciones_division = opciones_division1
    else:
        opciones_division = opciones_division2
    # Actualiza el menú desplegable de división con las nuevas opciones
    menu_division = division["menu"]
    menu_division.delete(0, "end")
    for opcion in opciones_division:
        menu_division.add_command(label=opcion, command=lambda value=opcion: variable2.set(value))  
    cerrar_base_de_datos()
    
def reemplazar_espacios(event):
    texto = materia_nombre.get()
    texto_modificado = texto.replace(' ', '_')
    materia_nombre.delete(0, tk.END)  # Borra el contenido actual
    materia_nombre.insert(0, texto_modificado)
    


def opciones_docentes(option):
    conectar_base_de_datos()
    if option==3:
        codigo_area = c_a.get()
        telefono1 = entry_telefono.get()
        telefono2 = entry_telefono2.get()

        # Limpia los valores de los teléfonos de espacios y caracteres no deseados
        codigo_area = codigo_area.strip()
        telefono1 = telefono1.strip()
        telefono2 = telefono2.strip()
        
        obtenernombre=añadir_nombre.get()
        obtenerapellido=añadir_apellido.get()
        obtenertelefono= f"{codigo_area} {telefono1} {telefono2}"
        obtenerdni=entry_dni.get()
        obtenertipodni = variable4.get()
        obtenercorreo=entry_correo.get()
        obtenerdireccion=entry_direccion.get()
        obteneraltura=entry_Altura.get()
        obtenerfecha=entry_fecha.get()
        obtenerdpto=f"Piso {piso.get()}" + " " + departamento.get()

        
        
    
        if check_var.get() == 1:
            if not obtenernombre or not obtenerapellido or not obtenertelefono or not obtenerdni or not obtenercorreo or not obtenerdireccion or not obtenerfecha  or not obtenertipodni:
                messagebox.showerror("Error", "Debe ingresar todos los datos.")
                return False
        else:
            if not obtenernombre or not obtenerapellido or not obtenertelefono or not obtenerdni or not obtenercorreo or not obtenerdireccion or not obteneraltura or not  obtenerfecha or not obtenertipodni:
                messagebox.showerror("Error", "Debe ingresar todos los datos.")
                return False
        
        select_query = "SELECT * FROM profesores WHERE Nombre = %s AND Apellido = %s AND Telefono= %s AND Nro_de_documento = %s AND Tipo_documento = %s AND Correo = %s AND Direccion = %s AND Altura = %s AND Departamento = %s AND Fecha_nacimiento = %s"
        data_verificar = (obtenernombre, obtenerapellido,obtenertelefono,obtenerdni,obtenertipodni,obtenercorreo,obtenerdireccion,obteneraltura,obtenerdpto,obtenerfecha)
                
        cursor = cnx.cursor()
        cursor.execute(select_query, data_verificar)
        existing_row = cursor.fetchone()
            
        if existing_row:
            messagebox.showerror("Error", "La fila ya existe en la base de datos.")
            return     
                
                # Crear la sentencia SQL de inserción
        insert_query = "INSERT INTO profesores (Nombre, Apellido, Telefono, Tipo_documento,Nro_de_documento, Correo, Direccion,Altura, Departamento, Fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
        dataagregar = (obtenernombre, obtenerapellido, obtenertelefono,obtenertipodni, obtenerdni,obtenercorreo, obtenerdireccion,obteneraltura, obtenerdpto, obtenerfecha)  
        agregar_numero()        
        cursor = cnx.cursor()
        
        cursor.execute(insert_query, dataagregar)
        cnx.commit() # Importante: Confirmar los cambios en la base de datos
        last_id = cursor.lastrowid
        messagebox.showinfo("Aviso", "Profesor agregado correctamente")
        tree_Profe.insert(parent='', index='end', values=(last_id,obtenernombre, obtenerapellido, obtenertelefono, obtenertipodni, obtenerdni,obtenercorreo, obtenerdireccion,obteneraltura, obtenerdpto, obtenerfecha)) 
        borrar_entrys()
        division.set(opciones_documento[0])
        cerrar_base_de_datos()       
    elif option == 4:
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar estos datos?")
        if respuesta:
            conectar_base_de_datos()
            eleccion = tree_Profe.selection()
            if not eleccion:
                messagebox.showerror("Error", "Seleccione al menos un aula")
            else:
                try:
                    cursor = cnx.cursor()
                    for ele in eleccion:
                        profes_id = tree_Profe.item(ele, "values")[0]
                        cursor.execute("DELETE FROM profesores WHERE Id_profesor = %s",(profes_id,))
                        tree_Profe.delete(ele)
                    cnx.commit()
                    cursor.close()
                    if len(eleccion) == 1:
                        messagebox.showinfo("Profesor", "Profesor eliminado")
                    else:
                        messagebox.showinfo("Profesores", f"{len(eleccion)} profesores eliminados exitosamente")
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error al eliminar: {str(e)}")
                finally:
                    cerrar_base_de_datos()
    elif option == 5:
        conectar_base_de_datos()
        obtenernombre=materia_nombre.get()
        obteneraño = variable1.get()
        obtenerdivision = variable2.get()
        obtenergrupo = variable3.get()
        obtenerespecialidad = entry_especialidad.get()
        if not obtenernombre or not obtenerdivision:
            messagebox.showerror("Error", "Debe ingresar todos los datos.")
            return False
     
        if obteneraño in [1,2, 3] and obtenerespecialidad:
            messagebox.showerror("Error", "La especialidad es solo para opciones de ciclo superior.")
            return False
        else:
            if obteneraño in [4,5,6,7] and not obtenerespecialidad:
                messagebox.showerror("Error", "La especialidad es obligatoria para opciones de ciclo superior.")
                return False
        
        select_query = "SELECT * FROM espacio_curricular WHERE nombre_materia = %s AND año = %s AND division = %s AND Grupo = %s AND Especialidad = %s"
        data_verificar = (obtenernombre,obteneraño,obtenerdivision,obtenergrupo, obtenerespecialidad)
                
        cursor = cnx.cursor()
        cursor.execute(select_query, data_verificar)
        existing_row = cursor.fetchone()
            
        if existing_row:
            messagebox.showerror("Error", "La fila ya existe en la base de datos.")
            return     
                
                # Crear la sentencia SQL de inserción
        insert_query = "INSERT INTO espacio_curricular (nombre_materia, año, division, Grupo, Especialidad) VALUES (%s, %s, %s, %s, %s)"
        dataagregar = (obtenernombre,obteneraño,obtenerdivision,obtenergrupo, obtenerespecialidad)
        cursor = cnx.cursor()
        cursor.execute(insert_query, dataagregar)
        cnx.commit()  # Importante: Confirmar los cambios en la base de datos
        messagebox.showinfo("Aviso", "Materia agregada correctamente") 
        tree_materias.insert(parent='', index='end', values=(obtenernombre,obteneraño,obtenerdivision,obtenergrupo,obtenerespecialidad))
        materia_nombre.delete(0, tk.END)
        cerrar_base_de_datos()
    elif option == 6:
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar estos datos?")
        if respuesta == True:
            conectar_base_de_datos()
            eleccion = tree_materias.selection()
            if not eleccion:
                messagebox.showerror("Error", "Seleccione al menos una materia")
            else:
                try:
                    cursor = cnx.cursor()
                    for ele in eleccion:
                        obtenernombremateria = tree_materias.item(ele, 'values')[0]
                        cursor.execute("DELETE FROM espacio_curricular WHERE nombre_materia = %s", (obtenernombremateria,))
                        tree_materias.delete(ele)
                    
                    cnx.commit()  # Importante: Confirmar los cambios en la base de datos
                    cursor.close()

                    if len(eleccion) == 1:
                        messagebox.showinfo("Materia", "Materia eliminada")
                    else:
                        messagebox.showinfo("Materias eliminadas", f"{len(eleccion)} materias eliminadas exitosamente")
                    
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error al eliminar: {str(e)}")
                finally:
                    cerrar_base_de_datos()
    elif option == 7:
        codigo_area = c_a.get()
        telefono1 = entry_telefono.get()
        telefono2 = entry_telefono2.get()

        # Limpia los valores de los teléfonos de espacios y caracteres no deseados
        codigo_area = codigo_area.strip()
        telefono1 = telefono1.strip()
        telefono2 = telefono2.strip()
        
        obtenernombre=añadir_nombre.get()
        obtenerapellido=añadir_apellido.get()
        obtenertelefono= f"{codigo_area} {telefono1} {telefono2}"
        obtenerdni=entry_dni.get()
        obtenertipodni = variable4.get()
        obtenercorreo=entry_correo.get()
        obtenerdireccion=entry_direccion.get()
        obteneraltura=entry_Altura.get()
        obtenerfecha=entry_fecha.get()
        obtenerdpto=f"Piso {piso.get()}" + " " + departamento.get()
       

        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de modificar estos datos?")
        if respuesta == True:
            conectar_base_de_datos()
            eleccion = tree_Profe.selection()
            if check_var.get() == 1:
                if not obtenernombre or not obtenerapellido or not obtenertelefono or not obtenerdni or not obtenercorreo or not obtenerdireccion or not obtenertipodni:
                    messagebox.showerror("Error", "Debe ingresar todos los datos.")
                    return False
            else:
                if not obtenernombre or not obtenerapellido or not obtenertelefono or not obtenerdni or not obtenercorreo or not obtenerdireccion or not obteneraltura  or not obtenertipodni:
                    messagebox.showerror("Error", "Debe ingresar todos los datos.")
                    return False
            if not eleccion:
                 messagebox.showerror("Error", "Elija por lo menos una fila de la tabla apretando doble click.")
                 return False
            else:
                try:
            
                    
                    # Verificar si se han realizado cambios
                    if obtenernombre == values[1] and obtenerapellido == values[2] and obtenertelefono == values[3] and obtenerdni == values[5] and obtenertipodni == values[4] and obtenercorreo == values[6] and obtenerdireccion == values[7] and obteneraltura == values[8] and obtenerdpto == values[9] and obtenerfecha == values[10]:
                        messagebox.showerror("Error", "No ha modificado ningún dato.") 
                        return False
                    else:
                        cursor = cnx.cursor()
                        profes_id = tree_Profe.item(eleccion, "values")[0]
                        cursor.execute("UPDATE profesores SET Nombre = %s, Apellido = %s, Telefono = %s, Tipo_documento = %s,Nro_de_documento = %s, Correo = %s, Direccion = %s, Altura = %s,Departamento = %s, Fecha_nacimiento = %s WHERE Id_profesor = %s",(obtenernombre, obtenerapellido, obtenertelefono, obtenertipodni,obtenerdni, obtenercorreo, obtenerdireccion,obteneraltura,obtenerdpto,obtenerfecha ,profes_id))
                        cnx.commit()
                        cursor.close()
                        messagebox.showinfo("Éxito", "Los datos se han actualizado correctamente.")
                        tree_Profe.item(eleccion, values=(profes_id,obtenernombre, obtenerapellido, obtenertelefono, obtenertipodni,obtenerdni, obtenercorreo, obtenerdireccion,obteneraltura,obtenerdpto,obtenerfecha))
                except Exception as e:
                    messagebox.showerror("Error", "Se produjo un error al actualizar los datos: " + str(e))
   
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
    
def volver_al_menu(ventana):
    print("volver")
def volver_docentes(ventana):
    eliminar(ventana)
    botones_docentes(ventana)
def flecha_arriba(event, anterior_entry): 
    anterior_entry.focus_set()
def procesar_enter(event, next_entry):
    next_entry.focus_set()



if __name__ == "__main__":
    ventana = tk.Tk()
    botones_docentes(ventana)
    ventana.mainloop()