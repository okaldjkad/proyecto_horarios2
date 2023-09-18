
import tkinter as tk
import mysql.connector
from Parte_Agustin_tobias import pantalla_de_administrador
from Parte_Javi_Alejo import reset_button
from Funcionalidad_parte_principal import añadir_horario
from Pestaña_filtro import Pestaña_filtro
from tkinter import messagebox,ttk
from PDF import PDF
from PIL import ImageTk, Image
import Aulas
import Profesores
import eliminar_usuario
#Contribuciones de: Javier Correa, Tobias Bonanno, Valentino Signorello, Ariela Faivisovich
def inicializar():
    global imagen_horario,imagen_filtrar,MAX_INTENTOS
    imagen_filtrar=None
    imagen_horario=None
    MAX_INTENTOS = 3
    ventana_login()
def ventana_login():
    global ventana_inicio,intentos_restantes,user_entry,password_entry
    intentos_restantes = MAX_INTENTOS
    ventana_inicio = tk.Tk()
    ventana_inicio.title("Inicio de Sesión")
    ventana_inicio.geometry("600x460")
    ventana_inicio.minsize(600, 460)
    ventana_inicio.iconbitmap("Imagenes/Colegio_logo.ico")
    logo_imagen(ventana_inicio)
    
    label_login = ttk.LabelFrame(ventana_inicio, text="Inicio de Sesión")
    label_login.grid(row=0, column=1,pady=50,sticky="nsew",padx=(0,14))
    ventana_inicio.columnconfigure(0, weight=1)
    ventana_inicio.columnconfigure(1, weight=1)
    ventana_inicio.rowconfigure(0, weight=1)
    label_login.columnconfigure(0, weight=1)
    label_login.rowconfigure((0,1,2,3,4), weight=1)
    
    ttk.Label(label_login, text="Usuario",anchor="center").grid(row=0, column=0,pady=5,sticky="ew")
    user_entry = ttk.Entry(label_login,)
    user_entry.grid(row=1, column=0,pady=5,sticky="ew",padx=20)
    user_entry.bind('<Return>', lambda event: procesar_enter(event,password_entry))
    
    user_entry.focus_set()
    ttk.Label(label_login, text="Contraseña",anchor="center").grid(row=2, column=0,pady=5,sticky="ew")
    password_entry = ttk.Entry(label_login,show="●")
    password_entry.grid(row=3, column=0,pady=5,sticky="ew",padx=20)
    
    ttk.Button(label_login, text="Iniciar Sesión", command=iniciar_sesion).grid(row=4, column=0,pady=5,sticky="ewn",padx=20)
    password_entry.bind('<Return>', lambda event: presionar_enter(event,iniciar_sesion))
    password_entry.bind("<Up>", lambda event: flecha_arriba(event, user_entry))
    ventana_inicio.bind("<Escape>", lambda event: salir_programa(ventana_inicio))
    ventana_inicio.protocol("WM_DELETE_WINDOW",lambda: salir_programa(ventana_inicio))
    ventana_inicio.mainloop()
