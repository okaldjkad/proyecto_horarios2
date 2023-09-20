#pip install mysql-connector-python
#pip install tkcalendar

#CREATE USER 'pipo'@'localhost' IDENTIFIED BY '1243';
#GRANT ALL PRIVILEGES ON *.* TO 'pipo'@'localhost'; 

try:
    from tkinter import *
    from tkinter import ttk,messagebox
    from tkcalendar import Calendar

    import mysql.connector
    from datetime import datetime
    from PIL import ImageTk, Image

except:
    print("no se encuentran librerias nesesarias")
    exit()




BGcolor="#c9daf8"  #Celeste muy claro
BG1color="#212121" #Negro
BG2color="#6D9EEB" #Celeste
BG3color="#A4C2F4" #Celeste claro
BG4color="#6FA8DC" #Cyan
BG5color="#9E9E9E" #gris claro
LS1color=""
LS2color="#F2D7D5" #rojo muy clarito



cursos = [ #Estructura: [ {AÑO}, {DIVISION}, "", {MATERIAS} ] -- Materias deben ser separadas con ";"
    ["1ro", "A", "", "Matemáticas;Literatura;Programación"],
    ["1ro", "B", "", "Matemáticas;Literatura;Programación"],
    ["1ro", "C", "", "Matemáticas;Literatura;Programación"],
    ["1ro", "D", "", "Matemáticas;Literatura;Programación"],
    ["1ro", "E", "", "Matemáticas;Literatura;Programación;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect;ect"],
    ["2do", "A", "", "Historia;Geografía;Inglés"],
    ["2do", "B", "", "Historia;Geografía;Inglés"],
    ["2do", "C", "", "Historia;Geografía;Inglés"],
    ["2do", "D", "", "Historia;Geografía;Inglés"],
    ["3ro", "A", "", "Historia;Literatura;Ciudadania"],
    ["3ro", "B", "", "Historia;Literatura;Ciudadania"],
    ["3ro", "C", "", "Historia;Literatura;Ciudadania"],
    ["3ro", "D", "", "Historia;Literatura;Ciudadania"],
    ["4to", "1ra", "", "Hardware;Salud y Adolescencia;Sistemas Operativos"],
    ["4to", "2da", "", "Hardware;Salud y Adolescencia;Sistemas Operativos"],
    ["4to", "3ra", "", "Hardware;Salud y Adolescencia;Sistemas Operativos"],
    ["4to", "4ta", "", "Hardware;Salud y Adolescencia;Sistemas Operativos"],
    ["4to", "5ta", "", "Hardware;Salud y Adolescencia;Sistemas Operativos"],
    ["4to", "6ta", "", "Hardware;Salud y Adolescencia;Sistemas Operativos"],
    ["5to", "1ra", "", "Hardware;Programacion;TeleInformatica"],
    ["5to", "2da", "", "Hardware;Programacion;TeleInformatica"],
    ["5to", "3ra", "", "Hardware;Programacion;TeleInformatica"],
    ["5to", "4ta", "", "Hardware;Programacion;TeleInformatica"],
    ["5to", "5ta", "", "Hardware;Programacion;TeleInformatica"],
    ["6to", "1ra", "", "Programacion;Analisis Matematico;Artistica"],
    ["6to", "2da", "", "Programacion;Analisis Matematico;Artistica"],
    ["6to", "3ra", "", "Programacion;Analisis Matematico;Artistica"],
    ["6to", "4ta", "", "Programacion;Analisis Matematico;Artistica"],
    ["6to", "5ta", "", "Programacion;Analisis Matematico;Artistica"],
    ["7mo", "1ra", "", "Pasantias;Programacion;Hardware"],
    #["7mo", "2da", "", "Pasantias;Programacion;Hardware"],
    ["7mo", "3ra", "", "Pasantias;Programacion;Hardware"],
    ["7mo", "4ta", "", "Pasantias;Programacion;Hardware"]
]

#Materias de ejemplo para probar el sistema
materiasEjemplo = [ #estructura: [ {Nombre Materia}, {Cursos Asignados} ]
    ["Matematicas","1ro_A;1ro_B;1ro_C;1ro_D;1ro_E"],
    ["Literatura","1ro_A;1ro_B;1ro_C;1ro_D;1ro_E"],
    ["Historia","1ro_A;1ro_B;1ro_C;1ro_D;1ro_E"],

    ["Sistemas Operativos","5to_1ra;5to_2da;5to_3ra"],
    ["Tele Informatica","5to_1ra;5to_2da;5to_3ra"],

    ["Programacion","5to_2da"],
    ["Base de datos","5to_2da"],

    ["Hardware","5to_1ra;5to_3ra"],
    ["Electronica","5to_1ra;5to_3ra"],

    ["Dibujo Tecnico","5to_4ta;5to_5ta"],
]

maestrias = [ #estructura: [ {ID Predefinida}, {Nombre Maestria} ]
    (0,"Ninguna"), #En el caso de materias de ciclo basico o materias compartidas entre maestrias
    (1,"Programacion"),
    (2,"Informatica"),
    (3,"Maestro Mayor de Obras"),
]

for curso in cursos:
    curso[2] = curso[0]+"_"+curso[1] #crear variable curso juntando año y division
    curso[2] = curso[2].lower() #se asegura que el curso sea minuscula
    curso[3] = curso[3].replace(" ","_") #reemplazar espacios con "_"









