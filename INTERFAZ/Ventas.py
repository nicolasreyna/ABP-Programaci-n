import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

carpeta_proyecto = os.path.dirname(__file__)
ruta_logo = os.path.join(carpeta_proyecto, "LOGO APP.png")

def Ventas(parent):
    """Entidad: VENTAS (id_venta PK, fecha_hora, monto_total, id_cliente FK, id_vendedor FK)"""

    Frame_principal = tk.Frame(parent, bg="black", bd=5, relief="groove")
    Frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    ttk.Label(
        Frame_principal,
        text="Ventas",
        background="black",
        foreground="white",
        font=("Arial", 15, "bold"),
    ).pack(anchor="w", padx=10, pady=5)

    # ── Formulario ──
    form = tk.Frame(Frame_principal, bg="black")
    form.pack(fill=tk.X, padx=10, pady=5)

    def campo(parent_frame, label_text):
        contenedor = tk.Frame(parent_frame, bg="black")
        contenedor.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=(0, 10))
        ttk.Label(
            contenedor,
            text=label_text,
            background="black",
            foreground="white",
            font=("Arial", 11),
        ).pack(anchor="w")
        entry = ttk.Entry(contenedor)
        entry.pack(fill=tk.X)
        return entry

    entrada_monto_total  = campo(form, "Monto Total ($):")
    entrada_id_cliente   = campo(form, "ID Cliente (FK):")
    entrada_id_vendedor  = campo(form, "ID Vendedor (FK):")

    
    frame_tabla = tk.Frame(Frame_principal, bg="black")
    frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    columnas = ("id_venta", "fecha_hora", "monto_total", "id_cliente", "id_vendedor")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=15, selectmode="browse")
    for col, texto, ancho, anchor in [
        ("id_venta",     "ID Venta",     80,  "center"),
        ("fecha_hora",   "Fecha y Hora", 150, "center"),
        ("monto_total",  "Monto Total",  100, "center"),
        ("id_cliente",   "ID Cliente",   80,  "center"),
        ("id_vendedor",  "ID Vendedor",  80,  "center"),
    ]:
        tabla.heading(col, text=texto)
        tabla.column(col, width=ancho, anchor=anchor)

    # Scrollbar
    scrollbar = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tabla.pack(fill=tk.BOTH, expand=True)

    tabla.insert("", "end", values=("1", "2024-06-01 10:30", "150.00", "101", "201"))
    tabla.insert("", "end", values=("2", "2024-06-02 14:45", "200.00", "102", "202"))

    # ── Lógica de agregar ── (adentro de Ventas para acceder a entrada_* y tabla)
    contador_id = [3]

    def agregar_venta():
        Monto_total = entrada_monto_total.get().strip()
        Cliente_id = entrada_id_cliente.get().strip()
        Vendedor_id = entrada_id_vendedor.get().strip()

        if not all([Monto_total, Cliente_id, Vendedor_id]):
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
            return

        try:
            monto_val = float(Monto_total)
        except ValueError:
            messagebox.showerror("Monto inválido", "El monto total debe ser un número válido.")
            return

        if monto_val <= 0:
            messagebox.showerror("Monto inválido", "El monto total debe ser mayor a cero.")
            return

        if not Cliente_id.isdigit() or not Vendedor_id.isdigit():
            messagebox.showerror("IDs inválidos", "El ID de cliente y vendedor deben ser números enteros.")
            return

        id_venta = str(contador_id[0])
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        contador_id[0] += 1

        tabla.insert("", tk.END, values=(
            id_venta,
            fecha_hora,
            f"${monto_val:.2f}",
            Cliente_id,
            Vendedor_id,
        ))

        for entry in (entrada_monto_total, entrada_id_cliente, entrada_id_vendedor):
            entry.delete(0, tk.END)


    # ── Cargar venta seleccionada en el formulario ──
    def cargar_venta(event=None):
        seleccion = tabla.selection()

        for entry in (entrada_monto_total, entrada_id_cliente, entrada_id_vendedor):
            entry.delete(0, tk.END)

        if not seleccion:
            return

        _, _, monto, id_cliente, id_vendedor = tabla.item(seleccion[0], "values")
        entrada_monto_total.insert(0, str(monto).lstrip("$"))
        entrada_id_cliente.insert(0, id_cliente)
        entrada_id_vendedor.insert(0, id_vendedor)

    tabla.bind("<<TreeviewSelect>>", cargar_venta)

    # ── Lógica de modificar ──
    def modificar_venta():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccioná una venta de la tabla para modificarla.",
            )
            return

        Monto_total = entrada_monto_total.get().strip()
        Cliente_id  = entrada_id_cliente.get().strip()
        Vendedor_id = entrada_id_vendedor.get().strip()

        if not all([Monto_total, Cliente_id, Vendedor_id]):
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
            return

        try:
            monto_val = float(Monto_total)
        except ValueError:
            messagebox.showerror("Monto inválido", "El monto total debe ser un número válido.")
            return

        if monto_val <= 0:
            messagebox.showerror("Monto inválido", "El monto total debe ser mayor a cero.")
            return

        if not Cliente_id.isdigit() or not Vendedor_id.isdigit():
            messagebox.showerror("IDs inválidos", "El ID de cliente y vendedor deben ser números enteros.")
            return

        # El ID y la fecha originales de la venta se conservan
        id_venta, fecha_hora = tabla.item(seleccion[0], "values")[:2]
        tabla.item(seleccion[0], values=(
            id_venta,
            fecha_hora,
            f"${monto_val:.2f}",
            Cliente_id,
            Vendedor_id,
        ))
        tabla.selection_remove(seleccion)

    # ── Lógica de borrar ──
    def borrar_venta():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccioná una venta de la tabla para borrarla.",
            )
            return

        valores = tabla.item(seleccion[0], "values")
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que querés borrar la venta N° {valores[0]} ({valores[1]})?",
        )

        if confirmar:
            tabla.delete(seleccion[0])
            tabla.event_generate("<<TreeviewSelect>>")


    frame_btn = tk.Frame(Frame_principal, bg="black")
    frame_btn.pack(fill=tk.X, padx=10, pady=(0, 10))

    tk.Button(
        frame_btn,
        text="Registrar Venta",
        command=agregar_venta,
        bg="forestgreen", fg="white",
        activebackground="green", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT, padx=(0, 10))


    tk.Button(
        frame_btn,
        text="Modificar Venta",
        command=modificar_venta,
        bg="royalblue", fg="white",
        activebackground="navy", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT, padx=(0, 10))


    tk.Button(
        frame_btn,
        text="Borrar Venta",
        command=borrar_venta,
        bg="firebrick", fg="white",
        activebackground="darkred", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT)


def mostrar_ventana_ventas():
    ventana = tk.Tk()
    ventana.title("Ventas — Almacén de Don Mario")
    ventana.minsize(900, 600)
    ventana.resizable(False, False)
    ventana.configure(bg="black")

    ttk.Label(
        ventana,
        text="Almacén de Don Mario",
        font=("Times New Roman", 20, "bold"),
        background="black",
        foreground="white",
    ).pack(pady=15)

    main_frame = tk.Frame(ventana, bg="black")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    Ventas(main_frame)

    ventana.mainloop()


if __name__ == "__main__":
    mostrar_ventana_ventas()