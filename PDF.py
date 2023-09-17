from fpdf import FPDF
import mysql.connector
import os
import subprocess
from win10toast import ToastNotifier
from tkinter import Tk, filedialog
#Hecho por Valentino signorello
class PDF():
    def __init__(self, tipo_de_aula, numero_de_aula):
        self.tipo_de_aula = tipo_de_aula
        self.numero_de_aula = numero_de_aula
        self.pdf = FPDF(orientation='L', unit='mm', format='A4')
        self.pdf.add_page()
        self.tabla()
    
        
        
    def header(self):
     url="https://eestn1tfeb.blogspot.com"
     self.set_font("Times", "B", 25)
     self.cell(285, 15, "Escuela Técnica N°1: Manuel Belgrano", border=1,align="C", ln=True,link=url)
     self.ln(5)
    FPDF.header = header
         
    def tabla(self):
        try:
            # Conexión a la base de datos
            self.cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='proyecto_colegio2'
            )
            self.cursor = self.cnx.cursor()
            self.cursor.execute("SELECT * FROM horarios WHERE Numero_aula=%s AND tipo_de_aula=%s",
                                (self.numero_de_aula, self.tipo_de_aula))
            self.VALORES = self.cursor.fetchall()

            self.dias_a_numeros = {"Lunes": 1, "Martes": 2, "Miercoles": 3, "Jueves": 4, "Viernes": 5}
            horarios_por_dia = {dia: [] for dia in self.dias_a_numeros.keys()}
            print(horarios_por_dia)
            for valor in self.VALORES:
                dia_numero = valor[10]
                dia_texto = list(self.dias_a_numeros.keys())[dia_numero - 1]
                horarios_por_dia[dia_texto].append(valor)

        except mysql.connector.Error as err:
            print("Error al conectarse a MySQL: {}".format(err))
            self.cursor.close()
            self.cnx.close()
            return

 

        # Encabezados
        self.pdf.set_fill_color(81, 112, 238)  
        self.pdf.cell(285,10, "Horarios", border=1,align='C',fill=1,ln=1)
        
        #cambiar fuente a la normal
        self.pdf.set_font("Arial", size=10)
        #y color
        self.pdf.set_fill_color(12, 171, 196)
        self.pdf.cell(25, 10, "Dia", border=1, align='C', fill=1)
        self.pdf.cell(25, 10, "Numero de aula", border=1, align='C', fill=1)
        self.pdf.cell(25, 10, "Tipo de aula", border=1, align='C', fill=1)
        self.pdf.cell(40, 10, "Horario entrada", border=1, align='C', fill=1)
        self.pdf.cell(40, 10, "Horario salida", border=1, align='C', fill=1)
        self.pdf.cell(40, 10, "Espacio curricular", border=1, align='C', fill=1)
        self.pdf.cell(15, 10, "Año", border=1, align='C', fill=1)
        self.pdf.cell(15, 10, "Division", border=1, align='C', fill=1)
        self.pdf.cell(15, 10, "Grupo", border=1, align='C', fill=1)
        self.pdf.cell(45, 10, "Profesor", border=1, align='C', fill=1)
        self.pdf.ln()

        self.pdf.set_fill_color(220, 220, 220)
        dia_antes=None
        fila_nueva=True
        self.c = 0 
       
        for dia, horarios in horarios_por_dia.items():
         if horarios:
            if dia == dia_antes:
                  self.pdf.cell(25,10, "",border=1,align='C',fill=0)

            else:
                fila_nueva=True
                self.pdf.cell(25,10 * len(horarios) ,str(dia),border=1,align='C',fill=0)
                dia_antes = dia

            
            
            for valor in horarios:
                if not fila_nueva:
                 self.pdf.cell(25, 10, "", border=0, align='C', fill=0)
                else:
                 fila_nueva = False  

                self.pdf.cell(25, 10, str(valor[1]), border=1, align='C', fill=1)
                self.pdf.cell(25, 10, str(valor[2]), border=1, align='C', fill=1)
                self.pdf.cell(40, 10, str(valor[3]), border=1, align='C', fill=1)
                self.pdf.cell(40, 10, str(valor[4]), border=1, align='C', fill=1)
                self.pdf.cell(40, 10, str(valor[5]), border=1, align='C', fill=1)
                self.pdf.cell(15, 10, str(valor[6]), border=1, align='C', fill=1)
                self.pdf.cell(15, 10, str(valor[7]), border=1, align='C', fill=1)
                self.pdf.cell(15, 10, str(valor[8]), border=1, align='C', fill=1)
                self.pdf.cell(45, 10, str(valor[9]), border=1, align='C', fill=1)
                self.pdf.ln()
                if self.c % 2 == 0:
                        self.pdf.set_fill_color(255, 255, 255)  
                else:
                        self.pdf.set_fill_color(220, 220, 220)  

                self.c += 1  


        #archivo
        nombre_archivo = f"Horario {self.tipo_de_aula} {self.numero_de_aula}.pdf"
        contador = 1
        while os.path.exists(nombre_archivo):
            nombre_archivo = f"({contador}) " + nombre_archivo
            contador += 1

        self.pdf.output(nombre_archivo)

        try:
            subprocess.run([nombre_archivo], shell=True)
        except Exception as e:
            print("Error al abrir el PDF:", e)
        # Obtener la carpeta de descargas del usuario
        folder_selected = os.path.join(os.path.expanduser("~"), "Downloads")
