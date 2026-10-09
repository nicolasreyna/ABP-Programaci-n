import os
import tkinter as tk
from tkinter import ttk, messagebox
from CicloDeCompras import Proveedor, Compra
from Ventas import Ventas
carpeta_proyecto = os.path.dirname(__file__)
ruta_logo = os.path.join(carpeta_proyecto, "LOGO APP.png")

def Cliente(parent: tk.Frame):
    
    left_frame = tk.Frame(parent, bg="black", bd=5, relief="groove")
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

    ttk.Label(
        left_frame,
        text="Cliente",
        background="black",
        foreground="white",
        font=("Arial", 15, "bold"),
    ).pack(anchor="w", padx=10, pady=(10, 6))

    # ── Formulario ──
    form = tk.Frame(left_frame, bg="black")
    form.pack(fill=tk.X, padx=10, pady=5)

    def campo(label_text: str):
        ttk.Label(
            form,
            text=label_text,
            background="black",
            foreground="white",
            font=("Arial", 11),
        ).pack(anchor="w")
        entry = ttk.Entry(form)
        entry.pack(fill=tk.X, pady=(0, 6))
        return entry

    entrada_dni     = campo("DNI:")
    entrada_nombre  = campo("Nombre:")
    entrada_apellido = campo("Apellido:")

    ttk.Label(
        form,
        text="Método De Pago:",
        background="black",
        foreground="white",
        font=("Arial", 11),
    ).pack(anchor="w")
    combo_pago = ttk.Combobox(
        form,
        values=["Crédito", "Transferencia", "Débito", "Efectivo"],
        state="readonly",
    )
    combo_pago.pack(fill=tk.X, pady=(0, 10))

    # ── Tabla ──
    columnas = ("dni", "Nombre", "Apellido", "Pago")
    tabla = ttk.Treeview(left_frame, columns=columnas, show="headings", height=8, selectmode="browse")
    for col, ancho, anchor in [
        ("dni",      100, "center"),
        ("Nombre",   130, "w"),
        ("Apellido", 130, "w"),
        ("Pago",     110, "center"),
    ]:
        tabla.heading(col, text=col.upper())
        tabla.column(col, width=ancho, anchor=anchor)
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # Datos de ejemplo
    tabla.insert("", "end", values=("30111222", "Juan",  "Pérez", "Transferencia"))
    tabla.insert("", "end", values=("28555999", "María", "Gómez", "Débito"))

    # ── Lógica de agregar ──
    def agregar_cliente():
        dni      = entrada_dni.get().strip()
        nombre   = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()
        pago     = combo_pago.get()

        if not dni.isdigit() or len(dni) > 8:
            messagebox.showerror(
                "DNI inválido",
                "El DNI debe contener solo números y tener como máximo 8 dígitos.",
            )
            return

        if not all([dni, nombre, apellido, pago]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        tabla.insert("", tk.END, values=(dni, nombre, apellido, pago))
        for entry in (entrada_dni, entrada_nombre, entrada_apellido):
            entry.delete(0, tk.END)
        combo_pago.set("")

    # ── Cargar cliente seleccionado en el formulario ──
    def cargar_cliente(event=None) -> None:
        seleccion = tabla.selection()

        for entry in (entrada_dni, entrada_nombre, entrada_apellido):
            entry.delete(0, tk.END)
        combo_pago.set("")

        if not seleccion:
            return

        dni, nombre, apellido, pago = tabla.item(seleccion[0], "values")
        entrada_dni.insert(0, str(dni))
        entrada_nombre.insert(0, nombre)
        entrada_apellido.insert(0, apellido)
        combo_pago.set(pago)

    tabla.bind("<<TreeviewSelect>>", cargar_cliente)

    # ── Lógica de modificar ──
    def modificar_cliente():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccioná un cliente de la tabla para modificarlo.",
            )
            return

        dni      = entrada_dni.get().strip()
        nombre   = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()
        pago     = combo_pago.get()

        if not all([dni, nombre, apellido, pago]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        if not dni.isdigit() or len(dni) > 8:
            messagebox.showerror(
                "DNI inválido",
                "El DNI debe contener solo números y tener como máximo 8 dígitos.",
            )
            return

        tabla.item(seleccion[0], values=(dni, nombre, apellido, pago))
        tabla.selection_remove(seleccion)  # deselecciona y limpia el formulario

    # ── Lógica de borrar ──
    def borrar_cliente():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccioná un cliente de la tabla para borrarlo.",
            )
            return

        # Armamos el mensaje con los datos del cliente elegido
        dni, nombre, apellido, _ = tabla.item(seleccion[0], "values")
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que querés borrar a {nombre} {apellido} (DNI {dni})?",
        )

        if confirmar:
            for item in seleccion:
                tabla.delete(item)
            tabla.event_generate("<<TreeviewSelect>>")


    # ── Botones ──
    frame_botones = tk.Frame(form, bg="black")
    frame_botones.pack(anchor="w", pady=(0, 12))

    tk.Button(
        frame_botones,
        text="Agregar Cliente",
        command=agregar_cliente,
        bg="forestgreen", fg="white",
        activebackground="green", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT, padx=(0, 10))

    tk.Button(
        frame_botones,
        text="Modificar Cliente",
        command=modificar_cliente,
        bg="royalblue", fg="white",
        activebackground="navy", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT, padx=(0, 10))

    tk.Button(
        frame_botones,
        text="Borrar Cliente",
        command=borrar_cliente,
        bg="firebrick", fg="white",
        activebackground="darkred", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT)


