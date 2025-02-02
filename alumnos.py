#pip install mysql-connector-python
#pip install tkcalendar
#pip install Pillow 
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


from ingreso import ingreso1

BGcolor="#c9daf8"  #Celeste muy claro
BG1color="#212121" #Negro
BG2color="#6D9EEB" #Celeste
BG3color="#A4C2F4" #Celeste claro
BG4color="#6FA8DC" #Cyan
BG5color="#9E9E9E" #gris claro


class alumnos1:
    def __init__(self, tk, sql, cursor):
        self.ingreso=ingreso1(tk,sql,cursor)


        # -- CODIGO PARA CREAR BASE DE DATOS AUTOMATICAMENTE --

        #cursor.execute("create table if not exists DNI_alumnos( DNI varchar(10) PRIMARY KEY, AÑO varchar(10) not null, DIVISION varchar(10) not null, CURSO varchar(10) UNIQUE not null, MATERIAS mediumtext not null);")
        #cursor.execute("create table if not exists UID_alumnos( UID INT AUTO_INCREMENT PRIMARY KEY, DNI varchar(10) not null, CURSO varchar(10) not null);")
        
        #Tabla de cursos
        #cursor.execute("""create table if not exists cursos(
        #               ID INT AUTO_INCREMENT PRIMARY KEY,
        #               CURSO varchar(10) UNIQUE not null,
        #               MATERIAS mediumtext
        #               );""")
        
        #Crear tabla de alumnos
        #cursor.execute("""CREATE TABLE if not exists `alumnos` (
        #                `ID` int AUTO_INCREMENT PRIMARY KEY,
        #                `NOMBRE` varchar(50) NOT NULL,
        #                `APELLIDO` varchar(50) NOT NULL,
        #                `CURSO` varchar(10) NOT NULL,
        #                `GRUPO` varchar(10) NOT NULL,
        #                `NACIMIENTO` date NOT NULL,
        #                `TELEFONO` varchar(20),
        #                `nro_de_documento` varchar(10) NOT NULL,
        #                FOREIGN KEY (CURSO) REFERENCES cursos(CURSO)
        #               )""")

        #cursor.execute("SELECT CURSO FROM `cursos`")
        #databasesPrefix = cursor.fetchall() #Obtiene la lista de todos los cursos
        #print(databasesPrefix)
        #for prefix in databasesPrefix:
        #    prefix = str(prefix[0])
        #    cursor.execute(f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'tecnica_2023' and table_name LIKE '{prefix}__%'")
        #    materias1 = cursor.fetchall() #Obtiene la lista de todas las tablas de todas las materia del curso en cuestion
        #    print(materias1)

    def crear(self,tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,alumnosFunc):

        cursor.reset()

        def eliminar():
            for elemento in tk.winfo_children():
                elemento.destroy()
        def volver():
            eliminar()
            menuFunc(tipoCuenta,nombreCuenta)
            return
        
        def funcIngreso(valores=[False]):
            if valores[0] is False:
                valores=[False, ultimoCurso[1], ultimoCurso[0]["text"]]
            eliminar()
            self.ingreso.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,alumnosFunc,valores)
        
        def eliminarAlumno(lista,div,strAÑO):
            SQLcurso = str((strAÑO+"_"+div["text"]).lower())
            seleccionados = lista.selection()
            print(seleccionados)
            sqlIDs = []
            for ElistaID in seleccionados:
                fila = lista.item(ElistaID)
                sqlID = str(fila.get("tags")[0])
                print(sqlID)
                sqlIDs.append(sqlID)
                
            if len(seleccionados)<=0:
                messagebox.showinfo(message="No se ha seleccionado\nningun alumno", title="Error")
            else:
                opcion = messagebox.askyesno(message="esta usted seguro?\nse eliminaran "+str(len(seleccionados))+" alumnos", title="Advertencia",icon='warning')
                if opcion==True:
                    for delID in sqlIDs:
                        print(delID)
                        cursor.execute(f"DELETE FROM `alumnos` WHERE CURSO='{SQLcurso}' and ID={delID} ")
                    ObtenerLista(div,strAÑO)


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
        #Iconos de botones
        self.imagen_eliminar =ImageTk.PhotoImage(Image.open("imagenes/eliminar.png").resize((20, 20), Image.ANTIALIAS))
        self.imagen_volver =ImageTk.PhotoImage(Image.open("imagenes/volver.png").resize((20, 20), Image.ANTIALIAS))
        self.imagen_editar =ImageTk.PhotoImage(Image.open("imagenes/editar.png").resize((15, 15), Image.ANTIALIAS))
        
        FrameBotones=Frame(FrameTOP,bg=BGcolor)
        FrameBotones.place(relx = 0.52, rely = 0.5, anchor ='w', relwidth=0.48, relheight=0.8)

        FrameBotones.columnconfigure(tuple(range(0,3)), weight=1)
        FrameBotones.rowconfigure((0,1), weight=1)

        #BotonPeticion = Button(FrameBotones, text ="Enviar Peticion",width=20)#, command = lambda: accion.actualizar(0,lista))
        BotonImprimir = Button(FrameBotones, text ="Imprimir",width=10)#, command = lambda: accion.actualizar(0,lista))
        BotonVolver   = Button(FrameBotones, text ="Volver",image=self.imagen_volver,compound="left",width=60, command = lambda: volver())
        BotonAlumno   = Button(FrameBotones, text ="Ingresar Alumno",width=20, command = lambda: funcIngreso())
        BotonEliminar = Button(FrameBotones, text ="Eliminar Seleccionados",bg="#960000",fg="white",image=self.imagen_eliminar,compound="left",width=50, command = lambda: eliminarAlumno(lista))
        BotonEditar   = Button(FrameBotones, text ="Editar Seleccionados",image=self.imagen_editar,compound="left",width=15, command = lambda: EditarLista())
        BotonImprimir["state"] = "disabled"

        #BotonPeticion.grid(row=0,column=0,columnspan=2,padx=4,pady=(0,1),sticky="news")
        BotonImprimir.grid(row=0,column=2,columnspan=1,padx=(4,1),pady=(0,1),sticky="news")
        BotonVolver.grid(row=0,column=3,columnspan=1,padx=(1,4),pady=(0,1),sticky="news")
        BotonAlumno.grid(row=1,column=0,columnspan=2,padx=4,pady=(1,0),sticky="news")
        BotonEliminar.grid(row=1,column=2,columnspan=2,padx=4,pady=(1,0),sticky="news")
        BotonEditar.grid(row=0,column=0,columnspan=2,padx=4,pady=(0,1),sticky="news")

        if tipoCuenta == 1: #botones Maestro
            BotonAlumno['state'] = DISABLED
            BotonEliminar['state'] = DISABLED
        elif tipoCuenta == 2: #botones Preceptor
            BotonAlumno['state'] = DISABLED
            BotonEliminar['state'] = DISABLED
        elif tipoCuenta == 3: #botones Administrador
            BotonAlumno['state'] = NORMAL
            BotonEliminar['state'] = NORMAL


        #recargar = Button(FrameBotones, text ="Actualizar Lista",width=17 , command = lambda: accion.actualizar(0,lista))
        #eliminar = Button(FrameBotones, text ="Eliminar Seleccionados",width=17 , command = lambda: accion.eliminar(lista))
        #recargar.pack(side='left', expand=False)
        #eliminar.pack(side='left', expand=False)

        lista = ttk.Treeview(tk, columns=("c1","c2","c3","c4","c5","c6"), show='headings', selectmode='extended')


        #aprobados = Button(botones, text ="Mostrar Aprobados",width=17 , command = lambda: accion.actualizar(1,lista))
        #desaprobados = Button(botones, text ="Mostrar Desaprobados",width=17 , command = lambda: accion.actualizar(2,lista))
        #desaprobados.pack(side='right', expand=False)
        #aprobados.pack(side='right', expand=False)

        lista.column("#0",anchor=CENTER, stretch=NO, width=0, minwidth=0)
        lista.column("#1",anchor=CENTER, stretch=YES, width=100, minwidth=100)
        lista.column("#2",anchor=CENTER, stretch=YES, width=100, minwidth=100)
        lista.column("#3",anchor=CENTER, stretch=YES, width=80, minwidth=80)
        lista.column("#4",anchor=CENTER, stretch=YES, width=80, minwidth=80)
        lista.column("#5",anchor=CENTER, stretch=YES, width=120, minwidth=120)
        lista.column("#6",anchor=CENTER, stretch=YES, width=100, minwidth=100)
        lista.heading('#0', text='\n') #para mas lineas de texto en el heading, agregar mas "\n"
        lista.heading('#1', text='Nombre')
        lista.heading('#2', text='Apellido')
        lista.heading("#3", text="Grupo de\nTaller")
        lista.heading('#4', text='Fecha de\nNacimiento')
        lista.heading('#5', text='Numero Telefonico\ndel Tutor/a')
        lista.heading('#6', text='DNI')
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

        subfix = " > Alumnos"
        if tipoCuenta==1:
            etiqueta_izquierda.config(text=str("Profesor"+subfix))
        elif tipoCuenta==2:
            etiqueta_izquierda.config(text=str("Preceptor"+subfix))
        elif tipoCuenta==3:
            etiqueta_izquierda.config(text=str("Administrador"+subfix))


        def EditarLista():
            filaSeleccion = lista.selection()
            print(filaSeleccion)
            if len(filaSeleccion)<=0:
                messagebox.showinfo(message="No se ha seleccionado\nningun alumno", title="Error")
            elif len(filaSeleccion)>1:
                messagebox.showinfo(message="Seleccione solo 1 alumno", title="Error")
            else:
                listaSeleccion = lista.item(filaSeleccion)
                seleccion = listaSeleccion['values']
                print(seleccion)
                calFecha = seleccion[3].split("-")
                funcIngreso([True,seleccion[0],seleccion[1],ultimoCurso[1],ultimoCurso[0]["text"],seleccion[2],seleccion[4],seleccion[5],datetime(int(calFecha[0]),int(calFecha[1]),int(calFecha[2])),listaSeleccion['tags'][0]])



        #obtener notas de alumno en cuestion
        def ObtenerLista(div,strAÑO):
            global ultimoCurso
            ultimoCurso = [div,strAÑO]
            SQLcurso = str((strAÑO+"_"+div["text"]).lower())
            print(SQLcurso)
            BotonEliminar.config(command = lambda: eliminarAlumno(lista,div,strAÑO))
            #cursor.execute(f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'tecnica_2023' and table_name LIKE '{SQLcurso}__%' ")
            #SQLmaterias = cursor.fetchall() #Obtiene la lista de todas las tablas de todas las materia del curso en cuestion
            #print(SQLmaterias)
            lista.delete(*lista.get_children()) #Limpiar lista antes de insertar nuevos elementos

            cursor.execute(f"SELECT NOMBRE, APELLIDO, GRUPO, NACIMIENTO, TELEFONO, nro_de_documento, ID FROM alumnos WHERE CURSO='{SQLcurso}' ")
            alumnos = cursor.fetchall()

            for alumno in alumnos:
                print(alumno)
                tagID = alumno[6]
                alumno = list(alumno)
                alumno.pop(6)
                if alumno[2] is None:
                    alumno[2]="Ninguno"
                for i in alumno:
                    if i is None:
                        alumno[alumno.index(i)] = ""
                lista.insert('',END,values=alumno,tags=(tagID))


        #al apretar un boton de division
        def SeleccionDivision(boton, strAÑO):
            print(boton["text"])
            for btn in BotonesDIVISION:
                if btn == boton:
                    btn.config(relief="groove",bg=BG4color)
                    ObtenerLista(boton,strAÑO)
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
                if btn == boton:
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

if __name__=="__main__":
    #conectar con mysql
    with open('database.txt', 'r') as archivo:
        database_var = archivo.read()
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

    #ventana principal
    tk = Tk()
    tk.title("pyNotas")
    tk.geometry("712x480")
    #tk.resizable(0,0)
    tk.configure(bg=BGcolor)

    #--ARREGLO BUG DE TKINTER--
    def fixed_map(option):
        return [elm for elm in style.map('Treeview', query_opt=option) if
        elm[:2] != ('!disabled', '!selected')]
    style = ttk.Style()
    style.map('Treeview', foreground=fixed_map('foreground'),
    background=fixed_map('background'))

    #Auto Crear Base de datos
    #cursor.execute("create database if not exists tecnica_2023")
    #sql.database = "tecnica_2023"

    def funcExit(a,b):
        exit()

    alumnos = alumnos1(tk,sql,cursor)
    def alumnosFunc1(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,alumnosFunc):
        alumnos.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,alumnosFunc)

    alumnosFunc1(tk,sql,cursor,3,"test",funcExit,alumnosFunc1)

    tk.mainloop()