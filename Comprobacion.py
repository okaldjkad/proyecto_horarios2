import mysql.connector
from tkinter import messagebox

class comprobacion:
    def __init__(self):
        with open('database.txt', 'r') as archivo:
            self.database_var = archivo.read()
        with open("tecnica_2023.sql", "r", encoding='utf-8') as archivo_sql:
            self.consulta_sql = archivo_sql.read()
        try:
            self.cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
            )
            self.cursor = self.cnx.cursor()

            self.cursor.execute("SHOW DATABASES")
            databases = [row[0] for row in self.cursor.fetchall()]
            if self.database_var not in databases:
                self.cursor.execute(f"CREATE DATABASE {self.database_var}")
                self.cursor.execute(f"USE {self.database_var}")
                consultas = []
                consulta_actual = ""
                dentro_de_comillas = False
                for caracter in self.consulta_sql:
                    consulta_actual += caracter
                    if caracter == "'":
                        dentro_de_comillas = not dentro_de_comillas
                    elif caracter == ';' and not dentro_de_comillas:
                        consultas.append(consulta_actual.strip())
                        consulta_actual = ""

                for statement in consultas:
                    self.cursor.execute(statement)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
        except Exception as e:
            if "1046 (3D000): No database selected" in str(e):
                # Manejar el error de base de datos no seleccionada aquí
                print("No se ha seleccionado una base de datos.")
                # Puedes ejecutar código alternativo aquí si es necesario
            else:
                print(e)
                messagebox.showerror("Error", "No se pudo conectar a la base de datos, abrir el XAMPP")

if __name__ == "__main__":
    comprobacion_instancia = comprobacion()
