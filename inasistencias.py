#pip install mysql-connector-python
#pip install tkcalendar

#CREATE USER 'pipo'@'localhost' IDENTIFIED BY '1243';
#GRANT ALL PRIVILEGES ON . TO 'pipo'@'localhost'; 

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



class inasistencias1():
    def __init__(self, tk, sql, cursor):
        #Auto Crear Base de datos
        sql.database = "tecnica_2023"

        cursor.execute("SELECT CURSO FROM cursos")
        fetchCursos = cursor.fetchall()
        print(fetchCursos)
        
        #for fetch in fetchCursos:
        #    database = str("inasistencias__"+fetch[0])
        #    print(fetch[0])
        #    cursor.execute(f"create table if not exists {database}(ID INT AUTO_INCREMENT PRIMARY key, NOMBRE varchar(50) not null, APELLIDO varchar(50) not null, FECHA date not null, TIPO INT not null);")
        
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
        
        cursor.reset()

        def volver():
            for elemento in tk.winfo_children():
                elemento.destroy()
            menuFunc(tipoCuenta,nombreCuenta)
            return



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
        self.imagen_eliminar =ImageTk.PhotoImage(Image.open("imagenes/eliminar.png").resize((20, 20), Image.LANCZOS))
        self.imagen_volver =ImageTk.PhotoImage(Image.open("imagenes/volver.png").resize((20, 20), Image.LANCZOS))
        self.imagen_editar =ImageTk.PhotoImage(Image.open("imagenes/editar.png").resize((15, 15), Image.LANCZOS))




        FrameBotones=Frame(FrameTOP,bg=BGcolor)
        FrameBotones.place(relx = 0.52, rely = 0.5, anchor ='w', relwidth=0.48, relheight=0.8)

        FrameBotones.columnconfigure(tuple(range(0,3)), weight=1)
        FrameBotones.rowconfigure((0,1), weight=1)

        #BotonPeticion = Button(FrameBotones, text ="Enviar Peticion",width=20)#, command = lambda: accion.actualizar(0,lista))
        BotonImprimir = Button(FrameBotones, text ="Imprimir",width=10)#, command = lambda: accion.actualizar(0,lista))
        BotonVolver   = Button(FrameBotones, text ="Volver",image=self.imagen_volver,compound="left",width=60, command = lambda: volver())
        BotonNuevo   = Button(FrameBotones, text ="Registrar",width=10, command = lambda: EditarLista(True))
        BotonEditar   = Button(FrameBotones, text ="Editar",image=self.imagen_editar,compound="left",width=50, command = lambda: EditarLista(False))
        BotonEliminar   = Button(FrameBotones, text ="Eliminar",image=self.imagen_eliminar,compound="left",width=10,bg="#960000",fg="white", command = lambda: eliminarInasistencia())


        LabelAlumno = Label(FrameBotones, text ="Alumno:",width=10,bg=BGcolor,anchor="e", font=("Arial", 10, "bold"))
        BotonImprimir["state"] = "disabled"

        ComboboxAlumno = ttk.Combobox(FrameBotones,text="Alumno", state="readonly", values=[""])

        #BotonPeticion.grid(row=0,column=0,columnspan=2,padx=4,pady=(0,1),sticky="news")
        BotonImprimir.grid(row=0,column=2,columnspan=1,padx=(4,1),pady=(0,1),sticky="news")
        BotonVolver.grid(row=0,column=3,columnspan=1,padx=(1,4),pady=(0,1),sticky="news")
        BotonNuevo.grid(row=0,column=0,columnspan=1,padx=(4,1),pady=(0,1),sticky="news")
        BotonEditar.grid(row=0,column=1,columnspan=1,padx=(1,4),pady=(0,1),sticky="news")
        BotonEliminar.grid(row=1,column=0,columnspan=1,padx=(4,1),pady=(1,0),sticky="news")
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

        lista = ttk.Treeview(tk, columns=("c0","c1","c2","c3","c4")#,"c5","c6")
                             , show='headings', selectmode='extended')

        #aprobados = Button(botones, text ="Mostrar Aprobados",width=17 , command = lambda: accion.actualizar(1,lista))
        #desaprobados = Button(botones, text ="Mostrar Desaprobados",width=17 , command = lambda: accion.actualizar(2,lista))
        #desaprobados.pack(side='right', expand=False)
        #aprobados.pack(side='right', expand=False)

        lista.column("#1",anchor=CENTER, stretch=YES, width=180, minwidth=180)
        lista.column("#2",anchor=CENTER, stretch=YES, width=200, minwidth=200)
        lista.column("#3",anchor=CENTER, stretch=YES, width=160, minwidth=160)
        lista.column("#4",anchor=CENTER, stretch=YES, width=170, minwidth=170)
        lista.heading('#1', text='Fecha')
        lista.heading('#2', text='Inasistencia o Llegada Tarde')
        lista.heading('#3', text='Faltas')
        lista.heading("#4", text='Total a la fecha')
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

        subfix = " > Inasistencias"
        if tipoCuenta==1:
            etiqueta_izquierda.config(text=str("Profesor"+subfix))
        elif tipoCuenta==2:
            etiqueta_izquierda.config(text=str("Preceptor"+subfix))
        elif tipoCuenta==3:
            etiqueta_izquierda.config(text=str("Administrador"+subfix))

        ComboboxAlumno.bind("<<ComboboxSelected>>",lambda a: ObtenerLista(ultimoCurso[0],ultimoCurso[1],True))


        noAlumnos = "ERROR: No hay Alumnos"

        def eliminarInasistencia():
            filaSeleccion = lista.selection()
            print(filaSeleccion)
            if len(filaSeleccion)<=0:
                messagebox.showinfo(message="No se ha seleccionado\nninguna Inasistencia", title="Error")
            else:
                opcion = messagebox.askyesno(message="esta usted seguro?\nse eliminara la inasistencia seleccionada", title="Advertencia",icon='warning')
                if opcion==True:
                    for i in filaSeleccion:
                        listaSeleccion = lista.item(i)
                        print(listaSeleccion)
                        alumnoID = cursor.fetchone()
                        print(alumnoID)
                        cursor.execute(f"DELETE FROM `inasistencias` WHERE CURSO='{ultimoCurso[1]}_{ultimoCurso[0]['text']}' AND ID={listaSeleccion['tags'][0]}")
                ObtenerLista(ultimoCurso[0],ultimoCurso[1],True)


        def EditarLista(nuevo):
            filaSeleccion = lista.selection()
            print(filaSeleccion)
            if len(filaSeleccion)<=0 and nuevo==False:
                messagebox.showinfo(message="No se ha seleccionado\nninguna Inasistencia", title="Error")
            elif len(filaSeleccion)>1 and nuevo==False:
                messagebox.showinfo(message="Selecciona solo 1 Inasistencia", title="Error")
            elif ComboboxAlumno["values"][0]==noAlumnos:
                messagebox.showinfo(message="No se encontraron Alumnos", title="Error")
            else:
                print(ComboboxAlumno["values"])
                FrameEditar = Frame(FrameTOP,bg=BG3color)
                FrameEditar.place(relx = 0.0, rely = 0.5, anchor ='w', relwidth=1.0, relheight=0.8)
                FrameEditar.columnconfigure(tuple(range(0,6)), weight=1)
                FrameEditar.rowconfigure((0,1), weight=1)
                FrameBotones.place_forget()
                FrameCurso.place_forget()
                
                fuenteEdit=("Arial",9,"bold")
                fuenteEdit2=("Arial",9)

                LabelFecha = Label(FrameEditar,text="Fecha", font=fuenteEdit, bg=BG3color)
                LabelFecha.grid(row=0,column=0,columnspan=1,padx=(0,0),pady=(0,2),sticky="e")
                FrameFecha = Frame(FrameEditar,width=10)
                FrameFecha.grid(row=0,column=1,columnspan=3,pady=(0,2),sticky="news")
                
                EntryFecha = Entry(FrameFecha,width=10, font=fuenteEdit2)
                EntryFecha.place(relx=0.0,rely=0.0,relheigh=1.0,relwidth=0.75)
                BotonFecha = Button(FrameFecha,width=10, text="📅",font=("arial",18),command=lambda: BotonCalendario())
                BotonFecha.place(relx=0.75,rely=0.0,relheigh=1.0,relwidth=0.25)
                
                if nuevo is True:
                    EntryFecha.insert(0,str(datetime.now().date()))
                
                LabelTipo = Label(FrameEditar,text="Falta o llegada tarde", font=fuenteEdit, bg=BG3color, anchor="e")
                LabelTipo.grid(row=0,column=4,columnspan=1,padx=(16,0),pady=2,sticky="e")
                ComboboxTipo = ttk.Combobox(FrameEditar, values=["Llegada Tarde", "Inasistencia"], state="readonly")
                ComboboxTipo.grid(row=0, column=5, columnspan=1, padx=(16, 0), pady=2, sticky="news")

                ErrorLabel = Label(FrameEditar, text="",font=fuenteEdit, bg=BG3color, fg='#C80000', anchor="w")
                ErrorLabel.place(relx = 0.1, rely = 0.75, anchor ='w', relwidth=0.5, relheight=0.3)

                BotonConfirmar = Button(FrameEditar, text="Confirmar", command=lambda:Confirmar())
                BotonConfirmar.grid(row=0,column=6,columnspan=1,padx=(32,0),pady=2,sticky="news")

                BotonCancelar = Button(FrameEditar, text="Cancelar", command=lambda:Terminar())
                BotonCancelar.grid(row=1,column=6,columnspan=1,padx=(32,0), pady=2,sticky="news")
                
                filaSeleccion = lista.selection()
                listaSeleccion = lista.item(filaSeleccion)
                seleccion = listaSeleccion['values']
                if nuevo==False:
                    print(seleccion)
                    EntryFecha.insert(0,seleccion[0])
                    ComboboxTipo.current(listaSeleccion['tags'][1])
                else:
                    ComboboxTipo.current(0)
                
                def BotonCalendario():
                    calendarioWin=Toplevel(tk)
                    calendarioWin.geometry("180x160")
                    calendarioWin.resizable(0,0)
                    calendarioWin.title("📅")
                    calendario = Calendar(calendarioWin,font=("arial", 7) , selectmode = 'day', date_pattern="yyyy-mm-dd", mindate=datetime(2000,1,1), maxdate=datetime.now())
                    calendario.bind('<<CalendarSelected>>',lambda ev: focus(ev,EntryFecha,"2000-01-01",calendario,calendarioWin))
                    
                    calendario.pack()
                    calendarioWin.lift()
                    calendarioWin.focus_force()
                    calendarioWin.grab_set()

                def focus(event, entry, textoDefault, calendario, calendarioWin):
                    event = str(event)
                    print(event)
                    textoEntry = entry.get()
                    print(textoEntry)
                    if event=='<VirtualEvent event x=0 y=0>':
                        entry.delete(0,END)
                        entry.config(fg="black")
                        entry.focus()
                        entry.insert(0,calendario.get_date())
                        calendarioWin.destroy()
                    elif event=='<FocusIn event>' and textoEntry == "" or textoEntry == None or textoEntry == textoDefault:
                        entry.delete(0,END)
                        entry.config(fg="black")
                    elif event=='<FocusOut event>' and textoEntry == "" or textoEntry == None:
                        entry.insert(0,textoDefault)
                        entry.config(fg="gray")

                def Terminar():
                    EntryFecha.delete(0,END)
                    
                    
                    FrameEditar.place_forget() 
                    FrameBotones.place(relx = 0.52, rely = 0.5, anchor ='w', relwidth=0.48, relheight=0.8)
                    FrameCurso.place(relx = 0.0, rely = 0.5, anchor ='w', relwidth=0.5, relheight=0.8)
                    
                    ObtenerLista(ultimoCurso[0],ultimoCurso[1],True)
                    
                def Confirmar():
                    SQLcurso = str((ultimoCurso[1]+"_"+ultimoCurso[0]["text"]).lower())
                    print(SQLcurso)
                    print(listaSeleccion['tags'])
                    
                    falta = ComboboxTipo.current()
                    
                    cursor.execute(f"SELECT NOMBRE, APELLIDO, ID FROM alumnos WHERE CURSO='{SQLcurso}' ")
                    alumnos = cursor.fetchall()


                    alumnoC = ComboboxAlumno.current()
                    alumno = [alumnos[alumnoC][0],alumnos[alumnoC][1]]
                    alumnoID = alumnos[alumnoC][2]

                    Ifecha = EntryFecha.get().strip()
                    Sfechas = Ifecha.replace('/','.').replace('-','.')
                    Lfechas = Sfechas.split('.')
                    
                    try:
                        Cfecha = datetime(int(Lfechas[0]), int(Lfechas[1]), int(Lfechas[2]))
                    except ValueError:
                        ErrorLabel.config(text = "Ingrese una Fecha de Nacimiento Válida.")
                        print("Fecha Invalida")
                        tk.bell()
                        return

                    if nuevo == False:
                        cursor.execute(f"UPDATE inasistencias SET FECHA='{Cfecha}', TIPO='{falta}' WHERE ID={listaSeleccion['tags'][0]} AND ID_ALUMNO={alumnoID} AND CURSO='{ultimoCurso[1]}_{ultimoCurso[0]['text']}'; ")
                        Terminar()
                    elif nuevo == True:
                        cursor.execute(f"INSERT INTO inasistencias (ID_ALUMNO,CURSO,FECHA,TIPO) VALUES({alumnoID},'{ultimoCurso[1]}_{ultimoCurso[0]['text']}','{EntryFecha.get()}','{falta}');")
                        Terminar()

        #lista.bind('<Double-Button-1>',lambda event: EditarLista(event))

        #obtener notas de alumno en cuestion
        def ObtenerLista(div,strAÑO,recarga):
            global ultimoCurso
            ultimoCurso = [div,strAÑO]
            SQLcurso = str((strAÑO+"_"+div["text"]).lower())
            print(SQLcurso)
            cursor.execute(f"SELECT NOMBRE, APELLIDO, ID FROM alumnos WHERE CURSO='{SQLcurso}' ")
            alumnos = cursor.fetchall()
            if alumnos == []:
                print("ERROR: no se encontraron alumnos en "+SQLcurso)
                alumnos = [noAlumnos]
                ComboboxAlumno["values"] = alumnos
            else:
                CAvalues = []
                for i in alumnos:
                    CAvalues.append(str(i[0]+" "+i[1]))
                ComboboxAlumno['values'] = CAvalues
            
            if ComboboxAlumno.get()=="" or recarga==False:
                try:
                    ComboboxAlumno.current(0)
                except:
                    ComboboxAlumno['values'] = [""]
                    ComboboxAlumno.current(0)
            
            Calumno = ComboboxAlumno.current()
            alumno = [alumnos[Calumno][0],alumnos[Calumno][1]]
            alumnoID = alumnos[Calumno][2]

            lista.delete(*lista.get_children()) #Limpiar lista antes de insertar nuevos elementos

            
            if alumnos != [noAlumnos]:
                cursor.execute(f"SELECT ID, NOMBRE, APELLIDO, GRUPO FROM alumnos WHERE CURSO='{SQLcurso}' AND ID='{alumnoID}' ")
                INalumno = cursor.fetchall()
                INalumno = list(INalumno[0])
                print(INalumno)


                cursor.execute(f"SELECT FECHA, TIPO, ID FROM inasistencias WHERE ID_ALUMNO={alumnoID} ")
                ausencias = cursor.fetchall()

                TOTALausencia = float(0)
                for ausencia in ausencias:
                    if ausencia is not None:
                        ausencia = list(ausencia)
                        IDausencia = ausencia[2]
                        ausencia.pop(2)
                        cursor.reset()
                        print(ausencia)
                        print(type(ausencia))
                        
                        StrAusencia = ["Llegada Tarde", "Inasistencia"]
                        ValoresAusencia = [0.5, 1]

                        TIPOausencia = ausencia[1]

                        VALORausencia = ValoresAusencia[TIPOausencia]
                        ausencia[1] = StrAusencia[TIPOausencia]
                        
                        TOTALausencia = TOTALausencia + VALORausencia
                        
                        valoresInsert=[ausencia[0],ausencia[1],VALORausencia,TOTALausencia]
                        for valor in valoresInsert:
                            if valor is None:
                                valoresInsert[valoresInsert.index(valor)] = ""

                                
                        lista.insert('',END,values=valoresInsert, tags=(IDausencia,TIPOausencia))
                


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
    print("a")
    #ventana principal
    tk = Tk()
    tk.title("pyNotas")
    tk.geometry("1200x680")
    #tk.resizable(0,0)

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

    inasistencias = inasistencias1(tk,sql,cursor)
    inasistencias.crear(tk,sql,cursor,3,"test",funcExit)
    

    tk.mainloop()