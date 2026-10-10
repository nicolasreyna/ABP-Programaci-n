import os
import tkinter as tk
from tkinter import ttk, messagebox

carpeta_proyecto = os.path.dirname(__file__)
ruta_logo = os.path.join(carpeta_proyecto, "LOGO APP.png")


def Vendedor(parent):
    """Entidad: VENDEDOR (id_vendedor PK, nombre, apellido, dni, celular)"""

    frame = tk.Frame(parent, bg="black", bd=5, relief="groove")
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    ttk.Label(
        frame,
        text="Vendedor",
        background="black",
        foreground="white",
        font=("Arial", 15, "bold"),
    ).pack(anchor="w", padx=10, pady=(10, 6))

    # ── Formulario ──
    form = tk.Frame(frame, bg="black")
    form.pack(fill=tk.X, padx=10, pady=5)

    def campo(label_text):
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

    entrada_nombre   = campo("Nombre:")
    entrada_apellido = campo("Apellido:")
    entrada_dni      = campo("DNI:")
    entrada_celular  = campo("Celular:")

    # ── Tabla ──
    columnas = ("id_vendedor", "nombre", "apellido", "dni", "celular")
    tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=12, selectmode="browse")
    for col, texto, ancho, anchor in [
        ("id_vendedor", "ID",       60,  "center"),
        ("nombre",      "NOMBRE",   130, "w"),
        ("apellido",    "APELLIDO", 130, "w"),
        ("dni",         "DNI",      100, "center"),
        ("celular",     "CELULAR",  110, "center"),
    ]:
        tabla.heading(col, text=texto)
        tabla.column(col, width=ancho, anchor=anchor)
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # Dato de ejemplo — Don Mario
    tabla.insert("", "end", values=("1", "Mario", "González", "20333444", "351-1234567"))

    # ── ID automático ──
    def siguiente_id():
        ids = [int(tabla.item(item, "values")[0]) for item in tabla.get_children()]
        return max(ids) + 1 if ids else 1

    # ── Cargar vendedor seleccionado en el formulario ──
    def cargar_vendedor(event=None):
        seleccion = tabla.selection()

        for entry in (entrada_nombre, entrada_apellido, entrada_dni, entrada_celular):
            entry.delete(0, tk.END)

        if not seleccion:
            return

        _, nombre, apellido, dni, celular = tabla.item(seleccion[0], "values")
        entrada_nombre.insert(0, nombre)
        entrada_apellido.insert(0, apellido)
        entrada_dni.insert(0, dni)
        entrada_celular.insert(0, celular)

    tabla.bind("<<TreeviewSelect>>", cargar_vendedor)

    # ── Lógica de agregar ──
    def agregar_vendedor():
        nombre   = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()
        dni      = entrada_dni.get().strip()
        celular  = entrada_celular.get().strip()

        if not all([nombre, apellido, dni, celular]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        if not dni.isdigit() or len(dni) > 8:
            messagebox.showerror(
                "DNI inválido",
                "El DNI debe contener solo números y tener como máximo 8 dígitos.",
            )
            return

        id_vendedor = str(siguiente_id())
        tabla.insert("", tk.END, values=(id_vendedor, nombre, apellido, dni, celular))

        for entry in (entrada_nombre, entrada_apellido, entrada_dni, entrada_celular):
            entry.delete(0, tk.END)

    # ── Lógica de modificar ──
    def modificar_vendedor():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccioná un vendedor de la tabla para modificarlo.",
            )
            return

        nombre   = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()
        dni      = entrada_dni.get().strip()
        celular  = entrada_celular.get().strip()

        if not all([nombre, apellido, dni, celular]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        if not dni.isdigit() or len(dni) > 8:
            messagebox.showerror(
                "DNI inválido",
                "El DNI debe contener solo números y tener como máximo 8 dígitos.",
            )
            return

        id_vendedor = tabla.item(seleccion[0], "values")[0]  # el ID no cambia
        tabla.item(seleccion[0], values=(id_vendedor, nombre, apellido, dni, celular))
        tabla.selection_remove(seleccion)

    # ── Lógica de borrar ──
    def borrar_vendedor():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccioná un vendedor de la tabla para borrarlo.",
            )
            return

        valores = tabla.item(seleccion[0], "values")
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que querés borrar a {valores[1]} {valores[2]} (DNI {valores[3]})?",
        )

        if confirmar:
            tabla.delete(seleccion[0])
            tabla.event_generate("<<TreeviewSelect>>")

    # ── Botones ──
    frame_botones = tk.Frame(form, bg="black")
    frame_botones.pack(anchor="w", pady=(0, 12))

    tk.Button(
        frame_botones,
        text="Agregar Vendedor",
        command=agregar_vendedor,
        bg="forestgreen", fg="white",
        activebackground="green", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT, padx=(0, 10))

    tk.Button(
        frame_botones,
        text="Modificar Vendedor",
        command=modificar_vendedor,
        bg="royalblue", fg="white",
        activebackground="navy", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT, padx=(0, 10))

    tk.Button(
        frame_botones,
        text="Borrar Vendedor",
        command=borrar_vendedor,
        bg="firebrick", fg="white",
        activebackground="darkred", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(side=tk.LEFT)


def mostrar_ventana_vendedor():
    ventana = tk.Tk()
    ventana.title("Vendedores — Almacén de Don Mario")
    ventana.minsize(700, 600)
    ventana.resizable(False, False)
    ventana.configure(bg="black")

    ttk.Label(
        ventana,
        text="Almacén de Don Mario",
        font=("Times New Roman", 20, "bold"),
        background="black",
        foreground="chartreuse2",
    ).pack(pady=15)

    main_frame = tk.Frame(ventana, bg="black")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    Vendedor(main_frame)

    ventana.mainloop()


if __name__ == "__main__":
    mostrar_ventana_vendedor()