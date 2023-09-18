#pip install mysql-connector-python
#pip install tkcalendar

#CREATE USER 'pipo'@'localhost' IDENTIFIED BY '1243';
#GRANT ALL PRIVILEGES ON *.* TO 'pipo'@'localhost'; 

try:
    from tkinter import *
    from tkinter import ttk,messagebox
    from tkcalendar import Calendar
    from PIL import ImageTk, Image

    import mysql.connector
    from datetime import datetime
    
except:
    print("no se encuentran librerias nesesarias")
    exit()


from registrar import registrar1

BGcolor="#c9daf8"  #Celeste muy claro
BG1color="#212121" #Negro
BG2color="#6D9EEB" #Celeste
BG3color="#A4C2F4" #Celeste claro
BG4color="#6FA8DC" #Cyan
BG5color="#9E9E9E" #gris claro


class cuentas1:
    def __init__(self, tk, sql, cursor):
        #self.registrar=registrar1(tk,sql,cursor)
        self.registrar=registrar1()
        #cursor.execute("create table if not exists usuarios( ID INT AUTO_INCREMENT PRIMARY key, usuario varchar (50) not null, email varchar (50) not null, contraseña varchar (50) not null, tipo INT, MATERIAS mediumtext not null);")

        #cursor.execute("SELECT CURSO FROM `cursos`")
        #databasesPrefix = cursor.fetchall() #Obtiene la lista de todos los cursos
        #print(databasesPrefix)
        #for prefix in databasesPrefix:
        #    prefix = str(prefix[0])
        #    cursor.execute(f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'tecnica_2023' and table_name LIKE '{prefix}__%'")
        #    materias1 = cursor.fetchall() #Obtiene la lista de todas las tablas de todas las materia del curso en cuestion
        #    print(materias1)

    def crear(self,tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc):

        cursor.reset()
        
        def eliminar():
            for elemento in tk.winfo_children():
                elemento.destroy()
        def volver():
            eliminar()
            menuFunc(tipoCuenta,nombreCuenta)
            return
        
        def funcregistrar():
            eliminar()
            self.registrar.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc)


        

        checkbox_var = BooleanVar()
        checkbox_var.set(False)

        def eliminarCuenta(lista):
            seleccion = lista.selection()
            print(seleccion)
            if len(seleccion)<=0:
                messagebox.showinfo(message="No se ha seleccionado\nninguna usuario", title="Error")
            else:
                opcion = messagebox.askyesno(message="esta usted seguro?\nse eliminaran los usuarios seleccionados", title="Advertencia",icon='warning')
                if opcion==True:
                    for i in seleccion:
                        fila = lista.item(i)
                        fila = fila.get("values")
                        print(fila)
                        print(fila[0])
                        cursor.execute(f"DELETE FROM usuarios WHERE ID='{fila[0]}' LIMIT 1")
                    ObtenerLista(UltimoTipo)


        #tk.grid_columnconfigure(0, weight=1)

        FrameTOP = Frame(tk,bg=BGcolor)
        FrameTOP.place(relx = 0.0, rely = 0.0, anchor ='nw', relwidth=1.0, relheight=0.15)

        FrameBotones=Frame(FrameTOP,bg=BGcolor)
        FrameBotones.place(relx = 1.0, rely = 0.5, anchor ='e', relwidth=1.0, relheight=0.8)

        FrameCurso=Frame(FrameTOP, bg=BGcolor, highlightbackground=BG1color, highlightthickness=1)
        FrameCurso.place(relx = 0.0, rely = 0.48, anchor ='sw', relwidth=0.74, relheight=0.4)

        FrameCurso.columnconfigure(tuple(range(0,6)), weight=1)
        FrameCurso.rowconfigure(0, weight=1)

        FrameLabel1 = Frame(FrameCurso,bg=BG2color, highlightbackground=BG1color, highlightthickness=0.5)
        FrameLabel1.grid(row=0,column=0,columnspan=2,sticky="news")



        LabelAÑO = Label(FrameCurso, bg=BG2color, text="Tipo de Cuenta:")
        LabelAÑO.grid(row=0,column=0,columnspan=2)

        BotonTipo0 = Button(FrameCurso,text="Todos",bg=BG3color,relief="solid",borderwidth=1,width=8, command=lambda: SeleccionTipo(0))
        BotonTipo1 = Button(FrameCurso,text="Maestro",bg=BG3color,relief="solid",borderwidth=1,width=12, command=lambda: SeleccionTipo(1))
        BotonTipo2 = Button(FrameCurso,text="Preceptor",bg=BG3color,relief="solid",borderwidth=1,width=12, command=lambda: SeleccionTipo(2))
        BotonTipo3 = Button(FrameCurso,text="Administrador",bg=BG3color,relief="solid",borderwidth=1,width=12, command=lambda: SeleccionTipo(3))
        BotonTipo0.grid(row=0,column=2,columnspan=1,sticky="news")
        BotonTipo1.grid(row=0,column=3,columnspan=1,sticky="news")
        BotonTipo2.grid(row=0,column=4,columnspan=1,sticky="news")
        BotonTipo3.grid(row=0,column=5,columnspan=1,sticky="news")

    

        FrameBotones.columnconfigure(tuple(range(0,8)), weight=1)
        FrameBotones.rowconfigure((0,1), weight=1)
        #iconos de botones
        self.imagen_eliminar =ImageTk.PhotoImage(Image.open("imagenes/eliminar.png").resize((20, 20), Image.ANTIALIAS))
        self.imagen_volver =ImageTk.PhotoImage(Image.open("imagenes/volver.png").resize((20, 20), Image.ANTIALIAS))
        self.imagen_editar =ImageTk.PhotoImage(Image.open("imagenes/editar.png").resize((15, 15), Image.ANTIALIAS))
        self.imagen_imprimir = ImageTk.PhotoImage(Image.open("imagenes/imprimir.png").resize((20, 20), Image.ANTIALIAS))
        
        
        Botones = [(0, BotonTipo0),(1, BotonTipo1),(2, BotonTipo2),(3, BotonTipo3)]


        OcultarContraseña = BooleanVar(value=True)

        #BotonPeticion = Button(FrameBotones, text ="Enviar Peticion",width=20)#, command = lambda: accion.actualizar(0,lista))
        BotonImprimir = Button(FrameBotones, text ="Imprimir",image=self.imagen_imprimir,compound="left",width=40)#, command = lambda: accion.actualizar(0,lista))
        BotonVolver   = Button(FrameBotones, text ="Volver",image=self.imagen_volver,compound="left",width=60, command = lambda: volver())
        BotonCuenta   = Button(FrameBotones, text ="Registrar Cuenta",width=20, command = lambda: funcregistrar())
        BotonEliminar = Button(FrameBotones, text ="Eliminar Cuenta",image=self.imagen_eliminar,compound="left",bg="#960000",fg="white",width=20, command = lambda: eliminarCuenta(lista))
        BotonEditar   = Button(FrameBotones, text ="Editar Cuenta",image=self.imagen_editar,compound="left",width=30, command = lambda: EditarCuenta())
        BotonContraseña= Checkbutton(FrameBotones, text="Ocultar Contraseñas",width=20,variable=OcultarContraseña,bg=BGcolor,activebackground=BGcolor,command=lambda: ObtenerLista(UltimoTipo))

        BotonImprimir["state"] = "disabled"

        #BotonPeticion.grid(row=0,column=0,columnspan=2,padx=4,pady=(0,1),sticky="news")
        BotonImprimir.grid(row=0,column=7,columnspan=1,padx=(4,1),pady=(0,1),sticky="news")
        BotonVolver.grid(row=0,column=8,columnspan=1,padx=(1,4),pady=(0,1),sticky="news")
        BotonCuenta.grid(row=1,column=3,columnspan=2,padx=4,pady=(1,0),sticky="news")
        BotonEditar.grid(row=1,column=5,columnspan=2,padx=4,pady=(1,0),sticky="news")
        BotonEliminar.grid(row=1,column=7,columnspan=2,padx=4,pady=(1,0),sticky="news")
        BotonContraseña.grid(row=1,column=0,columnspan=3,padx=4,pady=(1,0),sticky="news")
        

        if tipoCuenta == 1: #botones Maestro
            BotonCuenta['state'] = DISABLED
            BotonEliminar['state'] = DISABLED
        elif tipoCuenta == 2: #botones Preceptor
            BotonCuenta['state'] = DISABLED
            BotonEliminar['state'] = DISABLED
        elif tipoCuenta == 3: #botones Administrador
            BotonCuenta['state'] = NORMAL
            BotonEliminar['state'] = NORMAL


        #recargar = Button(FrameBotones, text ="Actualizar Lista",width=17 , command = lambda: accion.actualizar(0,lista))
        #eliminar = Button(FrameBotones, text ="Eliminar Seleccionados",width=17 , command = lambda: accion.eliminar(lista))
        #recargar.pack(side='left', expand=False)
        #eliminar.pack(side='left', expand=False)

        lista = ttk.Treeview(tk, columns=("c1","c2","c3","c4","c5"), show='headings', selectmode='extended')


        #aprobados = Button(botones, text ="Mostrar Aprobados",width=17 , command = lambda: accion.actualizar(1,lista))
        #desaprobados = Button(botones, text ="Mostrar Desaprobados",width=17 , command = lambda: accion.actualizar(2,lista))
        #desaprobados.pack(side='right', expand=False)
        #aprobados.pack(side='right', expand=False)

        #lista.column("#0",anchor=CENTER, stretch=NO, width=0, minwidth=0)
        lista.column("#1",anchor=CENTER, width=20, minwidth=20)
        lista.column("#2",anchor=CENTER, width=90, minwidth=100)
        lista.column("#3",anchor=CENTER, width=120, minwidth=100)
        lista.column("#4",anchor=CENTER, width=90, minwidth=100)
        lista.column("#5",anchor=CENTER, width=60, minwidth=20)
        #lista.column("#6",anchor=CENTER, stretch=YES, width=100, minwidth=100)
        #lista.heading('#0', text='\n') #para mas lineas de texto en el heading, agregar mas "\n"
        lista.heading('#1', text='ID')
        lista.heading('#2', text='Usuario')
        lista.heading("#3", text="Email")
        lista.heading('#4', text='Contraseña')
        lista.heading('#5', text='Tipo de Cuenta')
        #lista.heading('#6', text='DNI')
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

        subfix = " > Cuentas"
        if tipoCuenta==1:
            etiqueta_izquierda.config(text=str("Profesor"+subfix))
        elif tipoCuenta==2:
            etiqueta_izquierda.config(text=str("Preceptor"+subfix))
        elif tipoCuenta==3:
            etiqueta_izquierda.config(text=str("Administrador"+subfix))


        
        def EditarCuenta():
            filaSeleccion = lista.selection()
            print(filaSeleccion)
            if len(filaSeleccion)<=0:
                messagebox.showinfo(message="No se ha seleccionado\nninguna usuario", title="Error")
            elif len(filaSeleccion)>1:
                messagebox.showinfo(message="Seleccione solo 1 usuario", title="Error")
            else:
                ocultar = OcultarContraseña.get()
                listaSeleccion = lista.item(filaSeleccion)
                seleccion = listaSeleccion['values']
                print(seleccion)
                eliminar()
                if ocultar is True:
                    cursor.execute(f"SELECT contraseña FROM usuarios WHERE ID={seleccion[0]}")
                    seleccion[3] = cursor.fetchone()[0]
                if seleccion[4]=="Maestro":
                    cursor.execute(f"SELECT MATERIAS FROM usuarios WHERE ID={seleccion[0]}")
                    seleccion.append(cursor.fetchone()[0])
                    self.registrar.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc,[True,ocultar,seleccion[1],seleccion[2],seleccion[3],seleccion[4],seleccion[0], seleccion[5]])
                else:
                    self.registrar.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc,[True,ocultar,seleccion[1],seleccion[2],seleccion[3],seleccion[4],seleccion[0]])
                

        
        #obtener notas de cuenta en cuestion
        def ObtenerLista(tipo):
            global UltimoTipo
            UltimoTipo=tipo
            ocultar = OcultarContraseña.get()
            #cursor.execute(f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'tecnica_2023' and table_name LIKE '{SQLcurso}__%' ")
            #SQLmaterias = cursor.fetchall() #Obtiene la lista de todas las tablas de todas las materia del curso en cuestion
            #print(SQLmaterias)
            lista.delete(*lista.get_children()) #Limpiar lista antes de insertar nuevos elementos

            if tipo==0:
                cursor.execute("SELECT ID, usuario, email, contraseña, tipo FROM usuarios")
            else:
                cursor.execute(f"SELECT ID, usuario, email, contraseña, tipo FROM usuarios WHERE tipo={tipo}")
            cuentas = cursor.fetchall()

            for cuenta in cuentas:
                cuenta = list(cuenta)
                if ocultar==True:
                    cuenta[3] = '*' * len(cuenta[3])
                print(cuenta)
                
                if cuenta[4]==1:
                    cuenta[4]="Maestro"
                elif cuenta[4]==2:
                    cuenta[4]="Preceptor"
                elif cuenta[4]==3:
                    cuenta[4]="Administrador"
                else:
                    cuenta[4]="Desconocido"
                
                lista.insert('',END,values=cuenta)

        

        """
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
        """
        #Al apretar un boton de año
        def SeleccionTipo(tipo):
            for btn in Botones:
                if btn[0] == tipo:
                    btn[1].config(relief="sunken",bg=BG4color)
                    ObtenerLista(tipo)
                else:
                    btn[1].config(relief="solid",bg=BG3color)
        
        SeleccionTipo(0)

        """
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
        """
if __name__=="__main__":
    #conectar con mysql
    try:
        sql = mysql.connector.connect(user='root',#usuario registrado en el mysql
                                    password='', #contraseña del usuario
                                    host='127.0.0.1', #IP del server mysql (en este caso localhost)
                                    autocommit=True #automaticamente aplicar cambios
                                    #database='pynotas' #Base de datos que se usara
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
    sql.database = "tecnica_2023"

    for columna in range(10):
        tk.grid_columnconfigure(columna,weight=1)
    for fila in range(10):
        tk.grid_rowconfigure(fila,weight=1)

    def funcExit(a,b):
        exit()

    cuentas = cuentas1(tk,sql,cursor)
    def cuentasFunc1(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc):
        cuentas.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc)

    cuentasFunc1(tk,sql,cursor,3,"test",funcExit,cuentasFunc1)

    tk.mainloop()