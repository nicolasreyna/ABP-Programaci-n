# login.py
import tkinter as tk
from tkinter import messagebox, ttk
import os

# --- AQUÍ HACEMOS EL IMPORT ---
# Importamos la función 'mostrar_ventana_principal' desde el archivo 'abp_aplicacion.py'
from AbpAplicacion import mostrar_ventana_principal

# --- CONFIGURACIÓN DE RUTAS ---
carpeta_proyecto = os.path.dirname(__file__)
ruta_logo = os.path.join(carpeta_proyecto, "LOGO APP.png")

intentos_restantes = 3


def verificar_contrasena():
    global intentos_restantes
    entrada = entrada_pass.get()

    if entrada == "1234":
        ventana_login.destroy()  # Cierra la ventana de login
        mostrar_ventana_principal()  # LLAMAMOS A LA FUNCIÓN IMPORTADA AQUÍ
    else:
        intentos_restantes -= 1
        if intentos_restantes > 0:
            messagebox.showerror(
                "Error",
                f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos.",
            )
            entrada_pass.delete(0, tk.END)
        else:
            messagebox.showerror(
                "Acceso Denegado",
                "Has agotado los 3 intentos. La aplicación se cerrará.",
            )
            ventana_login.destroy()


# --- VENTANA DE LOGIN ---
ventana_login = tk.Tk()
ventana_login.title("Acceso al Sistema")
ventana_login.geometry("400x200")
ventana_login.resizable(False, False)
ventana_login.configure(bg="darkslategray")

try:
    Logo_App = tk.PhotoImage(file=ruta_logo)
    ventana_login.iconphoto(False, Logo_App)
except Exception:
    pass

lbl_titulo = tk.Label(
    ventana_login,
    text="Ingrese la Contraseña",
    font=("Arial", 14, "bold"),
    bg="darkslategray",
    foreground="white",
)
lbl_titulo.pack(pady=20)

entrada_pass = ttk.Entry(ventana_login, show="*", font=("Arial", 12), width=20)
entrada_pass.pack(pady=10)
entrada_pass.focus()

entrada_pass.bind("<Return>", lambda event: verificar_contrasena())

btn_ingresar = ttk.Button(
    ventana_login, text="Ingresar", command=verificar_contrasena
)
btn_ingresar.pack(pady=10)

ventana_login.mainloop()