import tkinter as tk
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class pantalla_de_administrador(tk.Toplevel):
    """Inicializa la pantalla de administrador"""
    def __init__(self, ventana_administrador):
        self.ventana_administracion = ventana_administrador
        self.ventana_administracion.title("Pantalla de Administrador")
        self.ventana_administracion.geometry("380x600")
        self.ventana_administracion.iconbitmap("Imagenes/Colegio_logo.ico")
        self.ventana_administracion.minsize(380, 620)
        self.colegio_imagen = None
        self.crear_imagen()
        self.widgets_administrador()
        
    def aceptar_credenciales(self):
        self.usuario= self.entrada_usuario.get()
        self.modificar_user = self.entrada_usuario_modificar.get()
        self.administrador = self.es_administrador.get()
        try:
            self.cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='proyecto_colegio2'
            )
            self.cursor = self.cnx.cursor()
            try:
                self.cursor.execute("UPDATE usuarios SET Usuario= %s,  Admin = %s WHERE Contraseña = %s",(self.usuario,self.administrador,self.modificar_user))
                self.cnx.commit()
                self.entrada_usuario.delete(0, "end")
                self.entrada_usuario_modificar.delete(0, "end")
                messagebox.showinfo("Informacion","Usuario Actualizado")      
                self.cnx.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error","Error al actualizar, Usuario no encontrado")
                print(err)
        except mysql.connector.Error as err:
            messagebox.showerror("Error","Error al conectarse a la base de datos")
    def crear_imagen(self):
        self.colegio_imagen=ImageTk.PhotoImage(Image.open("Imagenes/Colegio_logo.png").resize((110,140)))
    def widgets_administrador(self):
        self.es_administrador = tk.IntVar()
        # Configuramos la imagen del logo del administrador y ademas configuramos un label con la imagen y otro con los widgets
        ttk.Label(self.ventana_administracion,image=self.colegio_imagen).grid(row=0, column=0)
        self.frame_administrador = ttk.LabelFrame(self.ventana_administracion, text="Pantalla De Restablecer", padding=(20, 10))
        self.frame_administrador.grid(row=1, column=0, padx=(70), pady=(10), sticky="nsew")
        
        #Configuramos las columnas y filas
        self.ventana_administracion.columnconfigure(0, weight=1)
        self.ventana_administracion.rowconfigure(1, weight= 3)
        self.ventana_administracion.rowconfigure(0, weight=1)
        self.frame_administrador.columnconfigure(0, weight=1)
        self.frame_administrador.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),weight=1)
        
        #Añadimos y Configuramos los botones del frame administrador
        ttk.Label(self.frame_administrador, text="Contraseña del usuario:").grid(row=0, column=0,pady=5,sticky="ew")
        self.entrada_usuario_modificar = ttk.Entry(self.frame_administrador, show="*")
        self.ver_contra_check = tk.IntVar()
        self.ver_contra = ttk.Checkbutton(self.frame_administrador, variable=self.ver_contra_check, command= self.ver_contraseña)
        self.ver_contra.grid(row=1, column=1,pady=5,sticky="ew")
        self.entrada_usuario_modificar.grid(row=1, column=0,pady=5,sticky="ew")
        self.entrada_usuario_modificar.bind('<Return>', lambda event: procesar_enter(event,self.entrada_usuario))
        self.entrada_usuario_modificar.focus_set()
        
        #Añadimos el entry de usuario
        ttk.Label(self.frame_administrador, text="Usuario nuevo").grid(row=2, column=0,pady=5,sticky="ew")
        self.entrada_usuario = ttk.Entry(self.frame_administrador)
        self.entrada_usuario.grid(row=3, column=0,pady=5,sticky="ew")
        self.entrada_usuario.bind('<Return>', lambda event: procesar_enter(event,self.entrada_contraseña))
        self.entrada_usuario.bind("<Up>", lambda event: flecha_arriba(event,self.entrada_usuario_modificar))


        ttk.Checkbutton(self.frame_administrador, text="Es administrador", variable=self.es_administrador).grid(row=14, column=0,pady=5,sticky="ew")
        ttk.Button(self.frame_administrador, text="Actualizar datos", command=self.aceptar_credenciales).grid(row=15, column=0,pady=(1,10),sticky="ew",padx=40)
        
        self.ventana_administracion.bind("<Escape>", lambda event: salir_programa(self.ventana_administracion))
    
    def ver_contraseña(self):
        if self.ver_contra_check.get() == 1:
            self.entrada_usuario_modificar.config(show="")
        else:
            self.entrada_usuario_modificar.config(show="*")

def presionar_enter(event,funcion):
    funcion()
def flecha_arriba(event,anterior_entry): 
    anterior_entry.focus_set()
def procesar_enter(event, next_entry):
    next_entry.focus_set()
def salir_programa(root):
    if messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?"):
        root.destroy()
if __name__ == "__main__":
    ventana=tk.Tk()
    pantalla_de_administrador(ventana)
    ventana.mainloop()