def primer_menu():
    global ventana_menu,imagen_filtrar,imagen_horario,imagen_usuario,imagen_aulas,imagen_profesor,imagen_logo,frame_menu
    
    ventana_menu = tk.Tk()
    ventana_menu.title("Menu")
    frame_menu = ttk.LabelFrame(ventana_menu, text="Menu principal")
    frame_menu.grid(sticky="ewns", pady=(0,40), padx=15,column=0,row=1)
    
    imagen_filtrar = ImageTk.PhotoImage(Image.open("Imagenes/Filtrar.png").resize((20, 20)))
    imagen_horario = ImageTk.PhotoImage(Image.open("Imagenes/Horario.png").resize((20, 20)))
    imagen_usuario = ImageTk.PhotoImage(Image.open("Imagenes/usuario.png").resize((20, 20)))
    imagen_aulas = ImageTk.PhotoImage(Image.open("Imagenes/Aulas.png").resize((20, 20)))
    imagen_profesor = ImageTk.PhotoImage(Image.open("Imagenes/profesor.png").resize((20, 20)))
    imagen_logo = ImageTk.PhotoImage(Image.open("Imagenes/Colegio_logo.png").resize((130, 160)))
    
    frame_menu.columnconfigure((0,1,2,3), weight=1)
    frame_menu.rowconfigure((0,1), weight=1)
    ventana_menu.columnconfigure(0, weight=1)
    ventana_menu.rowconfigure((0,1), weight=1)
    
    ttk.Label(ventana_menu, image=imagen_logo,anchor="center").grid(column=0, row=0,sticky="nsew",padx=1,pady=1)
    ttk.Button(frame_menu, text="Aulas",image=imagen_aulas,compound="left", command=lambda:eliminar_menu(aulas)).grid(column=0, row=0,sticky="nsew",padx=1,pady=1)
    ttk.Button(frame_menu, text="Profesores y materias", command=lambda:eliminar_menu(docentes)).grid(column=1, row=0, columnspan=2,sticky="nsew",padx=1,pady=1)
    ttk.Button(frame_menu, text="Horarios",image=imagen_horario,compound="left", command=lambda:eliminar_menu(horarios)).grid(column=3, row=0,sticky="nsew",padx=1,pady=1)
    ttk.Button(frame_menu, text="Usuarios", image=imagen_usuario,compound="left",command=lambda:eliminar_menu(usuarios)).grid(column=0, row=1, columnspan=2,sticky="nsew",padx=1,pady=1)
    ttk.Button(frame_menu, text="Filtros",image=imagen_filtrar,compound="left",command=lambda:eliminar_menu(filtros)).grid(column=2, row=1, columnspan=2,sticky="nsew",padx=1,pady=1)
    
    ventana_menu.protocol("WM_DELETE_WINDOW",lambda: salir_programa(ventana_menu))
    ventana_menu.bind("<Escape>", lambda event: salir_programa(ventana_menu))    
def eliminar_menu(funcion):
   ventana_menu.destroy()
   funcion() 
    
def filtros():
    global ventana5
    ventana5 = tk.Tk()
    ventana5.title("Pantalla Principal")
    ventana5.iconbitmap("Imagenes/Colegio_logo.ico")
    
    ventana5.columnconfigure(0, weight=1)
    ventana5.columnconfigure((0,1,2), weight=1)
    perfiles_frame = ttk.LabelFrame(ventana5,text="filtros")
    perfiles_frame.grid(sticky="ew", pady=2, padx=2,column=0,row=0)
    ttk.Button(perfiles_frame, text="Volver", command=lambda: volver_al_menu(ventana5)).grid(row=0, column=0, padx=2, pady=2)
    ttk.Button(perfiles_frame, text="Filtrar por curso", command=curso_botones_filtro).grid(row=1, column=0, padx=2, pady=2)
    ttk.Button(perfiles_frame, text="Filtrar por profesor", command=filtro_profesor).grid(row=2, column=0, padx=2, pady=2)
    ttk.Button(perfiles_frame, text="Filtrar por dia", command=filtro_dia).grid(row=3, column=0, padx=2, pady=2)
def curso_botones_filtro():
    global ventana6
    ventana6 = tk.Toplevel()
    ventana6.title("Pantalla Principal")
    ventana6.iconbitmap("Imagenes/Colegio_logo.ico")
    ttk.Button(ventana6, text="Ciclo basico", command=lambda: filtro_curso(0)).grid(row=1, column=0, padx=2, pady=2)
    ttk.Button(ventana6, text="Ciclo superior", command=lambda: filtro_curso(1)).grid(row=2, column=0, padx=2, pady=2)
def filtro_curso(ciclo):
    if ciclo==0:
        ventana5.destroy()
        ventana_filtro = tk.Tk()
        ventana_horario2= Pestaña_filtro(ventana_filtro)
        ventana_horario2.widgets()
        ventana_horario2.agregar_ciclo_basico()
        ventana_horario2.treeview_filter()
        ventana_horario2.ejecutar()
    elif ciclo==1:
        ventana5.destroy()
        ventana_filtro = tk.Tk()
        ventana_horario2= Pestaña_filtro(ventana_filtro)
        ventana_horario2.widgets()
        ventana_horario2.agregar_ciclo_superior()
        ventana_horario2.treeview_filter()
        ventana_horario2.ejecutar()