class PDF_filtro():
    def __init__(self,query):
        self.query = query
        self.pdf = FPDF(orientation='L', unit='mm', format='A4')
        self.pdf.add_page()
        self.tabla()
    
        
        
    def header(self):
        url="https://eestn1tfeb.blogspot.com"
        self.pdf.image('imagenes/colegio_logo.png',10,10,15,15,link=url)
        self.pdf.set_font("Times", "B", 25)
        self.pdf.cell(285, 15, "Escuela Técnica N°1: Manuel Belgrano", border=1,align="C", ln=True,link=url)
        self.pdf.ln(5)
         
    def tabla(self):
        try:
            # Conexión a la base de datos
            self.cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='proyecto_colegio2'
            )
            self.cursor = self.cnx.cursor()
            self.cursor.execute(self.query)
            self.VALORES = self.cursor.fetchall()

            self.dias_a_numeros = {"Lunes": 1, "Martes": 2, "Miercoles": 3, "Jueves": 4, "Viernes": 5}
            horarios_por_dia = {dia: [] for dia in self.dias_a_numeros.keys()}
            print(horarios_por_dia)
            for valor in self.VALORES:
                dia_numero = valor[10]
                dia_texto = list(self.dias_a_numeros.keys())[dia_numero - 1]
                horarios_por_dia[dia_texto].append(valor)

        except mysql.connector.Error as err:
            print("Error al conectarse a MySQL: {}".format(err))
            self.cursor.close()
            self.cnx.close()
            return

        self.header()

        # Encabezados
        self.pdf.set_fill_color(81, 112, 238)  
        self.pdf.cell(285,10, "Horarios", border=1,align='C',fill=1,ln=1)
        
        #cambiar fuente a la normal
        self.pdf.set_font("Arial", size=10)
        #y color
        self.pdf.set_fill_color(12, 171, 196)
        self.pdf.cell(25, 10, "Dia", border=1, align='C', fill=1)
        self.pdf.cell(25, 10, "Numero de aula", border=1, align='C', fill=1)
        self.pdf.cell(25, 10, "Tipo de aula", border=1, align='C', fill=1)
        self.pdf.cell(40, 10, "Horario entrada", border=1, align='C', fill=1)
        self.pdf.cell(40, 10, "Horario salida", border=1, align='C', fill=1)
        self.pdf.cell(40, 10, "Espacio curricular", border=1, align='C', fill=1)
        self.pdf.cell(15, 10, "Año", border=1, align='C', fill=1)
        self.pdf.cell(15, 10, "Division", border=1, align='C', fill=1)
        self.pdf.cell(15, 10, "Grupo", border=1, align='C', fill=1)
        self.pdf.cell(45, 10, "Profesor", border=1, align='C', fill=1)
        self.pdf.ln()

        self.pdf.set_fill_color(220, 220, 220)
        dia_antes=None
        fila_nueva=True
        self.c = 0 
       
        for dia, horarios in horarios_por_dia.items():
         if horarios:
            if dia == dia_antes:
                  self.pdf.cell(25,10, "",border=1,align='C',fill=0)

            else:
                fila_nueva=True
                self.pdf.cell(25,10 * len(horarios) ,str(dia),border=1,align='C',fill=0)
                dia_antes = dia

            
            
            for valor in horarios:
                if not fila_nueva:
                 self.pdf.cell(25, 10, "", border=0, align='C', fill=0)
                else:
                 fila_nueva = False  

                self.pdf.cell(25, 10, str(valor[1]), border=1, align='C', fill=1)
                self.pdf.cell(25, 10, str(valor[2]), border=1, align='C', fill=1)
                self.pdf.cell(40, 10, str(valor[3]), border=1, align='C', fill=1)
                self.pdf.cell(40, 10, str(valor[4]), border=1, align='C', fill=1)
                self.pdf.cell(40, 10, str(valor[5]), border=1, align='C', fill=1)
                self.pdf.cell(15, 10, str(valor[6]), border=1, align='C', fill=1)
                self.pdf.cell(15, 10, str(valor[7]), border=1, align='C', fill=1)
                self.pdf.cell(15, 10, str(valor[8]), border=1, align='C', fill=1)
                self.pdf.cell(45, 10, str(valor[9]), border=1, align='C', fill=1)
                self.pdf.ln()
                if self.c % 2 == 0:
                        self.pdf.set_fill_color(255, 255, 255)  
                else:
                        self.pdf.set_fill_color(220, 220, 220)  

                self.c += 1  


        #archivo
        nombre_archivo = f"Horario.pdf"
        contador = 1
        while os.path.exists(nombre_archivo):
            nombre_archivo = f"({contador}) " + nombre_archivo
            contador += 1

        self.pdf.output(nombre_archivo)

        try:
            subprocess.run([nombre_archivo], shell=True)
        except Exception as e:
            print("Error al abrir el PDF:", e)
            
    
    def guardar_pdf(self):
        root = Tk()
        root.withdraw()  # Ocultar la ventana principal de Tkinter

        # Mostrar diálogo de selección de carpeta
        folder_selected = filedialog.askdirectory(title="Seleccione la carpeta para guardar el PDF")

        if folder_selected:
            # Crear el nombre del archivo y la ruta completa
            nombre_archivo = f"Horario.pdf"
            ruta_completa = os.path.join(folder_selected, nombre_archivo)

            # Guardar el PDF
            self.pdf.output(ruta_completa)

            # Abrir el PDF
            try:
                subprocess.run([ruta_completa], shell=True)
            except Exception as e:
                print("Error al abrir el PDF:", e)


        #notifiacion
        toast = ToastNotifier()
        mensaje_personalizado = "Esto puede tardar un momento"
        toast.show_toast("Generando PDF en segundo plano...",mensaje_personalizado, duration=10)
if __name__ == '__main__':
    app = PDF("Laboratorio",10)