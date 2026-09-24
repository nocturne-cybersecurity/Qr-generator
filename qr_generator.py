import qrcode as qr
import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Ventana Interactiva")
ventana.geometry("400x570")  # Subí un poco el alto para que quepa todo bien
ventana.config(bg='white')


def mostrar_qr():
    try:
        img = Image.open("codigo_qr.png")
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        label_imagen.config(image=img_tk)
        label_imagen.image = img_tk
    except Exception as e:
        etiqueta_crear.config(text=f"Error al cargar imagen: {e}")


def crear_qr():
    url = entrada_nombre.get()
    if url.strip():  # .strip() evita que solo envíes espacios en blanco
        try:
            # Genera el QR usando la librería
            img = qr.make(url)
            img.save('codigo_qr.png')

            etiqueta_crear.config(
                font=('Arial', 10),
                text="Código QR Generado: codigo_qr.png\nImagen guardada en su dispositivo"
            )
            mostrar_qr()
        except AttributeError:
            etiqueta_crear.config(text="Error: Revisa que no tengas un archivo llamado qrcode.py")
    else:
        etiqueta_crear.config(text="Por favor escribe una URL válida")


# Etiqueta 1
etiqueta = tk.Label(ventana, bg='white', fg='black', font=('Arial', 16, 'italic'), text="Generador QR")
etiqueta.pack(pady=10)

# Etiqueta 2
etiqueta_url = tk.Label(ventana, bg='white', fg='black', font=('Arial', 14), text="Escribe tu URL:")
etiqueta_url.pack(pady=10)

# Entrada de texto
entrada_nombre = tk.Entry(ventana, font=('Arial', 12), width=30)
entrada_nombre.pack(pady=5)

# Botón para crear (Debe ir antes de la acción o después de definir las funciones)
boton = tk.Button(ventana, bg='lightgray', fg='black', font=('Arial', 12), text="Crear QR", command=crear_qr)
boton.pack(pady=10)

# Sección de resultado
etiqueta_crear = tk.Label(ventana, bg='white', fg='black', font=('Arial', 12), text="Código QR Generado:")
etiqueta_crear.pack(pady=10)

label_imagen = tk.Label(ventana, bg='white')
label_imagen.pack(pady=10)

ventana.mainloop()