def filtro_profesor():
    ventana5.destroy()
    ventana_filtro1 = tk.Tk()
    ventana_horario4= Pestaña_filtro(ventana_filtro1)
    ventana_horario4.widgets()
    ventana_horario4.agregar_profesor()
    ventana_horario4.treeview_filter()
    ventana_horario4.ejecutar()
def filtro_dia():
    ventana5.destroy()
    ventana_filtro = tk.Tk()
    ventana_horario3= Pestaña_filtro(ventana_filtro)
    ventana_horario3.widgets()
    ventana_horario3.agregar_dia()
    ventana_horario3.treeview_filter()
    ventana_horario3.ejecutar()
def aulas():
    try:
        Aulas.botones_aulas()
    except:
        pass  
        Aulas.botones_aulas()
def volver_aulas(ventana):
    ventana.destroy()
    aulas()        
        

def usuarios():
    global ventana2,imagen_añadir,imagen_eliminar
    ventana2 = tk.Tk()   
    ventana2.geometry("800x600")
    ventana2.title("Pantalla Principal")
    ventana2.iconbitmap("Imagenes/Colegio_logo.ico")
    
    ventana2.columnconfigure(0, weight=1)
    ventana2.rowconfigure(0, weight=1)
    ventana2.rowconfigure(1, weight=1)
    ventana2.rowconfigure(2, weight=1)
    perfiles_frame = ttk.LabelFrame(ventana2,text="usuarios")
    imagen_añadir = ImageTk.PhotoImage(Image.open("Imagenes/Añadir-usuario.png").resize((20, 20)))
    imagen_eliminar = ImageTk.PhotoImage(Image.open("Imagenes/Eliminar.png").resize((20, 20)))

    perfiles_frame.grid(sticky="new", column=0,row=1)
    perfiles_frame.columnconfigure(0, weight=1)
    perfiles_frame.columnconfigure(1, weight=1)
    perfiles_frame.columnconfigure(2, weight=1)
    perfiles_frame.rowconfigure(0, weight=1)
    perfiles_frame.rowconfigure(1, weight=1)
    perfiles_frame.rowconfigure(2, weight=1)
    
    ttk.Button(ventana2, text="Volver", command=lambda: volver_al_menu(ventana2)).grid(row=0, column=0, padx=2, pady=2)    
        # crear las opciones del menú
    ttk.Button(perfiles_frame, text="Restablecer Contraseña", command=restablecer_boton).grid(row=1, column=0, padx=2, pady=2,sticky="ew")
        

    ttk.Button(perfiles_frame, text="Modificar nombre de usuario", command=modificar_usuario).grid(row=0, column=1, padx=2, pady=2,sticky="ew")
        

    ttk.Button(perfiles_frame, text="Agregar usuario",image=imagen_añadir,compound="left", command=agregar_usuario).grid(row=0, column=2, padx=2, pady=2,sticky="ew")

    ttk.Button(perfiles_frame, text="Ver usuarios", command= lambda: ver_aula(("Usuario", "Contraseña", "Admin"), "SELECT Usuario, Contraseña, Admin FROM usuarios")).grid(row=0, column=0, padx=2, pady=2,sticky="ew")
    
    ttk.Button(perfiles_frame, text="Eliminar Usuarios",image=imagen_eliminar,compound="left", command=eliminar_usuario.eliminar_usuarios2).grid(row=0, column=3, padx=2, pady=2, sticky="ew")


    

def docentes():
    try:
        Profesores.botones_docentes()
    except:
        pass  
        Profesores.botones_docentes()
def volver_docentes(ventana):
    ventana.destroy()
    docentes()

