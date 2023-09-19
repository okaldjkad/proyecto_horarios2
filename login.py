#login.py

from tkinter import *
from tkinter import ttk
#from PIL import ImageTk, Image
#from tkcalendar import Calendar
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime

# ---TIPO DE CUENTAS---
#  1 = Maestro
#  2 = Preceptor
#  3 = Administrador

tipoCuenta = 0

class login1:
#    def __init__(self):

    def crear(self,tk,sql,cursor,menuFunc): #crear login
            
        BGcolor="#c9daf8"
        tk.configure(bg=BGcolor)
        BG1color="black" #Negro
        BG2color="#6D9EEB" #Celeste
 
        fuente_grande = ('Arial', 30, "bold")
        fuente_mediana = ('Arial', 16)
        fuente_chica = ('Arial', 12)

        

        textoDefault1 = 'Introdusca su Usuario'
        textoDefaul = 'Introdusca su Email'
        textoDefault3 = 'Introdusca su Contraseña'


        BG2 = Frame(tk, bg='#6D9EEB',width=512,height=32)
        BG1 = Frame(tk, bg='black',width=80,height=256)
        BG1.place(relx = 0.0, rely = 1.0, anchor ='sw', relwidth=0.18, relheight=1.0)
        BG2.place(relx = 0.0, rely = 1.0, anchor ='sw', relwidth=1.0, relheight=0.07)

        etiqueta_derecha = Label(BG2, text="©5to1ra Grupo A - 2023", bg=BG2color,font=("Helvetica", 16))
        etiqueta_derecha.place(relx = 1.0, rely = 0.5, anchor ='e')

        #logo

        image = Image.open("Imagenes/logo.png.jpg")  
        photo = ImageTk.PhotoImage(image)
        image_label = Label(BG1, image=photo,borderwidth=0, highlightthickness=0)
        image_label.image = photo  
        image_label.pack()
        image_label.grid(row=0, column=0)  # Grid para la imagen

       


        text_label1 = Label(BG1, text="Escuela de", fg="white", bg='black', font=fuente_grande)
        text_label2 = Label(BG1, text="Educacion", fg="white", bg='black', font=fuente_grande)
        text_label3 = Label(BG1, text="Secundaria", fg="white", bg='black', font=fuente_grande)
        text_label4 = Label(BG1, text="Tecnica", fg="white", bg='black', font=fuente_grande)
        text_label5 = Label(BG1, text="Nº1", fg="white", bg='black', font=fuente_grande)

        text_label1.grid(row=10, column=0, sticky='w',pady=20)
        text_label2.grid(row=11, column=0, sticky='w',pady=20)
        text_label3.grid(row=12, column=0, sticky='w',pady=20)
        text_label4.grid(row=13, column=0, sticky='w',pady=20)
        text_label5.grid(row=14, column=0, sticky='w',pady=20)
        


        #LogoTec1 = Canvas(BG1, bg="black", width=500, height=500)
        #LogoTec1.create_image(125, 169, image=Image.open(r"C:/Users/LAB11/Downloads/LogoTec1.jpg"))
        #LogoTec1.pack()

        loginTitle1 = Label(tk, text="Inicio de Sesion",font=fuente_grande,bg=BGcolor)
        loginTitle1.place(relx = 0.6, rely = 0.02, anchor ='n')

        # ---Usuario---
        #loginLabel1 = Label(tk, text="Introdusca su Nombre de Usuario",font=fuente_chica,bg=BGcolor)
        #loginLabel1.place(relx = 0.6, rely = 0.2, anchor ='n')
        loginInput1 = Entry(tk, width = 25, font=fuente_mediana, fg="gray")
        loginInput1.place(relx = 0.6, rely = 0.27, anchor ='n')

        loginInput1.insert(0, textoDefault1)
        loginInput1.bind('<FocusIn>', lambda ev: focus(ev,loginInput1,textoDefault1))
        loginInput1.bind('<FocusOut>', lambda ev: focus(ev,loginInput1,textoDefault1))

        # ---Email---
        #loginLabel2 = Label(tk, text="Introdusca su Email",font=fuente_chica,bg=BGcolor)
        #loginLabel2.place(relx = 0.6, rely = 0.35, anchor ='n')
        loginInpu = Entry(tk, width = 25, font=fuente_mediana, fg="gray")
        loginInpu.place(relx = 0.6, rely = 0.42, anchor ='n')

        loginInpu.insert(0, textoDefaul)
        loginInpu.bind('<FocusIn>', lambda ev: focus(ev,loginInpu,textoDefaul))
        loginInpu.bind('<FocusOut>', lambda ev: focus(ev,loginInpu,textoDefaul))

        # ---Contraseña---
        #loginLabel3 = Label(tk, text="Introdusca su Contraseña",font=fuente_chica,bg=BGcolor)
        #loginLabel3.place(relx = 0.6, rely = 0.5, anchor ='n')
        loginInput3 = Entry(tk, width = 25, font=fuente_mediana, fg="gray")
        loginInput3.place(relx = 0.6, rely = 0.57, anchor ='n')

        loginInput3.insert(0, textoDefault3)
        loginInput3.bind('<FocusIn>', lambda ev: focus(ev,loginInput3,textoDefault3))
        loginInput3.bind('<FocusOut>', lambda ev: focus(ev,loginInput3,textoDefault3))

        loginError = Label(tk, text="",font=fuente_chica,bg=BGcolor)
        loginError.place(relx = 0.6, rely = 0.67, anchor ='n')
        
        #INSERT INTO usuarios (usuario, email, contraseña) VALUES (%s,%s,%s);

        def focus(event, entry, textoDefault):
            event = str(event)
            print(event)
            textoEntry = entry.get()
            print(textoEntry)
            if event=='<FocusIn event>' and textoEntry == "" or textoEntry == None or textoEntry == textoDefault:
                entry.delete(0,END)
                entry.config(fg="black")
            elif event=='<FocusOut event>' and textoEntry == "" or textoEntry == None:
                entry.insert(0,textoDefault)
                entry.config(fg="gray")

        def eliminar():
            for elemento in tk.winfo_children():
                elemento.destroy()
            #BG1.place_forget()
            #BG2.place_forget()
            #loginBoton.place_forget()
            #loginTitle1.place_forget()
            #loginInput1.place_forget()
            #loginInpu.place_forget()
            #loginInput3.place_forget()
            #loginError.place_forget()

        def logear():
            usuario=loginInput1.get()
            email=loginInpu.get()
            contraseña=loginInput3.get()
            print(usuario,email,contraseña)
            cursor.execute("SELECT * FROM usuarios WHERE Usuario=%s AND email=%s AND Contraseña=%s", (usuario, email, contraseña))
            loginFetch = cursor.fetchone()
            print(loginFetch)
            if usuario=="" or email=="" or contraseña=="" or usuario==textoDefault1 or email==textoDefaul or contraseña==textoDefault3:
                loginError.config(text="Introdusca un Usuario, Email y Contraseña")
                tk.bell()
            elif loginFetch==None:
                loginError.config(text = "Usuario, Email o Contraseña Incorrectos.")
                tk.bell()
            else:
                loginInput1.delete(0,END)
                loginInpu.delete(0,END)
                loginInput3.delete(0,END)
                loginError.config(text="")
                if loginFetch[7]==1:
                    print("tipo de cuenta 1 (maestro)")
                    eliminar()
                    tipoCuenta = 1
                    menuFunc(tipoCuenta,loginFetch[1])
                    return
                elif loginFetch[7]==2:
                    print("tipo de cuenta 2 (preceptor)")
                    eliminar()
                    tipoCuenta = 2
                    menuFunc(tipoCuenta,loginFetch[1])
                    return
                elif loginFetch[7]==3:
                    print("tipo de cuenta 3 (administrador)")
                    eliminar()
                    tipoCuenta = 3
                    menuFunc(tipoCuenta,loginFetch[1])
                    return
                else:
                    print("ERROR: tipo de cuenta desconocido")
                    return
                    
        loginBoton = Button(tk, text ="Iniciar Sesion", height = 1, width = 11, command = logear)
        loginBoton.place(relx = 0.6, rely = 0.8, anchor ='n')
        