class boletines1():
    def __init__(self, tk, sql, cursor):
        #Auto Crear Base de datos
        #cursor.execute("create database if not exists tecnica_2023")
        sql.database = "tecnica_2023"

        #Tabla de maestrias para materias(por default, 1 = Programacion, 2 = Informatica, 3 = Maestro mayor)
        #removido ya que no le veo la utilidad por que los cursos de cada materia por ahora definidos manualmente
        #cursor.execute("""CREATE TABLE if not exists MAESTRIAS(
        #               ID INT PRIMARY KEY not null,
        #               MAESTRIA varchar(25) not null
        #               )""")
        

        #Tabla de materias para cursos
        #cursor.execute("""CREATE TABLE if not exists MATERIAS(
        #               ID int AUTO_INCREMENT PRIMARY KEY,
        #               MATERIA varchar(25) UNIQUE,
        #               CURSOS text
        #               )""")

        #Tabla de materias para cursos (con maestrias)
#        cursor.execute("""CREATE TABLE if not exists MATERIAS(
#                       ID int AUTO_INCREMENT PRIMARY KEY,
#                       MATERIA varchar(25) UNIQUE,
#                       CURSOS text,
#                       ID_MAESTRIA int,
#                       FOREIGN KEY (ID_MAESTRIA) REFERENCES maestrias(ID)
#                       )""")


        #Tabla de cursos
        #cursor.execute("""create table if not exists cursos(
        #               ID INT AUTO_INCREMENT PRIMARY KEY,
        #               CURSO varchar(10) UNIQUE not null,
        #               MATERIAS mediumtext
        #               );""")
        
        for materiaEj in materiasEjemplo:
            materiaEj[1] = materiaEj[1].lower()
            cursor.execute("INSERT IGNORE INTO materias(MATERIA,CURSOS) VALUES (%s,%s)",materiaEj)

            #con maestrias:
            #cursor.execute("INSERT IGNORE INTO materias(MATERIA,CURSOS,ID_MAESTRIA) VALUES (%s,%s,%s)",materiaEj)


        #Tabla de boletines para cada materia
        print("----------------")
        print("MATERIAS:")
        cursor.execute("select MATERIA from materias")
        materias = cursor.fetchall()
        for materia in materias:
            materia = materia[0].replace(" ","_")
            print(materia)
            cursor.execute(f"""CREATE TABLE if not exists boletines__{materia} (
                        ID int(11) PRIMARY KEY,
                        CURSO varchar(10) NOT NULL,
                        NOTA1 DOUBLE(4,2),
                        NOTA2 DOUBLE(4,2),
                        NOTA3 DOUBLE(4,2),
                        NOTA_DICIE DOUBLE(4,2),
                        NOTA_FEBRE DOUBLE(4,2),
                        NOTA_MARZO DOUBLE(4,2),
                        NOTA_FINAL DOUBLE(4,2),
                        FOREIGN KEY (ID) REFERENCES alumnos(ID),
                        FOREIGN KEY (CURSO) REFERENCES cursos(CURSO)
                        );""")
        print("----------------")
        
        #crear maestrias default
        #for maestria in maestrias:
        #    cursor.execute("INSERT IGNORE INTO maestrias (ID, MAESTRIA) VALUES (%s, %s)", (maestria[0], maestria[1]))

        #crear cursos default con materias de ejemplo
        for curso in cursos:
            cursor.execute("INSERT IGNORE INTO Cursos (CURSO, MATERIAS) VALUES (%s, %s)", (curso[2],curso[3]))