def horarios():
    global ventana4,imagen_eliminar,imagen_PDF,imagen_agregar
    ventana4 = tk.Tk()
    ventana4.title("Pantalla Principal")
    ventana4.iconbitmap("Imagenes/Colegio_logo.ico")
    ventana4.columnconfigure(0, weight=1)
    ventana4.rowconfigure((0,1,2), weight=1)
    frame_horarios = ttk.LabelFrame(ventana4, text="Horarios")
    frame_horarios.grid(sticky="news", pady=2, padx=2,column=0,row=3)
    imagen_eliminar = ImageTk.PhotoImage(Image.open("Imagenes/eliminar.png").resize((20,20)))
    imagen_PDF = ImageTk.PhotoImage(Image.open("Imagenes/PDF.png").resize((20,20)))
    imagen_agregar =ImageTk.PhotoImage(Image.open("Imagenes/añadir.png").resize((20,20)))
    frame_horarios.columnconfigure((0,1,2), weight=1)
    frame_horarios.rowconfigure((0,1,2), weight=1)
    ttk.Button(ventana4, text="Volver", command=lambda: volver_al_menu(ventana4)).grid(row=0, column=0, padx=2, pady=2)
    ttk.Button(frame_horarios, text="Ver horarios Laboratorios", command=lambda:opcion_ver_horarios("Laboratorio",ver_horarios)).grid(row=0, column=0, padx=2, pady=2,sticky="ew")
    
    ttk.Button(frame_horarios, text="Añadir Horarios Laboratorios",image=imagen_agregar,compound="left",command=lambda:opcion_ver_horarios("Laboratorio",añadir_aula)).grid(row=0, column=1, padx=2, pady=2,sticky="ew")
      
    ttk.Button(frame_horarios, text="Exportar laboratorio a PDF",image=imagen_PDF,compound="left", command=lambda:opcion_ver_horarios("Laboratorio",exportar_pdf)).grid(row=0, column=3, padx=2, pady=2,sticky="ew")
    
    ttk.Button(frame_horarios, text="Ver horarios aulas", command=lambda:opcion_ver_horarios("Aula",ver_horarios)).grid(row=1, column=0, padx=2, pady=2,sticky="ew")
        
        
    ttk.Button(frame_horarios, text="Añadir horarios horarios aulas",image=imagen_agregar,compound="left",command=lambda:opcion_ver_horarios("Aula",añadir_aula)).grid(row=1, column=1, padx=2, pady=2,sticky="ew")
        
        
    ttk.Button(frame_horarios, text="Exportar aula a PDF", image=imagen_PDF,compound="left",command=lambda:opcion_ver_horarios("Aula",exportar_pdf)).grid(row=1, column=3, padx=2, pady=2,sticky="ew")
    
    ttk.Button(frame_horarios, text="Ver horarios talleres", command=lambda:opcion_ver_horarios("Taller",ver_horarios)).grid(row=2, column=0, padx=2, pady=2,sticky="ew")
        
        
    ttk.Button(frame_horarios, text="Añadir horarios talleres",image=imagen_agregar,compound="left",command=lambda:opcion_ver_horarios("Taller",añadir_aula)).grid(row=2, column=1, padx=2, pady=2,sticky="ew")
        
    # Asignar la función cerrar_ventana al evento de cerrar la ventana principal
    ttk.Button(frame_horarios,text="Exportar taller a PDF",image=imagen_PDF,compound="left", command=lambda:opcion_ver_horarios("Taller",exportar_pdf)).grid(row=2, column=3, padx=2, pady=2,sticky="ew")
    ventana4.protocol("WM_DELETE_WINDOW",lambda: volver_al_menu(ventana4))
def volver_al_menu(ventana):
    ventana.destroy()
    primer_menu()
def exportar_pdf(numero_aula2,tipo_de_aula1):
    pdf1=PDF(tipo_de_aula1,numero_aula2)
    pdf1.guardar_pdf()
    messagebox.showinfo("Exportar a PDF","PDF Exportado con exito al directorio de descargas")
    

