import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

#Hecho por Javier Correa Y Alejo Guzman
import mysql.connector
class reset_button():
    def __init__(self,ventana_reset):
        self.ventana = ventana_reset
        self.intentos=3
        self.restablece()
        
        
    def restablece(self):
       # Establecer el texto inicial
        self.ventana.iconbitmap("Imagenes/Colegio_logo.ico")
        self.ventana.title("Restablecer Contraseña")
        self.frame_restablecer= ttk.LabelFrame(self.ventana, text="Restablecer Contraseña",padding=(20,10))
        self.frame_restablecer.grid(row=1,column=0,padx=(70), pady=(10),sticky="nsew")
        self.frame_restablecer.columnconfigure(0, weight=1)
        self.frame_restablecer.rowconfigure((0,1,2,3,4,5,6),weight=1)
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure((0,1), weight=1)

        
        ttk.Label(self.frame_restablecer, text="Contraseña nueva").grid(row=0, column=0,padx=5, pady=5, sticky="ew")
        self.contraseña=ttk.Entry(self.frame_restablecer, show="●")
        
        self.contraseña.grid(row=1, column=0,padx=5, pady=5, sticky="ew")
        self.check = IntVar()
        self.boton_check = ttk.Checkbutton(self.frame_restablecer, variable=self.check, command= self.ver_contraseña)
        self.boton_check.grid(row=1, column=1,padx=5, pady=5, sticky="ew")
        self.contraseña.bind('<Return>', lambda event: self.procesar_enter(event,self.very))
        self.contraseña.focus_set()
        ttk.Label(self.frame_restablecer, text="Confirmar contraseña").grid(row=2, column=0,padx=5, pady=5, sticky="ew")
        self.very=ttk.Entry(self.frame_restablecer)
        self.very.grid(row=3, column=0,padx=5, pady=5, sticky="ew", ipady=2)
        self.very.bind('<Return>', lambda event: self.procesar_enter(event,self.mail))
        self.very.bind("<Up>", lambda event: self.flecha_arriba(event,self.contraseña))
        
        ttk.Label(self.frame_restablecer, text="Usuario").grid(row=4,column=0,padx=5, pady=5, sticky="ew")
        self.mail=ttk.Entry(self.frame_restablecer)
        self.mail.grid(row=5, column=0,padx=5, pady=5, sticky="ew", ipady=2) 
        self.mail.bind('<Return>', lambda event: self.presionar_enter(event,self.guardar))
        self.mail.bind("<Up>", lambda event: self.flecha_arriba(event,self.very))
        
        
        ttk.Button(self.frame_restablecer, text="Restablecer Contraseña",command=self.guardar).grid(row=6, column=0,padx=10, pady=10, sticky="nsew")
        
        self.ventana.bind("<Escape>", lambda event: self.salir_programa(self.ventana))
        self.ventana.protocol("WM_DELETE_WINDOW",lambda: self.salir_programa(self.ventana))
    def ver_contraseña(self):
        if self.check.get() == 1:
            self.contraseña.config(show="")
        else:
            self.contraseña.config(show="●")
    
    def quitar(self):
        self.ventana.quit()
        
    def guardar(self):  
        self.new = self.contraseña.get()
        self.mail2 = self.mail.get()
        self.new1=self.very.get()
        y = 0
        try:
            self.cnx = mysql.connector.connect(user="root", password="", host="localhost", database="tecnica_2023")
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            print("Error al conectarse a MySQL: {}".format(err))
            pass
        if not self.new or not self.mail or not self.new1:
            messagebox.showerror("Error","Debe llenar todos los campos")
            return False
        if self.new == self.new1:
            self.cursor.execute("UPDATE usuarios SET Contraseña = %s WHERE Usuario = %s",(self.new,self.mail2))
            self.cnx.commit()
            self.contraseña.delete(0, "end")
            self.very.delete(0, "end")
            self.mail.delete(0, "end")
        
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Informacion","Contraseña Actualizada")
                self.cursor.close()
                self.cnx.close()
            else:
                messagebox.showerror("Error","Usuario incorrecto o la contraseña ya existe en esta cuenta")
        else:
            self.contraseña.delete(0, "end")
            self.very.delete(0, "end")
            self.mail.delete(0, "end")
            self.intentos -=1
            if self.intentos > 0:
                messagebox.showerror("Inicio de sesion",f"credenciales invalidas. Te quedan {self.intentos}intentos")
            else:
                messagebox.showerror("inicio de sesion",f"intentos agotados se cerrara la ventana")
                self.quitar()
    def presionar_enter(self,event,funcion):
        funcion()
    def procesar_enter(self,event, next_entry):
        next_entry.focus_set()
    def flecha_arriba(self,event,anterior_entry): 
        anterior_entry.focus_set()
    def salir_programa(self,root):
        if messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?"):
            root.destroy()
    
if __name__ == "__main__":
    ventana= tk.Tk()
    reset_button1 = reset_button(ventana)
    ventana.mainloop()