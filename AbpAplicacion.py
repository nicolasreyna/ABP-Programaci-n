import tkinter as tk
from tkinter import ttk

ventana_principal = tk.Tk()
ventana_principal.title("Almacen gestionario de Don Mario")
ventana_principal.minsize(1200,500)
ventana_principal.resizable(False, False)
ventana_principal.configure(bg="darkslategray")

Logo_App = tk.PhotoImage(file="C:/Users/Lucas/Desktop/AbpProyecto/LOGO APP.png")
ventana_principal.iconphoto(False,Logo_App)



titulo = ttk.Label(
        ventana_principal,
        text="Almacén de Don Mario",
        font=("Times New Roman", 20),
        background="darkslategray",
        foreground="white"
    ).pack(pady=15)

ttk.Label(ventana_principal, text="Cliente", background="darkslategray", foreground="white",font=("Arial",15)).pack(padx=0, pady=0, fill="x")
ttk.Label(ventana_principal, text="Producto", background="darkslategray", foreground="white",font=("Arial",15)).place(x=1100,y=64)

ttk.Label(ventana_principal, text="DNI:", background="darkslategray", foreground="white", font=("Arial",15)).pack(padx=0, pady=10, fill="x")
ttk.Entry(ventana_principal).place(x=55,y=105)

ttk.Label(ventana_principal, text="Metodo De Pago:", background="darkslategray", foreground="white", font=("Arial",15)).place(x=0,y=135)

opciones = ["Crédito","Transferencia","Débito"]

ttk.Combobox(ventana_principal,values=opciones,state="readonly").place(x=167,y=140)

ttk.Label(ventana_principal, text="Código:", background="darkslategray",foreground="white",font=("Arial",15) ).place(x=926, y=100)
ttk.Entry(ventana_principal, width=50).place(x=1000,y=105)

ttk.Label(ventana_principal, text="Nombre:", background="darkslategray",foreground="white",font=("Arial",15) ).place(x=926, y=130)
ttk.Entry(ventana_principal, width=50).place(x=1005,y=135)

ttk.Label(ventana_principal, text="Precio:", background="darkslategray",foreground="white",font=("Arial",15) ).place(x=926, y=160)
ttk.Entry(ventana_principal, width=50).place(x=990,y=165)

ttk.Label(ventana_principal, text="Stock:", background="darkslategray",foreground="white",font=("Arial",15) ).place(x=926, y=190)
ttk.Entry(ventana_principal, width=50).place(x=985,y=195)

Columnas_Cliente = ["dni", "Nombre", "Apellido", "Pago"]
tabla_Cliente = ttk.Treeview(ventana_principal, columns=Columnas_Cliente, show="headings")

tabla_Cliente.heading("dni", text="DNI")
tabla_Cliente.heading("Nombre", text="NOMBRE")
tabla_Cliente.heading("Apellido", text="APELLIDO")
tabla_Cliente.heading("Pago", text="PAGO")

tabla_Cliente.column("dni", width=100)
tabla_Cliente.column("Nombre", width=150)
tabla_Cliente.column("Apellido", width=150)
tabla_Cliente.column("Pago", width=120)

tabla_Cliente.insert("", "end", values=("30111222", "Juan", "Pérez", "Transferencia"))
tabla_Cliente.insert("", "end", values=("28555999", "María", "Gómez", "Debito"))

tabla_Cliente.place(x=0,y=170)



columnas = ("codigo", "nombre", "precio", "stock")
tabla_producto = ttk.Treeview(ventana_principal, columns=columnas, show="headings")

tabla_producto.heading("codigo", text="Código")
tabla_producto.heading("nombre", text="Producto")
tabla_producto.heading("precio", text="Precio")
tabla_producto.heading("stock", text="Stock")


tabla_producto.column("codigo", width=90)
tabla_producto.column("nombre", width=180)
tabla_producto.column("precio", width=100)
tabla_producto.column("stock", width=90)


tabla_producto.insert("", "end", values=("P001", "Arroz 1kg", "$1500", "2", "$3000"))
tabla_producto.insert("", "end", values=("P002", "Fideos 500g", "$900", "1", "$900"))

tabla_producto.place(x=738,y=220)

ventana_principal.mainloop()