def opcion_ver_horarios(tipo_aula,segunda_funcion):
    global aula_ver_horarios
    aula_ver_horarios= tk.Toplevel()
    aula_ver_horarios.title("Pantalla Principal")
    aula_ver_horarios.iconbitmap("Imagenes/Colegio_logo.ico")
    botones_frame = ttk.LabelFrame(aula_ver_horarios, text="Horarios")
    botones_frame.pack(padx=10, pady=10)
    conectar_base_de_datos()
    cursor.execute('SELECT Tipo_de_aula, Numero FROM Aulas WHERE Tipo_de_aula = %s ORDER BY Numero ', (tipo_aula,))
    filas = cursor.fetchall()
    for i, fila in enumerate(filas):
        boton = ttk.Button(botones_frame, text=f"{tipo_aula} {fila[1]}", command=lambda r=fila[1]: segunda_funcion(r, tipo_aula))
        boton.grid(row=i // 3, column=i % 3, padx=10, pady=10)
    
def ver_horarios(numero,tipo_aula):
    ventana4.destroy()
    ventana_horario = tk.Tk()
    ventana_horario2= añadir_horario(ventana_horario,tipo_aula,numero)
    ventana_horario2.treeview()
    ventana_horario2.ejecutar()

def añadir_aula(numero,tipo_aula):
    ventana4.destroy()
    ventana_horario = tk.Tk()
    ventana_horario2= añadir_horario(ventana_horario,tipo_aula,numero)
    ventana_horario2.widgets()
    ventana_horario2.botones()
    ventana_horario2.ejecutar()

    
def modificar_usuario():
    ventana=tk.Tk()
    pantalla_de_administrador(ventana)
def restablecer_boton():
    ventana= tk.Tk()
    reset_button1 = reset_button(ventana)
    
    
def agregar_usuario():
    global contraseña_check, entrada_int, entrada_contraseña
    ventana_agregar_usuario= tk.Toplevel()
    ventana_agregar_usuario.iconbitmap("Imagenes/Colegio_logo.ico")
    ventana_agregar_usuario.title("Pantalla De Añadir")
    # Configuramos la imagen del logo del administrador y ademas configuramos un label con la imagen y otro con los widgets
    logo_imagen(ventana_agregar_usuario)
    frame_agregar_usuario = ttk.LabelFrame(ventana_agregar_usuario, text="Pantalla De Añadir", padding=(20, 10))
    frame_agregar_usuario.grid(row=1, column=0, padx=(70), pady=(10), sticky="nsew")
    #Configuramos las columnas y filas
    ventana_agregar_usuario.columnconfigure(0, weight=1)
    ventana_agregar_usuario.rowconfigure(1, weight= 3)
    ventana_agregar_usuario.rowconfigure(0, weight=1)
    frame_agregar_usuario.columnconfigure(0, weight=1)
    frame_agregar_usuario.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13),weight=1)
    global entrada_usuario, entrada_contraseña, entrada_apellido, entrada_nombre, entrada_email, entrada_cuil, es_admin
    es_admin = tk.IntVar()
    #Añadimos y Configuramos los botones del frame administrador
    ttk.Label(frame_agregar_usuario, text="Usuario").grid(row=0, column=0,pady=5,sticky="ew")
    entrada_usuario = ttk.Entry(frame_agregar_usuario)
    entrada_usuario.grid(row=1, column=0,pady=5,sticky="ew")
    entrada_usuario.bind('<Return>', lambda event: procesar_enter(event,entrada_contraseña))
    entrada_usuario.focus_set()
    ttk.Label(frame_agregar_usuario, text="Contraseña:").grid(row=2, column=0,pady=5,sticky="ew")
    
    entrada_contraseña = ttk.Entry(frame_agregar_usuario, show="●")
    entrada_int = tk.IntVar()
    entrada_contraseña.grid(row=3, column=0,pady=5,sticky="ew")
    entrada_contraseña_check = ttk.Checkbutton(frame_agregar_usuario, variable=entrada_int, command=ver_contraseña).grid(row=3, column=1,pady=5,sticky="ew")
    entrada_contraseña.bind("<Up>", lambda event: flecha_arriba(event,entrada_usuario))

    
    ttk.Checkbutton(frame_agregar_usuario, text="Es administrador", variable=es_admin).grid(row=12, column=0,pady=5,sticky="ew")
    ttk.Button(frame_agregar_usuario, text="Añadir datos", command=añadir_credenciales).grid(row=13, column=0,pady=(1,10),sticky="ew",padx=40)
    ventana_agregar_usuario.bind("<Escape>", lambda event: salir_programa(ventana_agregar_usuario))
    ventana_agregar_usuario.protocol("WM_DELETE_WINDOW",lambda: salir_programa(ventana_agregar_usuario))

def ver_contraseña():
        if entrada_int.get() == 1:
            entrada_contraseña.config(show="")
        else:
            entrada_contraseña.config(show="●") 

def opciones(option):
    Aulas.opciones_aula(option)
    Profesores.opciones_docentes(option)
def agregar_aulas(columnas_aula,query):
    Aulas.agregar_aulas(columnas_aula,query)
    