def Producto(parent: tk.Frame):
    """Sección de gestión de productos (panel derecho)."""

    right_frame = tk.Frame(parent, bg="black", bd=5, relief="groove")
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

    ttk.Label(
        right_frame,
        text="Producto",
        background="black",
        foreground="white",
        font=("Arial", 15, "bold"),
    ).pack(anchor="w", padx=10, pady=(10, 6))

    # ── Formulario ──
    form = tk.Frame(right_frame, bg="black")
    form.pack(fill=tk.X, padx=10, pady=5)

    def campo(label_text: str):
        ttk.Label(
            form,
            text=label_text,
            background="black",
            foreground="white",
            font=("Arial", 11),
        ).pack(anchor="w")
        entry = ttk.Entry(form)
        entry.pack(fill=tk.X, pady=(0, 6))
        return entry

    entrada_codigo  = campo("Código:")
    entrada_nombre  = campo("Nombre:")
    entrada_precio  = campo("Precio:")
    entrada_stock   = campo("Stock:")

    
    columnas = ("codigo", "nombre", "precio", "stock")
    tabla = ttk.Treeview(right_frame, columns=columnas, show="headings", height=8, selectmode="browse")
    for col, texto, ancho, anchor in [
        ("codigo", "Código",   90,  "center"),
        ("nombre", "Producto", 150, "w"),
        ("precio", "Precio",   100, "e"),
        ("stock",  "Stock",    90,  "center"),
    ]:
        tabla.heading(col, text=texto)
        tabla.column(col, width=ancho, anchor=anchor)
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # Datos de ejemplo
    tabla.insert("", "end", values=("P001", "Arroz 1kg",   "$1500", "2"))
    tabla.insert("", "end", values=("P002", "Fideos 500g", "$900",  "1"))

    def agregar_producto():
        codigo = entrada_codigo.get().strip()
        nombre = entrada_nombre.get().strip()
        precio = entrada_precio.get().strip()
        stock  = entrada_stock.get().strip()

        if not all([codigo, nombre, precio, stock]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        try:
            precio_val = float(precio)
            stock_val  = int(stock)
        except ValueError:
            messagebox.showerror(
                "Valores inválidos",
                "El precio debe ser un número (ej: 1500.50) y el stock un número entero.",
            )
            return

        if precio_val < 0 or stock_val < 0:
            messagebox.showerror("Error", "El precio y el stock no pueden ser negativos.")
            return

        tabla.insert("", tk.END, values=(codigo, nombre, f"${precio_val:.2f}", stock_val))
        for entry in (entrada_codigo, entrada_nombre, entrada_precio, entrada_stock):
            entry.delete(0, tk.END)


    # ── Cargar producto seleccionado en el formulario ──
    def cargar_producto(event=None):
        seleccion = tabla.selection()

        for entry in (entrada_codigo, entrada_nombre, entrada_precio, entrada_stock):
            entry.delete(0, tk.END)

        if not seleccion:
            return

        codigo, nombre, precio, stock = tabla.item(seleccion[0], "values")
        entrada_codigo.insert(0, codigo)
        entrada_nombre.insert(0, nombre)
        entrada_precio.insert(0, str(precio).lstrip("$"))  # sacamos el "$" para poder validarlo
        entrada_stock.insert(0, stock)

    tabla.bind("<<TreeviewSelect>>", cargar_producto)

    # ── Lógica de modificar ──
    def modificar_producto():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccioná un producto de la tabla para modificarlo.",
            )
            return

        codigo = entrada_codigo.get().strip()
        nombre = entrada_nombre.get().strip()
        precio = entrada_precio.get().strip()
        stock  = entrada_stock.get().strip()

        if not all([codigo, nombre, precio, stock]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        try:
            precio_val = float(precio)
            stock_val  = int(stock)
        except ValueError:
            messagebox.showerror(
                "Valores inválidos",
                "El precio debe ser un número (ej: 1500.50) y el stock un número entero.",
            )
            return

        if precio_val < 0 or stock_val < 0:
            messagebox.showerror("Error", "El precio y el stock no pueden ser negativos.")
            return

        tabla.item(seleccion[0], values=(codigo, nombre, f"${precio_val:.2f}", stock_val))
        tabla.selection_remove(seleccion)

# ── Lógica de borrar ──
    def borrar_producto():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccioná un producto de la tabla para borrarlo.",
            )
            return

        codigo, nombre, _, _ = tabla.item(seleccion[0], "values")
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que querés borrar el producto {nombre} (código {codigo})?",
        )

        if confirmar:
            tabla.delete(seleccion[0])
            tabla.event_generate("<<TreeviewSelect>>")

    frame_botones = tk.Frame(form, bg="black")
    frame_botones.pack(anchor="w", pady=(0, 12))

    tk.Button(
        frame_botones,
        text="Agregar Producto",
        command=agregar_producto,
        bg="forestgreen", fg="white",
        activebackground="green", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT, padx=(0, 10))

    tk.Button(
        frame_botones,
        text="Modificar Producto",
        command=modificar_producto,
        bg="royalblue", fg="white",
        activebackground="navy", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT, padx=(0, 10))

    tk.Button(
        frame_botones,
        text="Borrar Producto",
        command=borrar_producto,
        bg="firebrick", fg="white",
        activebackground="darkred", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT)

    

