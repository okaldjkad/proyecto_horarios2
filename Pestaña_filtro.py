import tkinter as tk
import mysql.connector
from CompletarAU import AutocompleteEntry
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from PDF import PDF_filtro
#Hecho por Tobias Bonanno
class Pestaña_filtro():
    def __init__(self,ventana_filtro):
        self.ventana_filtro=ventana_filtro
        self.ventana_filtro.title("Añadir horario")
        self.ventana_filtro.geometry("900x500")
        self.query=""
        self.techer = None
        self.label_dia = None
        self.año = None
        self.division = None
        self.dia = None
        self.configuracion_widgets()
    def configuracion_widgets(self):
        """
        Configurar los widgets para la interfaz de usuario.
       Esta función configura varios widgets `ttk.LabelFrame` y configura sus posiciones de cuadrícula en la ventana rootmodification.
       También configura el peso de las columnas y filas en los widgets rootmodification y frame_superior.
       Finalmente, llama a la función `widgets` para insertar los widgets.
       """
        self.frame_superior=ttk.LabelFrame(self.ventana_filtro)
        self.frame_inferior=ttk.LabelFrame(self.ventana_filtro)
        self.frame_derecha=ttk.LabelFrame(self.frame_superior)
        self.frame_izquierda=ttk.LabelFrame(self.frame_superior)
        
        
        self.frame_superior.grid(row=0, column=0, sticky="nsew")
        self.frame_inferior.grid(row=1, column=0,sticky="nsew")
        self.frame_derecha.grid(row=0, column=1,sticky="nsew")
        self.frame_izquierda.grid(row=0, column=0,sticky="nsew")
        self.ventana_filtro.columnconfigure(0, weight=1)
        self.ventana_filtro.rowconfigure(0, weight=1)
        self.ventana_filtro.rowconfigure(1, weight=6)
        
        self.frame_superior.columnconfigure(0, weight=10)
        self.frame_superior.columnconfigure(1, weight=2)
        self.frame_superior.rowconfigure(0, weight=1)
        self.frame_derecha.columnconfigure(0, weight=1)
        self.frame_derecha.columnconfigure(1, weight=2)
        self.frame_derecha.rowconfigure(0, weight=1)
        self.frame_derecha.rowconfigure(1, weight=3)
        self.frame_derecha.rowconfigure(2, weight=1)
        self.frame_derecha.rowconfigure(3, weight=1)
    def widgets(self):
        self.variable_check = tk.StringVar()
        self.variable_check.set("")
        style = ttk.Style()
        style.configure("Frame.TFrame", background="white")
        ttk.Label(self.frame_derecha, text="Filtros",anchor="w").grid(column=0, row=0,sticky="news")
        ttk.Button(self.frame_derecha,text="Volver",command=self.volver).grid(column=1, row=0, sticky="news",padx=(10,0))
        self.frame_variables=ttk.LabelFrame(self.frame_derecha)
        self.frame_variables.grid(column=0, row=1,columnspan=2,sticky="news")
        self.frame_variables.columnconfigure(0, weight=1)
        self.frame_variables.rowconfigure(0, weight=1)
        self.frame_variables.rowconfigure(1, weight=1)
        ttk.Button(self.frame_derecha,text="Exportar a PDF",command=self.exportar_a_pdf).grid(column=0, row=3, sticky="news",columnspan=2)
    def agregar_ciclo_basico(self):
        ttk.Button(self.frame_derecha,text="Filtrar",command=self.filtrar_division).grid(column=0, row=2, sticky="news",columnspan=2)
        ttk.Label(self.frame_izquierda, text="Curso").grid(column=0, row=0)
        ttk.Label(self.frame_izquierda, text="Division").grid(column=0, row=1)
        self.frame_izquierda.rowconfigure(0, weight=1)
        self.frame_izquierda.rowconfigure(1, weight=1)
        for x in range(0, 3):
            if x==0:
                ttk.Button(self.frame_izquierda, text=f"{x+1}°", command=lambda r=x+1: self.boton_agregar_año(r)).grid(column=x+1, row=0,columnspan=2, sticky="ew")
            else:
                ttk.Button(self.frame_izquierda, text=f"{x+1}°", command=lambda r=x+1: self.boton_agregar_año(r)).grid(column=1+x*2, row=0,columnspan=2, sticky="ew")
        divisiones = ["A", "B", "C", "D", "E", "F"]
        for x in range(7):
            self.frame_izquierda.columnconfigure(x, weight=1)
        for x, division in enumerate(divisiones):
            ttk.Button(self.frame_izquierda, text=f"{division}",command=lambda y=division: self.boton_agregar_division(y)).grid(column=x+1, row=1, sticky="ew")
    def volver(self):
        import Parte_principal
        self.ventana_filtro.destroy()
        Parte_principal.filtros()

    def agregar_ciclo_superior(self):
        ttk.Button(self.frame_derecha,text="Filtrar",command=self.filtrar_division).grid(column=0, row=2, sticky="news",columnspan=2)
        ttk.Label(self.frame_izquierda, text="Curso").grid(column=0, row=0)
        ttk.Label(self.frame_izquierda, text="Division").grid(column=0, row=1)
        self.frame_izquierda.rowconfigure(0, weight=1)
        self.frame_izquierda.rowconfigure(1, weight=1)
        for x in range(4, 8):
            self.frame_izquierda.columnconfigure(x-1, weight=1)
            if x == 8:
                ttk.Button(self.frame_izquierda, text=f"{x}°", command=lambda r=x: self.boton_agregar_año(r)).grid(column=6, row=0,columnspan=2,sticky="ew")
            else:
                ttk.Button(self.frame_izquierda, text=f"{x}°", command=lambda r=x: self.boton_agregar_año(r)).grid(column=int(2*(x-3.5)), row=0,columnspan=2,sticky="ew")
            
        for x in range(0,6):
            self.frame_izquierda.columnconfigure(x, weight=1)
            ttk.Button(self.frame_izquierda, text=f"{x+1}°", command=lambda r=x+1: self.boton_agregar_division(r)).grid(column=x+1, row=1,sticky="ew")
    def agregar_dia(self):
        ttk.Button(self.frame_derecha,text="Filtrar",command=self.filtrar_dia).grid(column=0, row=2, sticky="news",columnspan=2)
        numero_a_dia = {
                1: "Lunes",
                2: "Martes",
                3: "Miércoles",
                4: "Jueves",
                5: "Viernes"
        }
        ttk.Label(self.frame_izquierda, text="Dia de la semana").grid(column=0, row=0)
        for x in range(0,5):
            self.frame_izquierda.columnconfigure(x, weight=1)
            ttk.Button(self.frame_izquierda, text=f"{numero_a_dia[x+1]}°", command=lambda r=numero_a_dia[x+1]: self.boton_agregar_dia(r)).grid(column=x+1, row=0,sticky="ew")
    def filtrar_dia(self):
        try:
            self.conectar_a_mysql()
            self.my_treeview.delete(*self.my_treeview.get_children())
            dia_a_numero = {
            "Lunes": 1,
            "Martes": 2,
            "Miércoles": 3,
            "Jueves": 4,
            "Viernes": 5
            }
            numero_a_dia = {
                1: "Lunes",
                2: "Martes",
                3: "Miércoles",
                4: "Jueves",
                5: "Viernes"
            }
            self.dia = dia_a_numero[self.dia]
            self.cursor.execute("SELECT * FROM horarios WHERE dia =%s", (self.dia,))
            resultados = self.cursor.fetchall()
            resultados = [list(row) for row in resultados]
            for i, elemento in enumerate(resultados):
                dia_numero = elemento[10]  # El día está en el índice 10 según tu código
                dia_nombre = numero_a_dia.get(dia_numero, "desconocido")
                resultados[i][10] = dia_nombre
            for x in resultados:
                self.my_treeview.insert(parent='', index='end', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9],x[10]), tags=(x[1],))
            messagebox.showinfo("Información", "Filtro aplicado")
        except mysql.connector.Error as err:
            print("Error al conectar a MySQL: {}".format(err))
        finally:
            self.desconectar_de_mysql()
    def boton_agregar_dia(self, dia):
        self.dia=dia
        if self.label_dia:
            self.label_dia.destroy()
        self.label_dia=ttk.Label(self.frame_variables, text=f"Dia: {self.dia}")
        self.label_dia.grid(column=0, row=0)
    def exportar_a_pdf(self):
        if self.año and self.division:
            query="""SELECT * FROM horarios WHERE Año={} AND Division="{}" """.format(self.año, self.division)
        elif self.techer:
            query="""SELECT * FROM horarios WHERE Profesor={}""".format(self.techer)
        elif self.dia:
            query="""SELECT * FROM horarios WHERE Dia={}""".format(self.dia)
        else:
            messagebox.showerror("Error", "Porfavor, seleccionar un filtro")
        pdf2=PDF_filtro("""{}""".format(query))
    def agregar_profesor(self):
        ttk.Button(self.frame_derecha,text="Filtrar",command=self.filtrar_profesor).grid(column=0, row=2, sticky="news",columnspan=2)
        self.frame_izquierda.columnconfigure(0, weight=1)
        self.frame_izquierda.rowconfigure(0, weight=1)
        self.frame_izquierda.rowconfigure(1, weight=1)
        self.conectar_a_mysql()
        self.cursor.execute("SELECT nombre, apellido FROM profesores")
        self.profesor = self.cursor.fetchall()
        self.opciones_profesor = [""] + [f"{nombre} {apellido}" for nombre, apellido in self.profesor]
        self.desconectar_de_mysql()
        self.entry_profesor = AutocompleteEntry(self.opciones_profesor, self.frame_izquierda)
        self.entry_profesor.grid(row=1, column=0,sticky="ew")
        self.entry_profesor.bind('<FocusOut>', lambda event: self.validar_profesor(event, self.entry_profesor))
        ttk.Label(self.frame_izquierda, text="Profesor").grid(column=0, row=0)
        ttk.Button(self.frame_izquierda,text="Añadir",command=self.añadir_profesor).grid(column=0, row=2,columnspan=2)
    def añadir_profesor(self):
        if self.techer:
            self.techer.destroy()
        self.profesor_filtrar = self.entry_profesor.get()
        self.techer=ttk.Label(self.frame_variables, text=f"Profesor: {self.profesor_filtrar}")
        self.techer.grid(column=0, row=0)
    def validar_profesor(self, event, entry_widget):
        widget_con_enfoque = self.ventana_filtro.focus_get()
        # Verifica si el widget con enfoque es un Listbox
        if isinstance(widget_con_enfoque, tk.Listbox):
            return
        entrada = entry_widget.get()
        if not entrada in self.opciones_profesor:
            messagebox.showerror("Error", "El profesor no existe")
            entry_widget.delete(0, tk.END)
    def filtrar_profesor(self):
        try:
            self.conectar_a_mysql()
            self.my_treeview.delete(*self.my_treeview.get_children())
            numero_a_dia = {
                1: "Lunes",
                2: "Martes",
                3: "Miércoles",
                4: "Jueves",
                5: "Viernes"
            }
            self.cursor.execute("SELECT * FROM horarios WHERE profesor =%s", (self.profesor_filtrar,))
            resultados = self.cursor.fetchall()
            resultados = [list(row) for row in resultados]
            for i, elemento in enumerate(resultados):
                dia_numero = elemento[10]  # El día está en el índice 10 según tu código
                dia_nombre = numero_a_dia.get(dia_numero, "desconocido")
                resultados[i][10] = dia_nombre
            for x in resultados:
                self.my_treeview.insert(parent='', index='end', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9],x[10]), tags=(x[1],))
            messagebox.showinfo("Información", "Filtro aplicado")
            
        except Exception as e:
            messagebox.showerror("Error", "Error al filtrar, debe seleccionar un profesor")
            print(e)
            self.cnx.rollback()
        finally:
            self.desconectar_de_mysql()
    def treeview_filter(self):
        self.frame = self.frame_inferior
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side="right", fill="y")
        self.my_treeview = ttk.Treeview(self.frame,yscrollcommand=self.scrollbar.set, selectmode="extended")
        self.my_treeview.pack(fill="both", expand=True)
        self.scrollbar.config(command=self.my_treeview.yview)
        self.my_treeview["columns"] = ("ID","Numero de aula","Tipo de aula","Horario llegada","Horario salida","Espacio Curricular","Año","Division","Grupo","Profesor","Dia")
        self.my_treeview.column("#0", width=0, stretch=0)
        self.my_treeview.column("ID", anchor="n", width=1)
        self.my_treeview.column("Numero de aula", anchor="center", width=20)
        self.my_treeview.column("Tipo de aula", anchor="center", width=30)
        self.my_treeview.column("Horario llegada", anchor="center", width=40)
        self.my_treeview.column("Horario salida", anchor="center", width=40)
        self.my_treeview.column("Espacio Curricular", anchor="center", width=40)
        self.my_treeview.column("Año", anchor="center", width=20)
        self.my_treeview.column("Division", anchor="center", width=20)
        self.my_treeview.column("Grupo", anchor="center", width=20)
        self.my_treeview.column("Profesor", anchor="center", width=20)
        self.my_treeview.column("Dia", anchor="center", width=20)

        self.my_treeview.heading("#0", text="", anchor="w")
        self.my_treeview.heading("Numero de aula", text="Numero de aula", anchor="center")
        self.my_treeview.heading("Tipo de aula", text="Tipo de aula", anchor="center")
        self.my_treeview.heading("Horario llegada", text="Horario llegada", anchor="center")
        self.my_treeview.heading("Horario salida", text="Horario salida", anchor="center")
        self.my_treeview.heading("Espacio Curricular", text="Espacio Curricular", anchor="center")
        self.my_treeview.heading("Año", text="Año", anchor="center")
        self.my_treeview.heading("Division", text="Division", anchor="center")
        self.my_treeview.heading("Grupo", text="Grupo", anchor="center")
        self.my_treeview.heading("Profesor", text="Profesor", anchor="center")
        self.my_treeview.heading("Dia", text="Dia", anchor="center")
    def boton_agregar_año(self, x):
        self.año = x
        ttk.Label(self.frame_variables, text=f"Año:     {self.año}").grid(sticky="w",column=0, row=0)

    def boton_agregar_division(self, y):
        self.division = y
        ttk.Label(self.frame_variables, text=f"Division:    {self.division}").grid(sticky="w",column=0, row=1)

    def filtrar_division(self):
        try:
            self.my_treeview.delete(*self.my_treeview.get_children())
            numero_a_dia = {
                1: "Lunes",
                2: "Martes",
                3: "Miércoles",
                4: "Jueves",
                5: "Viernes"
            }
            self.conectar_a_mysql()
            self.cursor.execute("SELECT * FROM horarios WHERE Año=%s AND Division=%s", (self.año, self.division))
            resultados = self.cursor.fetchall()
            resultados = [list(row) for row in resultados]
            for i, elemento in enumerate(resultados):
                dia_numero = elemento[10]  # El día está en el índice 10 según tu código
                dia_nombre = numero_a_dia.get(dia_numero, "desconocido")
                resultados[i][10] = dia_nombre
            for x in resultados:
                self.my_treeview.insert(parent='', index='end', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9],x[10]), tags=(x[1],))
            messagebox.showinfo("Información", "Filtro aplicado")
        except AttributeError:
            messagebox.showerror("Error", "Debe seleccionar un curso y una división")
        finally:
            self.desconectar_de_mysql()
    def ejecutar(self):
        self.ventana_filtro.mainloop()
        
    def conectar_a_mysql(self):
        try:
                self.cnx = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='proyecto_colegio2'
                )
                self.cursor = self.cnx.cursor()
        except Exception as e:
                print(e)
                messagebox.showerror("Error", "No se pudo conectar a la base de datos")
                self.cnx.rollback()
                
    def desconectar_de_mysql(self):
        self.cursor.close()
        self.cnx.close()

if __name__ == "__main__":
    ventana_horario = tk.Toplevel()
    ventana_horario2= Pestaña_filtro(ventana_horario)
    ventana_horario2.widgets()
    ventana_horario2.agregar_profesor()
    ventana_horario2.treeview_filter()
    ventana_horario2.ejecutar()