def eliminar_aulas(columnas_aula,query):
    Aulas.eliminar_aulas(columnas_aula,query)

def agregar_profesores(columnas_aula,query):
    Profesores.agregar_profesores(columnas_aula,query)    
def agregar_materias(columnas_aula,query):
    Profesores.agregar_materias(columnas_aula,query)
def modificar_profesores(columnas_aula,query):
    Profesores.modificar_profesores(columnas_aula,query)

def mostrar_ventana_aulas():
    pass

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

    
def añadir_credenciales():
    usuario_agregar = entrada_usuario.get()
    contrasena_agregar = entrada_contraseña.get()
    admin = es_admin.get()
    conectar_base_de_datos()
    
    if not entrada_contraseña or not entrada_usuario:
        messagebox.showerror("Error", "Rellena todos los campos")
        return False
    
     # Verificar si el usuario ya existe
    cursor.execute("SELECT Usuario FROM usuarios WHERE Usuario = %s", (usuario_agregar,))
    usuario_existente = cursor.fetchone()
    
    if usuario_existente:
        messagebox.showerror("Error", "El usuario ya existe")
        return False 
    
    cursor.execute("INSERT INTO usuarios (Usuario,Contraseña, Admin) VALUES (%s, %s, %s)", (usuario_agregar, contrasena_agregar,admin))
            
    cnx.commit()    
    entrada_usuario.delete(0, tk.END)
    entrada_contraseña.delete(0, tk.END)
    messagebox.showinfo("Informacion","Usuario agregado correctamente.")
    cerrar_base_de_datos()

def iniciar_sesion():
    global intentos_restantes, ventana
    # Verificar la informacion del usuario
    usuario_sesion = user_entry.get()
    contrasena_sesion = password_entry.get()
    global administrador_contador
    administrador_contador=0
    conectar_base_de_datos()
    cursor.execute("SELECT * FROM usuarios WHERE Usuario = %s AND Contraseña = %s", (usuario_sesion, contrasena_sesion))
    resultado = cursor.fetchone()
    if resultado is not None and resultado[2]==1:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión de administrador exitoso.")
        administrador_contador=+1
        # Destruir la ventana de inicio de sesión y mostrar la ventana principal
        ventana_inicio.destroy()
        cerrar_base_de_datos()
        primer_menu()

    elif resultado is not None and usuario_sesion in resultado and contrasena_sesion in resultado:
        # Mostrar mensaje de inicio de sesión exitoso
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
        # Destruir la ventana de inicio de sesión y mostrar la ventana principal
        ventana_inicio.destroy()
        cerrar_base_de_datos()
        primer_menu()

    else:
        intentos_restantes -= 1
        if intentos_restantes > 0:
            messagebox.showerror("Inicio de Sesión", f"Credenciales inválidas. Te quedan {intentos_restantes} intentos.")
            password_entry.delete(0, tk.END)  # Borrar el campo de contraseña
            user_entry.delete(0, tk.END)
            cerrar_base_de_datos()
        else:
            messagebox.showerror("Inicio de Sesión", "Has agotado los intentos permitidos.")
            cerrar_ventana(ventana_inicio)
            ventana_inicio.protocol("WM_DELETE_WINDOW", ventana_inicio.destroy())
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
def logo_imagen(ventana):
    imagen_logo = ImageTk.PhotoImage(Image.open("Imagenes/Colegio_logo.png").resize((110, 140)))
    label_logo = ttk.Label(ventana, image=imagen_logo)
    label_logo.image = imagen_logo  # Almacenar la imagen en el widget para evitar que se elimine
    label_logo.grid(row=0, column=0, pady=10, padx=10)

def presionar_enter(event,funcion):
    funcion()
def flecha_arriba(event, anterior_entry): 
    anterior_entry.focus_set()
def procesar_enter(event, next_entry):
    next_entry.focus_set()
def restablecer_contrasena():
    ventana_restablecer= tk.Toplevel()
    reset_button(ventana_restablecer)

def modificar_usuario():
    ventana_agregar = tk.Toplevel()
    pantalla_de_administrador(ventana_agregar)

def salir_programa(root):
    if messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?"):
        root.destroy()
        cnx.close()

def cerrar_ventana(root):
    root.destroy()

if __name__ == "__main__":  
    inicializar()