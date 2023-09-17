#menu.py

from tkinter import *
from tkinter import ttk
import boletines as boletines
import Profesores
from alumnos import alumnos1
from inasistencias import inasistencias1
from cuentas import cuentas1
from PIL import ImageTk, Image

class menu1:
    def __init__(self,tk,sql,cursor):
        self.alumnos = alumnos1(tk,sql,cursor)
        self.inasistencias = inasistencias1(tk,sql,cursor)
        self.cuentas = cuentas1(tk,sql,cursor)
            
    def crear(self,tk,sql,cursor,tipoCuenta,nombreCuenta,cerrarSesion,menuFunc):

        def eliminar():
            for elemento in tk.winfo_children():
                elemento.destroy()

        def administrar_boletines():
            eliminar()
            self.boletines.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc)
            return

           #ejecutar modulo para administrar los boletines

        def administrar_asistencias():
            eliminar()
            self.inasistencias.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc)
            return
            #ejecutar modulo para administrar las asistencias

        def administrar_alumnos():
            eliminar()
            def alumnosFunc(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,alumnosFunc):
                self.alumnos.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,alumnosFunc)
            alumnosFunc(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,alumnosFunc)
            return
            #ejecutar modulo del ingreso de alumnos

        def administrar_cuentas():
            eliminar()
            def cuentasFunc(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc):
                self.cuentas.crear(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc)
            cuentasFunc(tk,sql,cursor,tipoCuenta,nombreCuenta,menuFunc,cuentasFunc)
            return
            #ejecutar modulo de administracion de cuentas

        def administrar_horarios():
            return
            #ejecutar modulo para administrar los horarios

        def administrar_materias(tk):
            eliminar()
            Profesores.botones_docentes(tk)
            #ejecutar modulo de administracion de cuentas

        def administrar_filtros():
            return
            #ejecutar modulo de administracion de cuentas

        def administrar_aulas():
            return
            #ejecutar modulo de administracion de cuentas

        def cerrar_sesion():
            eliminar()
            cerrarSesion()
            return
        
        BGcolor="#c9daf8"
        BG1color="#212121"
        BG2color="#6D9EEB"
        tk.configure(bg=BGcolor)
        

        tk.grid_columnconfigure(0, weight=1)
        
        BG2 = Frame(tk, bg=BG2color,width=512,height=32)
        #BG1 = Frame(tk, bg=BG1color,width=80,height=256)
        #BG1.place(relx = 0.0, rely = 1.0, anchor ='sw', relwidth=0.1, relheight=1.0)
        BG2.place(relx = 0.0, rely = 1.0, anchor ='sw', relwidth=1.0, relheight=0.07)
        self.imagen_administrar_boletin = ImageTk.PhotoImage(Image.open("imagenes/administrar_boletin.png").resize((20, 20), Image.ANTIALIAS))
        self.imagen_administrar_horario = ImageTk.PhotoImage(Image.open("imagenes/administrar_horario.png").resize((20, 20), Image.ANTIALIAS))
        self.imagen_administrar_asistencia = ImageTk.PhotoImage(Image.open("imagenes/administrador_de_asistencia.png").resize((20, 20), Image.ANTIALIAS))
        self.imagen_administrar_alumnos = ImageTk.PhotoImage(Image.open("imagenes/administrar_alumnos.png").resize((25, 25), Image.ANTIALIAS))
        self.imagen_administrar_cuentas = ImageTk.PhotoImage(Image.open("imagenes/administrar_cuentas.png").resize((20, 20), Image.ANTIALIAS))


      





        gridposicion = Label(tk, text="", font=('Arial',0), bg=BGcolor)
        gridposicion.grid(row=10,column=1, columnspan=2, padx=9999, pady=(0, 0 ))

        fuente_grande = ('Arial', 30, "bold")
        etiqueta_bienvenida = Label(tk, text="¡Bienvenido, "+nombreCuenta+"!", font=fuente_grande, bg=BGcolor)
        etiqueta_bienvenida.grid(row=0,column=1, columnspan=2, padx=0, pady=(0, 0))

        fuente_chica = ('Arial', 15, "bold")
        etiqueta_bienvenida = Label(tk, text="¿Qué desea hacer hoy?", font=fuente_chica, bg=BGcolor)
        etiqueta_bienvenida.grid(row=1, column=1, columnspan=2,padx=0, pady=(0, 0), ipady=0)


        #Boton Boletines
        boton_boletines = Button(tk, text="Administrar boletines", image=self.imagen_administrar_boletin, compound="left", borderwidth=1, relief="solid", height=30 , width=300, command=administrar_boletines, font=("Helvetica", 16))
        boton_boletines.grid(row=2, column=1, padx=(0, 10), pady=(0, 0), sticky="E")

        #Boton Asistencias
        boton_asistencias = Button(tk, text="Administrar Asistencias",image=self.imagen_administrar_asistencia,compound="left",borderwidth=1,relief="solid",  height=30 , width=300, command=administrar_asistencias, font=("Helvetica", 16))
        boton_asistencias.grid(row=3, column=1, padx=(0, 10), pady=(0, 0), sticky="E")

        #Boton Alumnos
        boton_alumno = Button(tk, text="Administrar alumnos",image=self.imagen_administrar_alumnos,compound="left",borderwidth=1,relief="solid",  height=30 , width=300, command=administrar_alumnos, font=("Helvetica", 16))
        boton_alumno.grid(row=4, column=1, padx=(0, 10), pady=(0,0), sticky="E")

        #Boton Cuentas
        boton_cuentas = Button(tk, text="Cuentas",image=self.imagen_administrar_cuentas,compound="left",borderwidth=1,relief="solid",  height=30 , width=300, command=administrar_cuentas, font=("Helvetica", 16))
        boton_cuentas.grid(row=5, column=1, padx=(0, 10), pady=(0,0), sticky="E")

        #Boton Horarios
        boton_horarios = Button(tk, text="Administrar Horarios",image=self.imagen_administrar_horario,compound="left",borderwidth=1,relief="solid",  height=30 , width=300, command=administrar_horarios, font=("Helvetica", 16))
        boton_horarios.grid(row=2, column=2, padx=(10, 0), pady=(0, 0), sticky="W")

        #Boton Materias
        boton_horarios = Button(tk, text="Materias y profesores",image=self.imagen_administrar_horario,compound="left",borderwidth=1,relief="solid",  height=30 , width=300, command=lambda:administrar_materias(tk), font=("Helvetica", 16))
        boton_horarios.grid(row=3, column=2, padx=(10, 0), pady=(0, 0), sticky="W")

        #Boton Filtros
        boton_horarios = Button(tk, text="Filtros",image=self.imagen_administrar_horario,compound="left",borderwidth=1,relief="solid",  height=30 , width=300, command=administrar_filtros, font=("Helvetica", 16))
        boton_horarios.grid(row=4, column=2, padx=(10, 0), pady=(0, 0), sticky="W")

        #Boton Aulas
        boton_horarios = Button(tk, text="Administrar Aulas",image=self.imagen_administrar_horario,compound="left",borderwidth=1,relief="solid",  height=30 , width=300, command=administrar_aulas, font=("Helvetica", 16))
        boton_horarios.grid(row=5, column=2, padx=(10, 0), pady=(0, 0), sticky="W")


        if tipoCuenta == 1: #botones Maestro
            boton_boletines['state'] = NORMAL
            boton_horarios['state'] = NORMAL
            boton_asistencias['state'] = DISABLED
            boton_alumno['state'] = DISABLED
            boton_cuentas['state'] = DISABLED
        if tipoCuenta == 2: #botones Preceptor
            boton_boletines['state'] = NORMAL
            boton_horarios['state'] = NORMAL
            boton_asistencias['state'] = NORMAL
            boton_alumno['state'] = NORMAL
            boton_cuentas['state'] = DISABLED
        if tipoCuenta == 3: #botones Administrador
            boton_boletines['state'] = NORMAL
            boton_horarios['state'] = NORMAL
            boton_asistencias['state'] = NORMAL
            boton_alumno['state'] = NORMAL
            boton_cuentas['state'] = NORMAL

        boton_cerrar_sesion = Button(tk, text="Cerrar Sesión", width=16, height=1, command=cerrar_sesion, bg="light coral", font=("Helvetica", 12))
        boton_cerrar_sesion.place(relx = 0.995, rely = 0.92, anchor ='se')

        etiqueta_derecha = Label(BG2, text="©5to1ra & 5to3ra - 2023", bg=BG2color,font=("Helvetica", 16))
        etiqueta_derecha.place(relx = 1.0, rely = 0.5, anchor ='e')

        etiqueta_izquierda = Label(BG2, text="", bg=BG2color,font=("Helvetica", 16))
        etiqueta_izquierda.place(relx = 0.1, rely = 0.5, anchor ='w')

        if tipoCuenta==1:
            etiqueta_izquierda.config(text="Profesor")
        elif tipoCuenta==2:
            etiqueta_izquierda.config(text="Preceptor")
        elif tipoCuenta==3:
            etiqueta_izquierda.config(text="Administrador")

        #canvas.tag_raise(rectangulo)