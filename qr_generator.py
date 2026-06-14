import qrcode as qr
import tkinter as tk
from PIL import Image, ImageTk


ventana = tk.Tk()
ventana.title("Ventana Interactiva")
ventana.geometry("400x500")
ventana.config(bg='white')
def mostrar_qr():
    img = Image.open("codigo_qr.png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    label_imagen.config(image=img_tk)
    label_imagen.image = img_tk
# Etiqueta 1
etiqueta = tk.Label(ventana, bg='white', fg='black', font=('Italic', 16), text="Generador QR")
etiqueta.pack(pady=10)
# Etiqueta 2
etiqueta = tk.Label(ventana, bg='white', fg='black', font=('Arial', 14), text="Escribe tu URL:")
etiqueta.pack(pady=10)
# Entrada de texto
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)
etiqueta_crear = tk.Label(ventana, bg='white', fg='black', font=('Arial', 12), text="Código QR Generado:")
etiqueta_crear.pack(pady=10)
label_imagen = tk.Label(ventana, bg='white')
label_imagen.pack(pady=10)
def crear_qr():
    url = entrada_nombre.get()
    if url:
        img = qr.make(url)
        img.save('codigo_qr.png')
        etiqueta_crear.config(font=('Arial', 10) ,text="Código QR Generado: codigo_qr.png"
                                   "\nImagen guardada en su dispositivo")
        mostrar_qr()
    else:
        etiqueta_crear.config(text="Por favor escribe una URL")

boton = tk.Button(ventana, bg='white', fg='black', font=('Arial', 12), text="Crear QR", command=crear_qr)
boton.pack(pady=10)
ventana.mainloop()

