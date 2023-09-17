import tkinter as tk

def obtener_dimensiones_pantalla():
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    return ancho_pantalla, alto_pantalla

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Frame de Pantalla Completa")

# Obtener dimensiones de la pantalla
ancho_pantalla, alto_pantalla = obtener_dimensiones_pantalla()

# Crear un Frame que ocupe toda la pantalla
frame_pantalla_completa = tk.Frame(ventana, bg="blue")
frame_pantalla_completa.place(x=0, y=0, relwidth=1, relheight=1)

# Ahora puedes agregar widgets u otros elementos al frame_pantalla_completa
etiqueta = tk.Label(frame_pantalla_completa, text="Frame de pantalla completa", fg="white")
etiqueta.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()