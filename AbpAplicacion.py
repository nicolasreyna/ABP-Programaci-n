import tkinter as tk
from tkinter import ttk
import os

# --- CONFIGURACIÓN DE RUTAS ---
carpeta_proyecto = os.path.dirname(__file__)
ruta_logo = os.path.join(carpeta_proyecto, "LOGO APP.png")


# Envolvemos todo en una función para que el Login pueda llamarla
def mostrar_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Almacen gestionario de Don Mario")
    ventana_principal.minsize(1200, 500)
    ventana_principal.resizable(False, False)
    ventana_principal.configure(bg="darkslategray")

    try:
        Logo_App_Main = tk.PhotoImage(file=ruta_logo)
        ventana_principal.iconphoto(False, Logo_App_Main)
    except Exception:
        pass

    titulo = ttk.Label(
        ventana_principal,
        text="Almacén de Don Mario",
        font=("Times New Roman", 20),
        background="darkslategray",
        foreground="white",
    ).pack(pady=15)

    ttk.Label(
        ventana_principal,
        text="Cliente",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
    ).place(x=10, y=64) #cambio de pack a place y las medidas

    ttk.Label(
        ventana_principal,
        text="Producto",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
        ).place(x=1100, y=64)

    ttk.Label(ventana_principal,
        text="DNI:",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
        ).place(x=10, y=100) #cambio de pack a place 
    #Asignamos a variable        
    entrada_dni = ttk.Entry(ventana_principal)
    entrada_dni.place(x=60, y=105)


        #       agregue este para asignar la variable a la entrada de nombre del cliente
    ttk.Label(
        ventana_principal,
        text="Nombre:",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
    ).place(x=195, y=100)
    #                  Aagregue la variable pase el ttk.Entry(ventana_principal, width=50).place(x=1005, y=135)
    entrada_nombre_cliente = ttk.Entry(ventana_principal, width=20)
    entrada_nombre_cliente.place(x=280, y=105)

    ttk.Label(
        ventana_principal,
        text="Metodo De Pago:",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
    ).place(x=0, y=135)

    opciones = ["Crédito", "Transferencia", "Débito"] #podriamos agregar efectivo
    combo_pago =ttk.Combobox(ventana_principal, values=opciones, state="readonly")
    combo_pago.place(x=167, y=140)

    ttk.Label(
        ventana_principal,
        text="Código:",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
    ).place(x=926, y=100)   
    entrada_codigo = ttk.Entry(ventana_principal, width=20) #agregada la variable para la entrada de codigo del producto
    entrada_codigo.place(x=1000, y=105)

    ttk.Label(
        ventana_principal,
        text="Nombre:",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
    ).place(x=926, y=130) #cambiamos de pack  a place
    
    entrada_nombre_producto = ttk.Entry(ventana_principal)
    entrada_nombre_producto.place(x=1005, y=135)

    ttk.Label(
      ventana_principal,
      text="Apellido:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 15),
     ).place(x=420, y=100)

    entrada_apellido_cliente = ttk.Entry(ventana_principal)  #  agregue este para asignar la variable a la entrada de nombre del cliente
    entrada_apellido_cliente.place(x=500, y=105)


    ttk.Label(
        ventana_principal,
        text="Precio:",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
    ).place(x=926, y=160)
    entrada_precio = ttk.Entry(ventana_principal, width=20)
    entrada_precio.place(x=990, y=165)

    ttk.Label(
        ventana_principal,
        text="Stock:",
        background="darkslategray",
        foreground="white",
        font=("Arial", 15),
    ).place(x=926, y=190)
    entrada_stock = ttk.Entry(ventana_principal, width=20)
    entrada_stock.place(x=985, y=195)

    #Tabla clietes
    Columnas_Cliente = ["dni", "Nombre", "Apellido", "Pago"]
    tabla_Cliente = ttk.Treeview(
        ventana_principal, columns=Columnas_Cliente, show="headings"
    )

    tabla_Cliente.heading("dni", text="DNI")
    tabla_Cliente.heading("Nombre", text="NOMBRE")
    tabla_Cliente.heading("Apellido", text="APELLIDO")
    tabla_Cliente.heading("Pago", text="PAGO")

    tabla_Cliente.column("dni", width=100)
    tabla_Cliente.column("Nombre", width=150)
    tabla_Cliente.column("Apellido", width=150)
    tabla_Cliente.column("Pago", width=120)
    tabla_Cliente.place(x=10, y=200)

    tabla_Cliente.insert(
        "", "end", values=("30111222", "Juan", "Pérez", "Transferencia")
    )
    tabla_Cliente.insert(
        "", "end", values=("28555999", "María", "Gómez", "Debito")
    )
    

    #Tabla producto
    columnas = ("codigo", "nombre", "precio", "stock")
    tabla_producto = ttk.Treeview(
        ventana_principal, columns=columnas, show="headings"
    )

    tabla_producto.heading("codigo", text="Código")
    tabla_producto.heading("nombre", text="Producto")
    tabla_producto.heading("precio", text="Precio")
    tabla_producto.heading("stock", text="Stock")

    tabla_producto.column("codigo", width=90)
    tabla_producto.column("nombre", width=180)
    tabla_producto.column("precio", width=100)
    tabla_producto.column("stock", width=90)

    tabla_producto.insert(
        "", "end", values=("P001", "Arroz 1kg", "$1500", "2", "$3000")
    )
    tabla_producto.insert(
        "", "end", values=("P002", "Fideos 500g", "$900", "1", "$900")
    )
    tabla_producto.place(x=700, y=270)

    #Funciones de los botones
    def agregar_cliente():
        # Obtenemos los valores de los Entry
        dni = entrada_dni.get()
        nombre = entrada_nombre_cliente.get()
        apellido = entrada_apellido_cliente.get()
        pago = combo_pago.get()
        
        # Si no están vacíos, agregamos a la tabla
        if dni and nombre and apellido and pago:
            tabla_Cliente.insert("", tk.END, values=(dni, nombre, apellido, pago))
            # Limpiamos los campos
            entrada_dni.delete(0, tk.END)
            entrada_nombre_cliente.delete(0, tk.END)
            entrada_apellido_cliente.delete(0, tk.END)
            combo_pago.set('')

    def agregar_producto():
        codigo = entrada_codigo.get()
        nombre = entrada_nombre_producto.get()
        precio = entrada_precio.get()
        stock = entrada_stock.get()
        
        if codigo and nombre and precio and stock:
            tabla_producto.insert("", tk.END, values=(codigo, nombre, precio, stock))
            entrada_codigo.delete(0, tk.END)
            entrada_nombre_producto.delete(0, tk.END)
            entrada_precio.delete(0, tk.END)
            entrada_stock.delete(0, tk.END)

    #  Botones
    btn_add_cliente = ttk.Button(ventana_principal, text="Agregar Cliente", command=agregar_cliente)
    btn_add_cliente.place(x=350, y=140)

    btn_add_producto = ttk.Button(ventana_principal, text="Agregar Producto", command=agregar_producto)
    btn_add_producto.place(x=985, y=230)


    ventana_principal.mainloop()