# ---CODIGO VIEJO PARA CREAR BASE DE DATOS---
#        cursor.execute("SELECT CURSO,MATERIAS FROM cursos")
#        fetchCursos = cursor.fetchall()
#        print(fetchCursos)
#        for fetch in fetchCursos:
#            curso = str(fetch[0])
#            if not fetch[1] is None:
#                materias = list(fetch[1].split(";"))
#                for materia in materias:
#                    database = str(curso+"__"+materia)
#                    cursor.execute(f"create table if not exists `{database}`(ID INT AUTO_INCREMENT PRIMARY key, NOMBRE varchar(50) not null, APELLIDO varchar(50) not null, GRUPO varchar(10) null, NOTA1 varchar(10) null, NOTA2 varchar(10) null, NOTA3 varchar(10) null, NOTA_DICIE varchar(10), NOTA_FEBRE varchar(10), NOTA_MARZO varchar(10), NOTA_FINAL varchar(10));")


        #print("[MATERIAS] se han creado las siguientes tablas")

        #cursor.execute("SELECT CURSO FROM `cursos`")
        #databasesPrefix = cursor.fetchall() #Obtiene la lista de todos los cursos
        #print(databasesPrefix)
        #for prefix in databasesPrefix:
        #    prefix = str(prefix[0])
        #    cursor.execute(f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'tecnica_2023' and table_name LIKE '{prefix}__%'")
        #    materias1 = cursor.fetchall() #Obtiene la lista de todas las tablas de todas las materia del curso en cuestion
        #    print(materias1)
    
    def crear(self,tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc):

        #cursor.reset()

        def volver():
            print("Func volver")

            for elemento in tk.winfo_children():
                elemento.destroy()
            menuFunc(tipoCuenta,nombreCuenta)
            return
        def validar_numeros(P):
    # Función de validación para permitir solo caracteres numéricos
            if all(c.isdigit() for c in P):
                return True
            else:
                messagebox.showerror("Error", "Solo se permiten números")
                return False
        def limite(event):
            contenido = EntryNota1.get() 
            contenido2 = EntryNota2.get()
            contenido3=EntryFebre.get()
            contenido4=EntryMarzo.get()
            contenido5= EntryDicie.get()
            contenido6=EntryCalifDef.get()
            
            if len(contenido) > 2:
                nuevo_contenido = contenido[:2]
                EntryNota1.delete(0, END)
                EntryNota1.insert(0, nuevo_contenido)
                messagebox.showerror("Error", "Solo se permiten 2 caracteres")
            elif len(contenido2) > 2:    
                nuevo_contenido1 = contenido2[:2]
                EntryNota2.delete(0, END)
                EntryNota2.insert(0, nuevo_contenido1)
                messagebox.showerror("Error", "Solo se permiten 2 caracteres")
            elif len(contenido3) > 2:
                nuevo_contenido2 = contenido3[:2]
                EntryFebre.delete(0, END)
                EntryFebre.insert(0, nuevo_contenido2)
                messagebox.showerror("Error", "Solo se permiten 2 caracteres")
            elif len(contenido4) > 2:
                nuevo_contenido3 = contenido4[:2]
                EntryMarzo.delete(0, END)
                EntryMarzo.insert(0, nuevo_contenido3)
                messagebox.showerror("Error", "Solo se permiten 2 caracteres")
            elif len(contenido5) > 2:
                nuevo_contenido4 = contenido5[:2]
                EntryDicie.delete(0, END)
                EntryDicie.insert(0, nuevo_contenido4)
                messagebox.showerror("Error", "Solo se permiten 2 caracteres")
            elif len(contenido6) > 2:
                nuevo_contenido5 = contenido6[:2]
                EntryCalifDef.delete(0, END)
                EntryCalifDef.insert(0, nuevo_contenido5)
                messagebox.showerror("Error", "Solo se permiten 2 caracteres")
        
           
            
        #tk.grid_columnconfigure(0, weight=1)

        FrameTOP = Frame(tk,bg=BGcolor)
        FrameTOP.place(relx = 0.0, rely = 0.0, anchor ='nw', relwidth=1.0, relheight=0.15)

        FrameCurso=Frame(FrameTOP, bg=BGcolor, highlightbackground=BG1color, highlightthickness=1)
        FrameCurso.place(relx = 0.0, rely = 0.5, anchor ='w', relwidth=0.5, relheight=0.8)

        FrameLabel1 = Frame(FrameCurso,bg=BG2color, highlightbackground=BG1color, highlightthickness=0.5)
        FrameLabel1.grid(row=0,column=0,columnspan=2,sticky="news")

        FrameLabel2 = Frame(FrameCurso,bg=BG2color, highlightbackground=BG1color, highlightthickness=0.5)
        FrameLabel2.grid(row=1,column=0,columnspan=2,sticky="news")


        BotonesAÑOS = []
        BotonesDIVISION = []
        AÑOS = ["1ro","2do","3ro","4to","5to","6to","7mo"]
        DIVISIONES = [(""),
                    ("A"  ,"B"  ,"C"  ,"D"  ,"E"  ," "  ," "),
                    ("A"  ,"B"  ,"C"  ,"D"  ," "  ," "  ," "),
                    ("A"  ,"B"  ,"C"  ,"D"  ," "  ," "  ," "),
                    ("1ra","2da","3ra","4ta","5ta","6ta"," "),
                    ("1ra","2da","3ra","4ta","5ta"," "  ," "),
                    ("1ra","2da","3ra","4ta","5ta"," "  ," "),
                    ("1ra"," "  ,"3ra","4ta"  ," "  ," "  ," ")]
        ColumnaAÑO = 1

        LabelAÑO = Label(FrameCurso, bg=BG2color, text="AÑO:")
        LabelDIV = Label(FrameCurso, bg=BG2color, text="DIVISION:")
        LabelAÑO.grid(row=0,column=0,columnspan=2)
        LabelDIV.grid(row=1,column=0,columnspan=2)


        FrameBotones=Frame(FrameTOP,bg=BGcolor)
        FrameBotones.place(relx = 0.52, rely = 0.5, anchor ='w', relwidth=0.48, relheight=0.8)

        FrameBotones.columnconfigure(tuple(range(0,3)), weight=1)
        FrameBotones.rowconfigure((0,1), weight=1)

        #Iconos de botones
        self.imagen_volver =ImageTk.PhotoImage(Image.open("imagenes/volver.png").resize((20, 20), Image.LANCZOS))
        self.imagen_editar =ImageTk.PhotoImage(Image.open("imagenes/editar.png").resize((15, 15), Image.LANCZOS))
        self.imagen_imprimir = ImageTk.PhotoImage(Image.open("imagenes/imprimir.png").resize((20, 20), Image.LANCZOS))

        #BotonPeticion = Button(FrameBotones, text ="Enviar Peticion",width=20)#, command = lambda: accion.actualizar(0,lista))
        BotonImprimir = Button(FrameBotones, text ="Imprimir",image=self.imagen_imprimir,compound="left",width=10)#, command = lambda: accion.actualizar(0,lista))
        BotonVolver   = Button(FrameBotones, text ="Volver",image=self.imagen_volver,compound="left",width=60, command = lambda: volver())
        BotonEditar   = Button(FrameBotones, text ="Editar Seleccionado",image=self.imagen_editar,compound="left",width=10, command = lambda: EditarLista())
        BotonImprimir["state"] = "disabled"

        if tipoCuenta==2:
            BotonEditar["state"] = "disabled"
        else:
            BotonEditar["state"] = "normal"

        LabelAlumno = Label(FrameBotones, text ="Alumno:",width=10,bg=BGcolor,anchor="e", font=("Arial", 10, "bold"))
        ComboboxAlumno = ttk.Combobox(FrameBotones, state="readonly", values=[""])

        if tipoCuenta==1:
            LabelAlumno.config(text="Materia:")

        #BotonPeticion.grid(row=0,column=0,columnspan=2,padx=4,pady=(0,1),sticky="news")
        BotonImprimir.grid(row=0,column=2,columnspan=1,padx=(4,1),pady=(0,1),sticky="news")
        BotonVolver.grid(row=0,column=3,columnspan=1,padx=(1,4),pady=(0,1),sticky="news")
        BotonEditar.grid(row=0,column=0,columnspan=2,padx=0,pady=(0,1),sticky="news")
        #BotonPeticion.grid(row=0,column=0,columnspan=2,padx=4,pady=(0,1),sticky="news")
        LabelAlumno.grid(row=1,column=1,columnspan=1,padx=0,pady=(1,0),sticky="e")
        ComboboxAlumno.grid(row=1,column=2,columnspan=2,padx=4,pady=(1,0),sticky="news")
        
        


        #BotonAlumno   = Button(FrameBotones, text ="Ingresar Alumno",width=20)#, command = lambda: accion.actualizar(0,lista))
        #BotonEliminar = Button(FrameBotones, text ="Eliminar Seleccionados",width=20, command = lambda: accion.eliminar(lista))
        #BotonAlumno.grid(row=1,column=0,columnspan=2,padx=4,pady=(1,0),sticky="news")
        #BotonEliminar.grid(row=1,column=2,columnspan=2,padx=4,pady=(1,0),sticky="news")

        #recargar = Button(FrameBotones, text ="Actualizar Lista",width=17 , command = lambda: accion.actualizar(0,lista))
        #eliminar = Button(FrameBotones, text ="Eliminar Seleccionados",width=17 , command = lambda: accion.eliminar(lista))
        #recargar.pack(side='left', expand=False)
        #eliminar.pack(side='left', expand=False)

        lista = ttk.Treeview(tk, columns=("c0","c1","c2","c3","c5","c6","c7","c8","c9"), show='headings', selectmode='extended')


        #aprobados = Button(botones, text ="Mostrar Aprobados",width=17 , command = lambda: accion.actualizar(1,lista))
        #desaprobados = Button(botones, text ="Mostrar Desaprobados",width=17 , command = lambda: accion.actualizar(2,lista))
        #desaprobados.pack(side='right', expand=False)
        #aprobados.pack(side='right', expand=False)

        if tipoCuenta==1:
            heading1="Alumno"
        else:
            heading1="Asignatura"

        lista.column("#1",anchor=CENTER, stretch=YES, width=135, minwidth=135)
        lista.column("#2",anchor=CENTER, stretch=YES, width=60, minwidth=60)
        lista.column("#3",anchor=CENTER, stretch=YES, width=60, minwidth=60)
        #lista.column("#4",anchor=CENTER, stretch=YES, width=0, minwidth=0)
        lista.column("#4",anchor=CENTER, stretch=YES, width=70, minwidth=70)
        lista.column("#5",anchor=CENTER, stretch=YES, width=75, minwidth=75)
        lista.column("#6",anchor=CENTER, stretch=YES, width=75, minwidth=75)
        lista.column("#7",anchor=CENTER, stretch=YES, width=75, minwidth=75)
        lista.column("#8",anchor=CENTER, stretch=YES, width=90, minwidth=90)
        lista.heading('#1', text=heading1) #para mas lineas de texto en el heading, agregar mas "\n"
        lista.heading('#2', text='1ra Nota')
        lista.heading('#3', text='2da Nota')
        #lista.heading('#4', text='3ra Nota')
        lista.heading("#4", text="Promedio")
        lista.heading('#5', text='Diciembre')
        lista.heading('#6', text='Febrero')
        lista.heading('#7', text='Marzo')
        lista.heading('#8', text='Calif. Definitiva')
        #lista.tag_configure("True", background=LS1color)
        lista.tag_configure("True", background=LS2color)
        lista.place(relx = 0.0, rely = 0.15, anchor ='nw', relwidth=1.0, relheight=0.78)


        #Fondo
        BG2 = Frame(tk, bg=BG2color,width=512,height=32)
        #BG1 = Frame(tk, bg=BG1color,width=80,height=256)
        #BG1.place(relx = 0.0, rely = 1.0, anchor ='sw', relwidth=0.1, relheight=1.0)
        BG2.place(relx = 0.0, rely = 1.0, anchor ='sw', relwidth=1.0, relheight=0.07)

        etiqueta_derecha = Label(BG2, text="©5to1ra Grupo A - 2023", bg=BG2color,font=("Helvetica", 16))
        etiqueta_derecha.place(relx = 1.0, rely = 0.5, anchor ='e')

        etiqueta_izquierda = Label(BG2, text="", bg=BG2color,font=("Helvetica", 16))
        etiqueta_izquierda.place(relx = 0.0, rely = 0.5, anchor ='w')

        subfix = " > Boletines"
        if tipoCuenta==1:
            etiqueta_izquierda.config(text=str("Profesor"+subfix))
        elif tipoCuenta==2:
            etiqueta_izquierda.config(text=str("Preceptor"+subfix))
        elif tipoCuenta==3:
            etiqueta_izquierda.config(text=str("Administrador"+subfix))

        ComboboxAlumno.bind("<<ComboboxSelected>>",lambda a: ObtenerLista(ultimoCurso[0],ultimoCurso[1],True))


        noAlumnos = "ERROR: No hay Alumnos"
        noMaterias = "ERROR: No hay Materias"

     
        
        def EditarLista():
            global EntryNota1, EntryNota2, EntryCalifDef, EntryMarzo, EntryFebre, EntryDicie
            print("Func EditarLista")

            filaSeleccion = lista.selection()
            print(filaSeleccion)
            if len(filaSeleccion)<=0:
                if tipoCuenta==1:
                    messagebox.showinfo(message="No se ha seleccionado\nningun alumno", title="Error")
                else:
                    messagebox.showinfo(message="No se ha seleccionado\nninguna nota", title="Error")
            elif len(filaSeleccion)>1:
                if tipoCuenta==1:
                    messagebox.showinfo(message="Seleccione solo 1 alumno", title="Error")
                else:
                    messagebox.showinfo(message="Seleccione solo 1 nota", title="Error")
            else:
                FrameEditar = Frame(FrameTOP,bg=BG3color)
                FrameEditar.place(relx = 0.0, rely = 0.5, anchor ='w', relwidth=1.0, relheight=0.8)
                FrameEditar.columnconfigure(tuple(range(0,6)), weight=1)
                FrameEditar.rowconfigure((0,1), weight=1)
                FrameBotones.place_forget() 
                FrameCurso.place_forget() 
                
                fuenteEdit=("Arial",11)


                LabelNota1 = Label(FrameEditar,text="1ra Nota", font=fuenteEdit, bg=BG3color)
                LabelNota1.grid(row=0,column=0,columnspan=1,padx=(0,0),pady=2,sticky="e")
                EntryNota1 = ttk.Entry(FrameEditar,width=4, font=fuenteEdit)
                EntryNota1.bind("<KeyRelease>", limite)
                
                EntryNota1.config(validate="key",validatecommand=(FrameEditar.register(validar_numeros), "%P"))

                EntryNota1.grid(row=0,column=1,columnspan=1,pady=2,sticky="ns")
                
                LabelNota2 = Label(FrameEditar,text="2da Nota", font=fuenteEdit, bg=BG3color)
                LabelNota2.grid(row=0,column=2,columnspan=1,padx=(16,0),pady=2,sticky="e")
                EntryNota2 = ttk.Entry(FrameEditar,width=4, font=fuenteEdit)
                EntryNota2.grid(row=0,column=3,columnspan=1,pady=2,sticky="ns")
                EntryNota2.config(validate="key",validatecommand=(FrameEditar.register(validar_numeros), "%P"))
                EntryNota2.bind("<KeyRelease>", limite)

                LabelCalifDef = Label(FrameEditar,text="Calif. Def.", font=fuenteEdit, bg=BG3color)
                LabelCalifDef.grid(row=0,column=4,columnspan=1,padx=(16,0),pady=2,sticky="e")
                EntryCalifDef = ttk.Entry(FrameEditar,width=4, font=fuenteEdit)
                EntryCalifDef.config(validate="key",validatecommand=(FrameEditar.register(validar_numeros), "%P"))
                EntryCalifDef.bind("<KeyRelease>", limite)
                EntryCalifDef.grid(row=0,column=5,columnspan=1,pady=2,sticky="ns")

                LabelDicie = Label(FrameEditar,text="Diciembre", font=fuenteEdit, bg=BG3color)
                LabelDicie.grid(row=1,column=0,columnspan=1,padx=(16,0),pady=2,sticky="e")
                EntryDicie = ttk.Entry(FrameEditar,width=4, font=fuenteEdit)
                EntryDicie.config(validate="key",validatecommand=(FrameEditar.register(validar_numeros), "%P"))
                EntryDicie.bind("<KeyRelease>", limite)
                EntryDicie.grid(row=1,column=1,columnspan=1,pady=2,sticky="ns")

                LabelFebre = Label(FrameEditar,text="Febrero", font=fuenteEdit, bg=BG3color)
                LabelFebre.grid(row=1,column=2,columnspan=1,padx=(16,0),pady=2,sticky="e")
                EntryFebre = ttk.Entry(FrameEditar,width=4, font=fuenteEdit)
                EntryFebre.config(validate="key",validatecommand=(FrameEditar.register(validar_numeros), "%P"))
                EntryFebre.bind("<KeyRelease>", limite)
                EntryFebre.grid(row=1,column=3,columnspan=1,pady=2,sticky="ns")

                LabelMarzo = Label(FrameEditar,text="Marzo", font=fuenteEdit, bg=BG3color)
                LabelMarzo.grid(row=1,column=4,columnspan=1,padx=(0,0),pady=2,sticky="e")
                EntryMarzo = ttk.Entry(FrameEditar,width=4, font=fuenteEdit)
                EntryMarzo.config(validate="key",validatecommand=(FrameEditar.register(validar_numeros), "%P"))
                EntryMarzo.bind("<KeyRelease>", limite)
                
                EntryMarzo.grid(row=1,column=5,columnspan=1,pady=2,sticky="ns")

                ErrorLabel = Label(FrameEditar,text='', font=("Arial",10), bg=BG3color, width=20)
                ErrorLabel.grid(row=0,column=6,columnspan=1,rowspan=2,pady=2,sticky="news")

                BotonConfirmar = Button(FrameEditar, text="Confirmar", command=lambda:Confirmar())
                BotonConfirmar.grid(row=0,column=7,columnspan=1,padx=(32,0),pady=2,sticky="news")

                BotonCancelar = Button(FrameEditar, text="Cancelar", command=lambda:Terminar())
                BotonCancelar.grid(row=1,column=7,columnspan=1,padx=(32,0), pady=2,sticky="news")
            
                listaSeleccion = lista.item(filaSeleccion)
                seleccion = listaSeleccion['values']
                print(seleccion)
                EntryNota1.insert(0,seleccion[1])
                EntryNota2.insert(0,seleccion[2])
                EntryDicie.insert(0,seleccion[4])
                EntryFebre.insert(0,seleccion[5])
                EntryMarzo.insert(0,seleccion[6])
                EntryCalifDef.insert(0,seleccion[7])


                def Terminar():
                    EntryNota1.delete(0,END)
                    EntryNota2.delete(0,END)
                    EntryMarzo.delete(0,END)
                    EntryFebre.delete(0,END)
                    EntryDicie.delete(0,END)
                    EntryCalifDef.delete(0,END)
                    
                    FrameEditar.place_forget() 
                    FrameBotones.place(relx = 0.52, rely = 0.5, anchor ='w', relwidth=0.48, relheight=0.8)
                    FrameCurso.place(relx = 0.0, rely = 0.5, anchor ='w', relwidth=0.5, relheight=0.8)
                    
                    ObtenerLista(ultimoCurso[0],ultimoCurso[1],True)
                    
                def Confirmar():

                    v = [EntryNota1.get(),EntryNota2.get(),EntryDicie.get(),EntryFebre.get(),EntryMarzo.get(),EntryCalifDef.get()]

                    #Validacion de las notas introducidas
                    for i in v:

                        #se fija si la informacion introducida es un numero o no
                        i.replace(",",".")
                        if i.replace(".","").isdigit()==True or i=='':
                            if i == '': #hace posible dejar notas vacias
                                v[v.index('')]="NULL"
                                

                            else:
                                i = round(float(i),2)
                                print(i)
                                if i>10 or i<0: #se asegura que la nota no sea mayor que 10 o menor que 0
                                    print("Nota fuera de rango")
                                    tk.bell()
                                    ErrorLabel.config(text="Asegurece que todas\nlas notas sean un\nnumero del 0 a 10")
                                    return
                                if i % 1 == 0:
                                    i = int(i)

                        else:
                            print(i)
                            print("Nota Invalida")
                            ErrorLabel.config(text="Asegurece que todas\nlas notas sean un\nnumero del 0 a 10")
                            tk.bell()
                            return

                        
                    print(v)


                    SQLcurso = str((ultimoCurso[1]+"_"+ultimoCurso[0]["text"]).lower())
                    print(SQLcurso)
                    print(listaSeleccion['tags'][1])

                    if tipoCuenta==1:
                        materia2=ComboboxAlumno["values"][ComboboxAlumno.current()]
                        #cursor.execute(f"UPDATE boletines__{materia2} SET NOTA1={}, NOTA2={}, NOTA_DICIE={}, NOTA_FEBRE={}, NOTA_MARZO={}, NOTA_FINAL={} WHERE ID={listaSeleccion['tags'][1]} AND CURSO='{SQLcurso}' ;".format(valores))
                    else:
                        cursor.execute(f"UPDATE boletines__{seleccion[0]} SET NOTA1={v[0]}, NOTA2={v[1]}, NOTA_DICIE={v[2]}, NOTA_FEBRE={v[3]}, NOTA_MARZO={v[4]}, NOTA_FINAL={v[5]} WHERE ID={listaSeleccion['tags'][1]} AND CURSO='{SQLcurso}' ;")
                    Terminar()

        #lista.bind('<Double-Button-1>',lambda event: EditarLista(event))

        #obtener notas de alumno en cuestion
        # --ESTE CODIGO NESESITA MUCHOS ARREGOS--
        def ObtenerLista(div,strAÑO,recarga):
            print("Func ObtenerLista")

            global ultimoCurso
            ultimoCurso = [div,strAÑO]
            SQLcurso = str(strAÑO+"_"+div["text"]).lower()
            print(SQLcurso)

            #cursor.execute(f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'tecnica_2023' and table_name LIKE '{SQLcurso}__%' ")
            #SQLmaterias = cursor.fetchall() #Obtiene la lista de todas las tablas de todas las materia del curso en cuestion
            #print(SQLmaterias)

            #obtener lista de alumnos del curso seleccionado
            cursor.execute(f"SELECT ID, NOMBRE, APELLIDO, GRUPO FROM alumnos WHERE CURSO='{SQLcurso}' ")
            alumnos1 = cursor.fetchall()

            #separar el nombre y apellido de la ID
            alumnos = []
            alumnosID = []
            for i in alumnos1:
                alumnos.append((i[1],i[2]))
                alumnosID.append(i[0])


            #obtener lista de materias del curso en cuestion
            cursor.execute(f"SELECT MATERIA FROM materias WHERE CURSOS LIKE '%{SQLcurso}%' ")
            materias = cursor.fetchall()
            materias1 = list(materias)

            #obtiene la lista de materias de la tabla de cursos
            #cursor.execute(f"SELECT MATERIAS FROM cursos WHERE CURSO='{SQLcurso}' ")
            #materias1 = cursor.fetchone()

            if tipoCuenta==1: # si la cuenta es maestro

                cursor.execute(f"SELECT materias FROM usuarios WHERE Usuario='{nombreCuenta}' ")
                materias2 = cursor.fetchone()
                if materias1 == []:
                    print("ERROR: no se encontraron materias en "+SQLcurso)
                    alumnos = [noMaterias]
                else:
                    materiasCursoActual = []
                    materiasAdmitidas = []
                    for x in materias2[0].split(";"):
                        x = x.split(",")
                        if str(x[1]+"_"+x[2]).lower() == SQLcurso.lower():
                            print(x)
                            materiasCursoActual.append(x[0])
                    for i in materiasCursoActual:
                        if i in materias1[0].split(";"):
                            materiasAdmitidas.append(i)
                    
                    if len(materiasAdmitidas)<=0:
                        print("ERROR: no se encontraron materias en "+SQLcurso)
                        alumnos = [noMaterias]
                        materiasAdmitidas = [noMaterias]

                    print(materias1)
                    print(materias2)
                    print(materiasCursoActual)
                    print(materiasAdmitidas)
                            
                        

                ComboboxAlumno['values'] = materiasAdmitidas


            else: #si la cuenta es preceptor o administrador

                #En el caso que no se encuentren alumnos
                if alumnos == []:
                    print("ERROR: no se encontraron alumnos en "+SQLcurso)
                    alumnos = [noAlumnos]

                ComboboxAlumno['values'] = alumnos
            

            # cambia automaticamente la seleccion al primer alumno al cambiar de curso o division
            if ComboboxAlumno.get()=="" or recarga==False:
                try:
                    ComboboxAlumno.current(0)
                except:
                    ComboboxAlumno['values'] = [""]
                    ComboboxAlumno.current(0)
                
            #preparar variables del alumno actual para mysql
            if tipoCuenta!=1: #en el caso de que la cuenta NO sea maestro
                print(ComboboxAlumno.current())
                print(alumnosID)
                alumno = ComboboxAlumno.current()

                try: #prevenir exepcion si no se encontraro alumnos
                    alumnoID = alumnosID[alumno]
                    alumno = alumnos[alumno]
                except:
                    print("error definiendo alumnoID (probablemente no se encontraron alumnos)")
                    pass
            
            lista.delete(*lista.get_children()) #Limpiar lista antes de insertar nuevos elementos


            print(alumnos)
            #solo en el caso de que se encuentren alumnos (admin/prece) o materias (profe)
            if alumnos != [noAlumnos] and alumnos != [noMaterias]: 

                if tipoCuenta==1: #en el caso de ser cuenta de profesor

                    SQLmateria = ComboboxAlumno["values"][ComboboxAlumno.current()]
                    for alumno in alumnos1:
                        cursor.execute(f"INSERT IGNORE INTO {SQLcurso}__{SQLmateria}(ID,NOMBRE,APELLIDO,GRUPO) VALUES('{alumno[0]}','{alumno[1]}','{alumno[2]}','{alumno[3]}')")

                    cursor.execute(f"SELECT ID, NOMBRE, APELLIDO, GRUPO, NOTA1, NOTA2, NOTA_DICIE, NOTA_FEBRE, NOTA_MARZO, NOTA_FINAL FROM {SQLcurso}__{SQLmateria} ")
                    INalumno = cursor.fetchall()
                    print(INalumno)

                    incompleto = False

                    for alumno1 in INalumno:
                        alumno1 = list(alumno1)
                        for i in range(len(alumno1)):
                            if alumno1[i]=="":
                                alumno1[i] = None

                        if all(alumno1 is None for alumno1 in alumno1)==True:
                            incompleto = True
                            promedio = ""
                        elif alumno1[4] is None or alumno1[5] is None:
                            promedio = ""
                        else:
                            promedio = (int(alumno1[4])+int(alumno1[5]))/2

                        for i in range(len(alumno1)):
                            if alumno1[i] is None:
                                alumno1[i] = ""

                        valoresInsert=[str(alumno1[1]+" "+alumno1[2]),alumno1[4],alumno1[5],"",promedio,alumno1[6],alumno1[7],alumno1[8],alumno1[9]]
                        print(valoresInsert)
                        for valor in valoresInsert:
                            if valor is None:
                                valoresInsert[valoresInsert.index(valor)] = ""

                        lista.insert('',END,values=valoresInsert, tags=(str(incompleto),alumno[0]))
                        print(str("incompleto = "+str(incompleto)))

                else: # en el caso de ser preceptor o administrador

                    #Obtener Info del alumno Seleccionado
                    print(alumno)
                    cursor.execute(f"SELECT ID, NOMBRE, APELLIDO, GRUPO FROM alumnos WHERE CURSO='{SQLcurso}' AND ID='{alumnoID}' ")
                    INalumno = cursor.fetchone()
                    INalumno = list(INalumno)
                    print(INalumno)

                    #Por cada materia del curso del alumno
                    print(materias)

                    for DBmateria in materias:

                        DBmateria = DBmateria[0]
                        print(DBmateria)
                        print("a")
                        cursor.reset()

                        #Crear Row para notas del alumno si no existe
                        DBmateria = DBmateria.replace(" ","_")
                        cursor.execute(f"INSERT IGNORE INTO boletines__{DBmateria}(ID,CURSO) VALUES('{alumnoID}','{SQLcurso}') ")

                        print(DBmateria,alumnoID,SQLcurso)
                        #Obtener Notas del Alumno
                        cursor.execute(f"SELECT NOTA1, NOTA2, NOTA3, NOTA_DICIE, NOTA_FEBRE, NOTA_MARZO, NOTA_FINAL, ID FROM boletines__{DBmateria} WHERE ID='{alumnoID}' and CURSO='{SQLcurso}' ")
                        notas = cursor.fetchone()
                        

                        #separar ID de las notas
                        IDnotas = notas[7]
                        notas = list(notas)
                        notas.pop(7)

                        cursor.reset()
                        materia = DBmateria.replace("_"," ")
                        print(notas)
                        print(type(notas))

                        incompleto = False

                        for i in range(len(notas)):
                            if notas[i]=="":
                                notas[i] = None

                        if all(notas is None for notas in notas)==True:
                            incompleto = True
                            promedio = ""
                        elif notas[0] is None or notas[1] is None:
                            promedio = ""
                        else:
                            promedio = (int(notas[0])+int(notas[1]))/2

                        for i in range(len(notas)):
                            if notas[i] is None:
                                notas[i] = ""

                        valoresInsert=[materia.capitalize(),notas[0],notas[1],promedio,notas[3],notas[4],notas[5],notas[6]]
                        for valor in valoresInsert:
                            if valor is None:
                                valoresInsert[valoresInsert.index(valor)] = ""

                                
                        lista.insert('',END,values=valoresInsert, tags=(str(incompleto),IDnotas))
                        print(str("incompleto = "+str(incompleto)))
                


        #al apretar un boton de division
        def SeleccionDivision(boton, strAÑO):
            print(boton["text"])
            for btn in BotonesDIVISION:
                if btn == boton and btn["relief"]=="groove" and btn["bg"]==BG4color:
                    ObtenerLista(boton,strAÑO,True)
                    #print("recarga de lista")
                elif btn == boton:
                    btn.config(relief="groove",bg=BG4color)
                    ObtenerLista(boton,strAÑO,False)
                    #print("cambio de division")
                elif btn["text"]==" ":
                    btn.config(relief="solid",bg=BGcolor)
                else:
                    btn.config(relief="solid",bg=BG3color)

        #creacion de botones de divisiones
        def CambioDivision(strAÑO,año):
            for btnDIV in BotonesDIVISION:
                btnDIV.destroy()
            BotonesDIVISION.clear()
            print(año)
            ColumnaDIVISION = 1
            for DIVISION in DIVISIONES[año]:
                BotonDIVISION = Button(FrameCurso,text=DIVISION,bg=BG3color,relief="solid",borderwidth=1)
                BotonDIVISION.config(height= 1, width=3,command=lambda B=BotonDIVISION, C=strAÑO:SeleccionDivision(B,C))
                if BotonDIVISION["text"]==" ":
                    BotonDIVISION["state"] = "disabled"
                    BotonDIVISION.config(bg=BGcolor)
                BotonDIVISION.grid(row=1,column=ColumnaDIVISION+1, padx=0, pady=0, sticky="news")
                BotonesDIVISION.append(BotonDIVISION)
                ColumnaDIVISION = ColumnaDIVISION + 1

        #Al apretar un boton de año
        def SeleccionAño(boton,año):
            print(boton["text"])
            for btn in BotonesAÑOS:
                if btn == boton and btn["relief"]=="groove" and btn["bg"]==BG4color:
                    btn.config(relief="groove",bg=BG4color)
                    CambioDivision(boton["text"],año)
                    BotonesDIVISION[0].config(relief="sunken")
                    SeleccionDivision(BotonesDIVISION[0],boton["text"])
                elif btn == boton:
                    btn.config(relief="groove",bg=BG4color)
                    CambioDivision(boton["text"],año)
                    BotonesDIVISION[0].config(relief="sunken")
                    SeleccionDivision(BotonesDIVISION[0],boton["text"])
                else:
                    btn.config(relief="solid",bg=BG3color)


        #Creacion de botones de AÑOS
        for AÑO in AÑOS:
            FrameCurso.columnconfigure(tuple(range(0,9)), weight=1)
            FrameCurso.rowconfigure((0,1), weight=1)
            BotonAÑO = Button(FrameCurso,text=AÑO,bg=BG3color,relief="solid",borderwidth=1)
            BotonAÑO.config(height= 1, width=3,command=lambda B=BotonAÑO,C=ColumnaAÑO:SeleccionAño(B,C))
            BotonAÑO.grid(row=0,column=ColumnaAÑO+1, padx=0, pady=0, sticky="news")
            BotonesAÑOS.append(BotonAÑO)
            print(ColumnaAÑO)
            ColumnaAÑO = ColumnaAÑO + 1

        BotonesAÑOS[0].config(relief="sunken")
        SeleccionAño(BotonesAÑOS[0],1)

if __name__ == "__main__":
    #ventana principal
    tk = Tk()
    tk.title("pyNotas")
    tk.geometry("712x480")
    #tk.resizable(0,0)
    with open('database.txt', 'r') as archivo:
        database_var = archivo.read()
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

    #--ARREGLO BUG DE TKINTER--
    def fixed_map(option):
        return [elm for elm in style.map('Treeview', query_opt=option) if
        elm[:2] != ('!disabled', '!selected')]
    style = ttk.Style()
    style.map('Treeview', foreground=fixed_map('foreground'),
    background=fixed_map('background'))

    tk.configure(bg=BGcolor)

    def funcExit(a,b):
        exit()

    boletines = boletines1(tk,sql,cursor)
    boletines.crear(tk,sql,cursor,3,"test",funcExit)

    tk.mainloop()