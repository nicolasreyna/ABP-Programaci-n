import os
import tkinter as tk
from tkinter import ttk


carpeta_proyecto = os.path.dirname(__file__)
ruta_logo = os.path.join(carpeta_proyecto, "LOGO APP.png")


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

  # Título Principal
  titulo = ttk.Label(
      ventana_principal,
      text="Almacén de Don Mario",
      font=("Times New Roman", 20, "bold"),
      background="darkslategray",
      foreground="white",
  )
  titulo.pack(pady=15)

  
  container = tk.Frame(ventana_principal, bg="darkslategray")
  container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

  # ==================== CLIENTES ====================
  left_frame = tk.Frame(container, bg="darkslategray", bd=5, relief="groove")
  left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))

  ttk.Label(
      left_frame,
      text="Cliente",
      background="darkslategray",
      foreground="white",
      font=("Arial", 15, "bold"),
  ).pack(anchor="w", pady=(0, 10))

  
  client_form = tk.Frame(left_frame, bg="darkslategray")
  client_form.pack(fill=tk.X, pady=5)

  ttk.Label(
      client_form,
      text="DNI:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 11),
  ).pack(anchor="w")
  entrada_dni = ttk.Entry(client_form)
  entrada_dni.pack(fill=tk.X, pady=(0, 6))

  ttk.Label(
      client_form,
      text="Nombre:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 11),
  ).pack(anchor="w")
  entrada_nombre_cliente = ttk.Entry(client_form)
  entrada_nombre_cliente.pack(fill=tk.X, pady=(0, 6))

  ttk.Label(
      client_form,
      text="Apellido:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 11),
  ).pack(anchor="w")
  entrada_apellido_cliente = ttk.Entry(client_form)
  entrada_apellido_cliente.pack(fill=tk.X, pady=(0, 6))

  ttk.Label(
      client_form,
      text="Método De Pago:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 11),
  ).pack(anchor="w")
  opciones = ["Crédito", "Transferencia", "Débito", "Efectivo"]
  combo_pago = ttk.Combobox(
      client_form, values=opciones, state="readonly"
  )
  combo_pago.pack(fill=tk.X, pady=(0, 10))

  
  def agregar_cliente():
    dni = entrada_dni.get()
    nombre = entrada_nombre_cliente.get()
    apellido = entrada_apellido_cliente.get()
    pago = combo_pago.get()

    if dni and nombre and apellido and pago:
      tabla_Cliente.insert("", tk.END, values=(dni, nombre, apellido, pago))
      entrada_dni.delete(0, tk.END)
      entrada_nombre_cliente.delete(0, tk.END)
      entrada_apellido_cliente.delete(0, tk.END)
      combo_pago.set("")

  
  btn_add_cliente = tk.Button(
      client_form,
      text="Agregar Cliente",
      command=agregar_cliente,
      bg="forestgreen",
      fg="white",
      activebackground="green",
      activeforeground="white",
      font=("Arial", 10, "bold"),
      cursor="hand2",
  )
  btn_add_cliente.pack(anchor="w", pady=(0, 15))

  
  Columnas_Cliente = ["dni", "Nombre", "Apellido", "Pago"]
  tabla_Cliente = ttk.Treeview(
      left_frame, columns=Columnas_Cliente, show="headings", height=8
  )
  tabla_Cliente.heading("dni", text="DNI")
  tabla_Cliente.heading("Nombre", text="NOMBRE")
  tabla_Cliente.heading("Apellido", text="APELLIDO")
  tabla_Cliente.heading("Pago", text="PAGO")

  tabla_Cliente.column("dni", width=100, anchor="center")
  tabla_Cliente.column("Nombre", width=130, anchor="w")
  tabla_Cliente.column("Apellido", width=130, anchor="w")
  tabla_Cliente.column("Pago", width=110, anchor="center")
  tabla_Cliente.pack(fill=tk.BOTH, expand=True)

  tabla_Cliente.insert(
      "", "end", values=("30111222", "Juan", "Pérez", "Transferencia")
  )
  tabla_Cliente.insert("", "end", values=("28555999", "María", "Gómez", "Debito"))

  # ====================  PRODUCTOS ====================
  right_frame = tk.Frame(container, bg="darkslategray", bd=5, relief="groove")
  right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(15, 0))

  ttk.Label(
      right_frame,
      text="Producto",
      background="darkslategray",
      foreground="white",
      font=("Arial", 15, "bold"),
  ).pack(anchor="w", pady=(0, 10))

  
  product_form = tk.Frame(right_frame, bg="darkslategray")
  product_form.pack(fill=tk.X, pady=5)

  ttk.Label(
      product_form,
      text="Código:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 11),
  ).pack(anchor="w")
  entrada_codigo = ttk.Entry(product_form)
  entrada_codigo.pack(fill=tk.X, pady=(0, 6))

  ttk.Label(
      product_form,
      text="Nombre:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 11),
  ).pack(anchor="w")
  entrada_nombre_producto = ttk.Entry(product_form)
  entrada_nombre_producto.pack(fill=tk.X, pady=(0, 6))

  ttk.Label(
      product_form,
      text="Precio:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 11),
  ).pack(anchor="w")
  entrada_precio = ttk.Entry(product_form)
  entrada_precio.pack(fill=tk.X, pady=(0, 6))

  ttk.Label(
      product_form,
      text="Stock:",
      background="darkslategray",
      foreground="white",
      font=("Arial", 11),
  ).pack(anchor="w")
  entrada_stock = ttk.Entry(product_form)
  entrada_stock.pack(fill=tk.X, pady=(0, 10))

  
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

  
  btn_add_producto = tk.Button(
      product_form,
      text="Agregar Producto",
      command=agregar_producto,
      bg="forestgreen",
      fg="white",
      activebackground="green",
      activeforeground="white",
      font=("Arial", 10, "bold"),
      cursor="hand2",
  )
  btn_add_producto.pack(anchor="w", pady=(0, 15))

  # Tabla Productos
  columnas = ("codigo", "nombre", "precio", "stock")
  tabla_producto = ttk.Treeview(
      right_frame, columns=columnas, show="headings", height=8
  )
  tabla_producto.heading("codigo", text="Código")
  tabla_producto.heading("nombre", text="Producto")
  tabla_producto.heading("precio", text="Precio")
  tabla_producto.heading("stock", text="Stock")

  tabla_producto.column("codigo", width=90, anchor="center")
  tabla_producto.column("nombre", width=150, anchor="w")
  tabla_producto.column("precio", width=100, anchor="e")
  tabla_producto.column("stock", width=90, anchor="center")
  tabla_producto.pack(fill=tk.BOTH, expand=True)

  tabla_producto.insert("", "end", values=("P001", "Arroz 1kg", "$1500", "2"))
  tabla_producto.insert("", "end", values=("P002", "Fideos 500g", "$900", "1"))

  ventana_principal.mainloop()


if __name__ == "__main__":
  mostrar_ventana_principal()