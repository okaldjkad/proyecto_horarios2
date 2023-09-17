import tkinter as tk
import mysql.connector
from CompletarAU import AutocompleteEntry
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk, Image
#Hecho por Tobias Bonanno
class añadir_horario():
    def __init__(self,ventana_horario,tipo_de_aula,numero_de_aula):
        self.numero_de_aula=numero_de_aula
        self.tipo_de_aula=tipo_de_aula
        self.ventana_horario=ventana_horario
        self.opciones_division=[]
        self.ventana_horario.title("Añadir horario")
        self.ventana_horario.geometry("900x500")
        self.ventana_horario.protocol("WM_DELETE_WINDOW",lambda: self.volver())
        self.configuracion_widgets()

    def configuracion_widgets(self):
        self.frame_superior=ttk.LabelFrame(self.ventana_horario)
        self.frame_inferior=ttk.LabelFrame(self.ventana_horario)
        self.frame_superior.grid(row=0, column=0, sticky="nsew")
        self.frame_inferior.grid(row=1, column=0,sticky="nsew")
        self.ventana_horario.columnconfigure(0, weight=1)
        self.ventana_horario.rowconfigure(0, weight=2)
        self.ventana_horario.rowconfigure(1, weight=6)
        
    def variables(self):
        self.variable_hora_llegada = tk.StringVar()
        self.variable_hora_salida = tk.StringVar()
        self.variable_tipo_de_aula = tk.StringVar()
        self.variable_numero_aula = tk.IntVar()
        self.variable_grupo = tk.StringVar()
        self.variable_dia = tk.StringVar()
        self.opciones_dia = ["Lunes","Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        self.opciones_grupos = ["A","A","B","C","D","Ambos"]
        self.opciones_division1 = ["A","B","C","D","E","F"]
        self.opciones_division2 = ["1","2","3","4","5","6","7"]
        self.horarios = []

        with open('horario.txt', 'r') as archivo:
            for linea in archivo:
                hora, minuto = linea.strip().split(':')
                hora = int(hora)
                minuto = int(minuto)
                self.horarios.append((f"{hora:02d}:{minuto:02d}"))
        
        self.opciones_grados = [0,1,2,3,4,5,6,7]
        self.conectar_a_mysql()
        self.cursor.execute("SELECT nombre_materia FROM espacio_curricular")
        self.materia = self.cursor.fetchall()
        
        self.cursor.execute("SELECT nombre, apellido FROM profesores")
        self.profesor = self.cursor.fetchall()
        
        self.cursor.execute("SELECT Numero FROM aulas WHERE tipo_de_aula=%s", (self.tipo_de_aula,))
        self.aula = self.cursor.fetchall()
        
        self.aula.sort()
        self.opciones_aula=[self.numero_de_aula] + [numero[0] for numero in self.aula]
        self.opciones_tipo_de_aula=[self.tipo_de_aula,"Laboratorio","Aula","Taller"]
        self.opciones_espacio_curricular = [nombre[0] for nombre in self.materia]
        self.opciones_profesor = [""] + [f"{nombre} {apellido}" for nombre, apellido in self.profesor]
        self.desconectar_de_mysql()
        
    def widgets(self):
        self.variables()
        for x in range(7):
            self.frame_superior.columnconfigure(x, weight=1)
            
        self.frame_superior.rowconfigure(0, weight=1)
        self.frame_superior.rowconfigure(1, weight=1)
        self.volver_imagen=ImageTk.PhotoImage(Image.open("Imagenes/volver.png").resize((15,15)))
        
        ttk.Label(self.frame_superior,text="Horario llegada").grid(row=0, column=0,)
        self.entrada_hora_llegada = AutocompleteEntry(self.horarios,self.frame_superior)
        self.entrada_hora_llegada.grid(row=1, column=0)
        
        ttk.Label(self.frame_superior,text="Horario salida").grid(row=0, column=1,)
        self.entrada_hora_salida = AutocompleteEntry(self.horarios,self.frame_superior)
        self.entrada_hora_salida.grid(row=1, column=1)

        ttk.Label(self.frame_superior,text="Espacio Curricular").grid(row=0, column=2,)
        self.espacio_curricular_entry = AutocompleteEntry(self.opciones_espacio_curricular,self.frame_superior)
        self.espacio_curricular_entry.grid(row=1, column=2)
        
        ttk.Label(self.frame_superior,text="Año").grid(row=0, column=3,)
        self.optionmenuan = ttk.Combobox(self.frame_superior,values=[1,2,3,4,5,6,7],state="readonly")
        self.optionmenuan.grid(row=1, column=3)
        
        ttk.Label(self.frame_superior,text="Division").grid(row=2, column=3,)
        self.optionmenudiv = ttk.Combobox(self.frame_superior,values=self.opciones_division,state="readonly")
        self.optionmenudiv.grid(row=3, column=3)
        
        ttk.Label(self.frame_superior,text="Grupo").grid(row=2, column=0,)
        ttk.OptionMenu(self.frame_superior, self.variable_grupo,*self.opciones_grupos).grid(row=3, column=0)
        
        ttk.Label(self.frame_superior,text="Profesor").grid(row=2, column=1,)
        self.entry_profesor = AutocompleteEntry(self.opciones_profesor,self.frame_superior)
        self.entry_profesor.grid(row=3, column=1)
        
        ttk.Label(self.frame_superior,text="Dia").grid(row=2, column=2,)
        ttk.OptionMenu(self.frame_superior, self.variable_dia,*self.opciones_dia).grid(row=3, column=2)
        
        ttk.Button(self.frame_superior,text="Volver",image=self.volver_imagen,compound="left",command=self.volver).grid(row=0, column=5,rowspan=1)
        
        self.espacio_curricular_entry.bind('<FocusOut>', lambda event: self.validar_materia(event, self.espacio_curricular_entry))
        self.entrada_hora_llegada.bind('<FocusOut>', lambda event: self.validar_contenido(event, self.entrada_hora_llegada))
        self.entrada_hora_salida.bind('<FocusOut>', lambda event: self.validar_contenido(event, self.entrada_hora_salida))
        self.entry_profesor.bind('<FocusOut>', lambda event: self.validar_profesor(event, self.entry_profesor))
        self.optionmenuan.bind("<<ComboboxSelected>>", self.actualizar_division)
        
        self.treeview()
        
    def actualizar_division(self,event):
        año_seleccionado = self.optionmenuan.get()
        if int(año_seleccionado) <= 3:
            opciones_division = self.opciones_division1
            self.optionmenudiv.config(values=opciones_division)
            self.optionmenudiv.current(0)
        else:
            opciones_division = self.opciones_division2
            self.optionmenudiv.config(values=opciones_division)
            self.optionmenudiv.current(0)


    def botones(self):
        ttk.Button(self.frame_superior,text="Agregar horario",command=self.agregar_horario).grid(row=1, column=5,sticky="nsew")
        ttk.Button(self.frame_superior,text="Eliminar horario",command=self.eliminar_horario).grid(row=2, column=5,sticky="nsew")

    def eliminar_horario(self):
        mensaje_confirmar=messagebox.askokcancel("Eliminar","Realmente desea eliminar el horario?")
        if mensaje_confirmar:
            try:
                    self.conectar_a_mysql()
                    selected_items = self.my_treeview.selection()
                    if not selected_items:
                        messagebox.showerror("Error", "Seleccione al menos un horario")
                        return
                    
                    for item in selected_items:
                        horario_id = self.my_treeview.item(item, "values")[0]
                        self.cursor.execute("DELETE FROM horarios WHERE id_hor=%s", (horario_id,))
                        self.my_treeview.delete(item)
                    
                    self.cnx.commit()
                    if len(selected_items) == 1:
                        messagebox.showinfo("Horario", "Horario eliminado")
                    else:
                        messagebox.showinfo("Horarios", "Horarios eliminados")
        
            except:
                messagebox.showerror("Error", "Seleccione al menos un horario")
            finally:
                self.desconectar_de_mysql()
        else:
            pass
    def agregar_horario(self):
        askyesnoal = messagebox.askyesno("Horario", "¿Desea agregar un horario?")
        if askyesnoal:
            try:
                numero_a_dia = {
                    1: "Lunes",
                    2: "Martes",
                    3: "Miércoles",
                    4: "Jueves",
                    5: "Viernes"
                }
                self.conectar_a_mysql()
                self.obtener_datos()
                if self.hora_llegada_get == self.hora_salida_get:
                    messagebox.showerror("Error", "Los horarios no pueden ser siguales")
                elif self.hora_salida_get < self.hora_llegada_get:
                    messagebox.showerror("Error", "La hora de salida no puede ser menor a la hora de llegada")
                elif self.calcular_diferencia_horas(self.hora_llegada_get, self.hora_salida_get) < 1:
                    messagebox.showerror("Error", "Tiene que haber minimo una hora de diferencia entre la hora de llegada y la hora de salida")
                elif self.profesor_get=="" or self.espacio_curricular_get=="" or self.hora_llegada_get=="" or self.hora_salida_get=="":
                    messagebox.showerror("Error", "Debe ingresar todos los datos")
                else:
                    self.cursor.execute("""INSERT INTO horarios(Numero_aula,Tipo_de_aula,Horario_e,Horario_s,Espacio_curricular,Año,Division,Grupo,Profesor,Dia)
                                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(self.aula_get,self.aula_tipo_get,self.hora_llegada_get,self.hora_salida_get,self.espacio_curricular_get,self.año_get,self.division_get,self.grupo_get,self.profesor_get,self.dia_get))
                    self.cnx.commit()
                    self.cursor.execute("SELECT ID_hor FROM horarios ORDER BY ID_hor DESC;")
                    id_profesor=self.cursor.fetchone()
                    self.cursor.fetchall()
                    messagebox.showinfo("Horario","Horario agregado")
                    self.dia_get = numero_a_dia.get(self.dia_get,"")                 
                    self.my_treeview.insert(parent='', index='end', values=(id_profesor,self.aula_get,self.aula_tipo_get,self.hora_llegada_get,self.hora_salida_get,self.espacio_curricular_get,self.año_get,self.division_get,self.grupo_get,self.profesor_get,self.dia_get))
            except mysql.connector.Error as err:
                print(err)
                messagebox.showerror("Error","No se pudo agregar el horario")
            finally:
                self.desconectar_de_mysql()
        
    def treeview(self):
        self.frame = self.frame_inferior
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side="right", fill="y")
        self.my_treeview = ttk.Treeview(self.frame,yscrollcommand=self.scrollbar.set, selectmode="extended")
        self.my_treeview.pack(fill="both", expand=True)
        self.scrollbar.config(command=self.my_treeview.yview)
        self.my_treeview["columns"] = ("ID","Numero de aula","Tipo de aula","Horario llegada","Horario salida","Espacio Curricular","Año","Division","Grupo","Profesor","Dia")
        self.my_treeview.column("#0", width=0, stretch=0)
        self.my_treeview.column("ID", anchor="center", width=1)
        self.my_treeview.column("Numero de aula", anchor="center", width=50)
        self.my_treeview.column("Tipo de aula", anchor="center", width=30)
        self.my_treeview.column("Horario llegada", anchor="center", width=45)
        self.my_treeview.column("Horario salida", anchor="center", width=40)
        self.my_treeview.column("Espacio Curricular", anchor="center", width=55)
        self.my_treeview.column("Año", anchor="center", width=20)
        self.my_treeview.column("Division", anchor="center", width=20)
        self.my_treeview.column("Grupo", anchor="center", width=20)
        self.my_treeview.column("Profesor", anchor="center", width=20)
        self.my_treeview.column("Dia", anchor="center", width=20)
        
        self.my_treeview.heading("#0", text="", anchor="w")
        self.my_treeview.heading("ID", text="ID", anchor="center")
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
        self.insertar_tree()
        
    def insertar_tree(self):
        self.conectar_a_mysql()
        numero_a_dia = {
            1: "Lunes",
            2: "Martes",
            3: "Miércoles",
            4: "Jueves",
            5: "Viernes"
        }
        
        self.cursor.execute("SELECT * FROM horarios WHERE Numero_aula=%s AND tipo_de_aula=%s ORDER BY Horario_e", (self.numero_de_aula,self.tipo_de_aula)) 
        self.data = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM horarios WHERE (CURTIME() BETWEEN `Horario_e` AND `Horario_s` AND DAYOFWEEK(NOW()) - 1 = Dia) AND Numero_aula=%s AND tipo_de_aula=%s; ", (self.numero_de_aula,self.tipo_de_aula))
        self.horario_actual = self.cursor.fetchall()
        
        self.data=[elemento for elemento in self.data if elemento not in self.horario_actual]
        self.data = [list(row) for row in self.data]
        self.horario_actual = [list(row) for row in self.horario_actual]
        
        for i, elemento in enumerate(self.data):
            dia_numero = elemento[10]
            dia_nombre = numero_a_dia.get(dia_numero, "")
            self.data[i][10] = dia_nombre
        for i, elemento in enumerate(self.horario_actual):
            dia_numero = elemento[10]
            dia_nombre = numero_a_dia.get(dia_numero, "desconocido")
            self.horario_actual[i][10] = dia_nombre

        
        self.my_treeview.tag_configure("meowrow",background="#6B8F71")
        for i in self.horario_actual:
            self.my_treeview.insert(parent='', index='end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],i[10]), tags=("meowrow", i[1]))
        for x in self.data:
            self.my_treeview.insert(parent='', index='end', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9],x[10]), tags=(x[1],))

    def validar_materia(self, event, entry_widget):
        self.espacio_curricular_entry.hide_listbox(self.ventana_horario)
        widget_con_enfoque = self.ventana_horario.focus_get()
        if isinstance(widget_con_enfoque, tk.Listbox):
            return
        entrada = entry_widget.get()
        if not entrada in self.opciones_espacio_curricular:
            messagebox.showerror("Error", "La materia no existe")
    def validar_profesor(self, event, entry_widget):
        self.entry_profesor.hide_listbox(self.ventana_horario)
        widget_con_enfoque = self.ventana_horario.focus_get()
        if isinstance(widget_con_enfoque, tk.Listbox):
            return
        entrada = entry_widget.get()
        if not entrada in self.opciones_profesor:
            messagebox.showerror("Error", "El profesor no existe")
            
    def calcular_diferencia_horas(self,hora_llegada, hora_salida):
        hora_llegada_obj = datetime.strptime(hora_llegada, "%H:%M")
        hora_salida_obj = datetime.strptime(hora_salida, "%H:%M")
        self.diferencia = hora_salida_obj - hora_llegada_obj
        return self.diferencia.total_seconds() / 3600 
    
    def validar_contenido(self, event, entry_widget):
        entry_widget.hide_listbox(self.ventana_horario)
        widget_con_enfoque = self.ventana_horario.focus_get()
        
        if isinstance(widget_con_enfoque, tk.Listbox):
            return
        entrada = entry_widget.get()
        try:
            if any(c.isalpha() for c in entrada):
                messagebox.showerror("Error", "El contenido contiene letras. Debe ser numérico.")
                entry_widget.delete(0, tk.END)
                
            elif len(entrada)==4:
                if int(entrada[0:1]) <=6 or int(entrada[3:5]) >=60 or int(entrada[3:5])%5 != 0:
                    messagebox.showerror("Error", "El contenido tiene que tener un horario valido")
                    entry_widget.delete(0, tk.END)
                else:
                    pass
                
            if not entrada in self.horarios:
                messagebox.showerror("Error", "El horario no es valido")
                entry_widget.delete(0, tk.END)
                
            elif int(entrada[0:2]) >=22 or int(entrada[0:2]) <=6 or int(entrada[3:5]) >=60 or int(entrada[3:5])%5 != 0:
                messagebox.showerror("Error", "El contenido tiene que tener un horario valido")
                entry_widget.delete(0, tk.END)
                
            elif len(entrada)>5 or len(entrada)<4:
                messagebox.showerror("Error", "El contenido tiene que tener menos de 5 caracteres o mas de 4")
                entry_widget.delete(0, tk.END)
        except ValueError:
            pass
    
    def obtener_datos(self):
        self.dias_a_numeros = {"Lunes": 1, "Martes": 2, "Miercoles": 3, "Jueves": 4, "Viernes": 5}
        self.aula_get = self.numero_de_aula
        self.aula_tipo_get = self.tipo_de_aula
        self.hora_llegada_get = self.entrada_hora_llegada.get()
        self.hora_salida_get = self.entrada_hora_salida.get()
        self.espacio_curricular_get = self.espacio_curricular_entry.get()
        self.año_get = self.optionmenudiv.get()
        self.division_get = self.optionmenuan.get()
        self.grupo_get = self.variable_grupo.get()
        self.profesor_get = self.entry_profesor.get()
        self.dia_get = self.variable_dia.get()
        self.dia_get = self.dias_a_numeros.get(self.dia_get.capitalize(), 0)
    
    def volver(self):
        import Parte_principal
        self.ventana_horario.destroy()
        Parte_principal.horarios()

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
    def ejecutar(self):
        self.ventana_horario.mainloop()

if __name__ == "__main__":
    ventana_horario = tk.Tk()
    ventana_horario2= añadir_horario(ventana_horario,"Laboratorio",10)
    ventana_horario2.widgets()
    ventana_horario2.botones()
    ventana_horario2.ejecutar()