def mostrar_ventana_principal():
    ventana = tk.Tk()
    ventana.title("Almacen gestionario de Don Mario")
    ventana.minsize(1200, 500)
    ventana.resizable(False, False)
    ventana.configure(bg="black")

    try:
        logo = tk.PhotoImage(file=ruta_logo)
        ventana.iconphoto(False, logo)
    except Exception:
        pass

    ttk.Label(
        ventana,
        text="Almacén de Don Mario",
        font=("Times New Roman", 20, "bold"),
        background="black",
        foreground="chartreuse2",
    ).pack(pady=15)

    # Frame compartido donde viven Cliente y Producto lado a lado ← CLAVE
    main_frame = tk.Frame(ventana, bg="black")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    #hacemos style para el notebook y sus pestañas para que se vea negro y no blanco 
    style = ttk.Style()
    style.theme_use("default")  # importante: sin esto el color puede no aplicar
    style.configure("TNotebook", background="black")
    style.configure("TNotebook.Tab", background="black", foreground="white")
    style.map("TNotebook.Tab",
              background=[("selected", "black")],  # color de la pestaña activa
              foreground=[("selected", "chartreuse3")],
              )

  # ponemos en frame al notebook para que se noten que los bordes tienen el efecto groove. ya que no hay un tk.notebook para poner relief= o bd=.
    frame_notebook = tk.Frame(ventana, bg="black", bd=5, relief="groove")
    frame_notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    notebook = ttk.Notebook(frame_notebook, style="TNotebook")
    notebook.pack(fill=tk.BOTH, expand=True)

    tab_CL_PR = tk.Frame(notebook, bg="black")
    notebook.add(tab_CL_PR, text="  Clientes y Productos  ")
    main_frame_ventas = tk.Frame(tab_CL_PR, bg="black")
    main_frame_ventas.pack(fill=tk.BOTH, expand=True)

    Cliente(main_frame_ventas)
    Producto(main_frame_ventas)

    tab_compra = tk.Frame(notebook, bg="black")
    notebook.add(tab_compra, text="  Ciclo de Compra  ")
    main_frame_compra = tk.Frame(tab_compra, bg="black")
    main_frame_compra.pack(fill=tk.BOTH, expand=True)

    Proveedor(main_frame_compra)
    Compra(main_frame_compra)


    tab_ventas = tk.Frame(notebook, bg="black")
    notebook.add(tab_ventas, text="Ventas")
    main_frame_ventas = tk.Frame(tab_ventas, bg="black")
    main_frame_ventas.pack(fill=tk.BOTH, expand=True)

    Ventas(main_frame_ventas)


    ventana.mainloop()


if __name__ == "__main__":
    mostrar_ventana_principal()