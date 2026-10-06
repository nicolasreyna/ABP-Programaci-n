import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

carpeta_proyecto = os.path.dirname(__file__)
ruta_logo = os.path.join(carpeta_proyecto, "LOGO APP.png")



def Proveedor(parent):
    """Entidad: PROVEEDOR (id_proveedor PK, cuit, nombre, dirección, celular, email)"""

    left_frame = tk.Frame(parent, bg="black", bd=5, relief="groove")
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

    ttk.Label(
        left_frame,
        text="Proveedor",
        background="black",
        foreground="white",
        font=("Arial", 15, "bold"),
    ).pack(anchor="w", padx=10, pady=(10, 6))

    # ── Formulario ──
    form = tk.Frame(left_frame, bg="black")
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

    entrada_cuit      = campo("CUIT:")
    entrada_nombre    = campo("Nombre:")
    entrada_direccion = campo("Dirección:")
    entrada_celular   = campo("Celular:")
    entrada_email     = campo("Email:")

    # ── Tabla ──
    columnas = ("id_proveedor", "cuit", "nombre", "direccion", "celular", "email")
    tabla = ttk.Treeview(left_frame, columns=columnas, show="headings", height=8)
    for col, texto, ancho, anchor in [
        ("id_proveedor", "ID",        50,  "center"),
        ("cuit",         "CUIT",      110, "center"),
        ("nombre",       "NOMBRE",    120, "w"),
        ("direccion",    "DIRECCIÓN", 120, "w"),
        ("celular",      "CELULAR",   90,  "center"),
        ("email",        "EMAIL",     140, "w"),
    ]:
        tabla.heading(col, text=texto)
        tabla.column(col, width=ancho, anchor=anchor)
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # Datos de ejemplo
    tabla.insert("", "end", values=("1", "20-12345678-9", "Distribuidora García", "Av. Colón 123", "351-4112233", "garcia@mail.com"))
    tabla.insert("", "end", values=("2", "30-98765432-1", "Bebidas del Sur S.A.", "Ruta 9 Km 5",  "351-5556677", "bdelsur@mail.com"))

    # ── Lógica de agregar ──
    contador_id = [3]

    def agregar_proveedor():
        cuit      = entrada_cuit.get().strip()
        nombre    = entrada_nombre.get().strip()
        direccion = entrada_direccion.get().strip()
        celular   = entrada_celular.get().strip()
        email     = entrada_email.get().strip()

        if not all([cuit, nombre, direccion, celular, email]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        cuit_limpio = cuit.replace("-", "")
        if not cuit_limpio.isdigit() or len(cuit_limpio) != 11:
            messagebox.showerror(
                "CUIT inválido",
                "El CUIT debe tener 11 dígitos numéricos.\nFormato esperado: 20-12345678-9",
            )
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Email inválido", "Ingresá un email con formato válido.")
            return

        id_proveedor = str(contador_id[0])
        contador_id[0] += 1

        tabla.insert("", tk.END, values=(id_proveedor, cuit, nombre, direccion, celular, email))
        for entry in (entrada_cuit, entrada_nombre, entrada_direccion, entrada_celular, entrada_email):
            entry.delete(0, tk.END)

    tk.Button(
        form,
        text="Agregar Proveedor",
        command=agregar_proveedor,
        bg="forestgreen", fg="white",
        activebackground="green", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(anchor="w", pady=(0, 12))



def Compra(parent):
    """Entidad: COMPRA (id_compra PK, fecha_hora, monto_total, id_proveedor FK, id_vendedor FK)"""

    right_frame = tk.Frame(parent, bg="black", bd=5, relief="groove")
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

    ttk.Label(
        right_frame,
        text="Compra",
        background="black",
        foreground="white",
        font=("Arial", 15, "bold"),
    ).pack(anchor="w", padx=10, pady=(10, 6))

    # ── Formulario ──
    form = tk.Frame(right_frame, bg="black")
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

    entrada_monto_total  = campo("Monto Total ($):")
    entrada_id_proveedor = campo("ID Proveedor (FK):")
    entrada_id_vendedor  = campo("ID Vendedor (FK):")

    # ── Tabla ──
    columnas = ("id_compra", "fecha_hora", "monto_total", "id_proveedor", "id_vendedor")
    tabla = ttk.Treeview(right_frame, columns=columnas, show="headings", height=8)
    for col, texto, ancho, anchor in [
        ("id_compra",    "ID",          50,  "center"),
        ("fecha_hora",   "FECHA/HORA",  145, "center"),
        ("monto_total",  "MONTO TOTAL", 100, "e"),
        ("id_proveedor", "ID PROV.",    80,  "center"),
        ("id_vendedor",  "ID VEND.",    80,  "center"),
    ]:
        tabla.heading(col, text=texto)
        tabla.column(col, width=ancho, anchor=anchor)
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

    # Datos de ejemplo
    tabla.insert("", "end", values=("1", "2026-10-05 09:30:00", "$15000.00", "1", "3"))
    tabla.insert("", "end", values=("2", "2026-10-05 11:15:00", "$13200.00", "2", "1"))

    # ── Lógica de agregar ──
    contador_id = [3]

    def agregar_compra():
        monto_total  = entrada_monto_total.get().strip()
        id_proveedor = entrada_id_proveedor.get().strip()
        id_vendedor  = entrada_id_vendedor.get().strip()

        if not all([monto_total, id_proveedor, id_vendedor]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        try:
            monto_val = float(monto_total)
        except ValueError:
            messagebox.showerror("Monto inválido", "El monto total debe ser un número válido.")
            return

        if monto_val <= 0:
            messagebox.showerror("Monto inválido", "El monto total debe ser mayor a cero.")
            return

        if not id_proveedor.isdigit() or not id_vendedor.isdigit():
            messagebox.showerror("IDs inválidos", "El ID de proveedor y vendedor deben ser números enteros.")
            return

        id_compra  = str(contador_id[0])
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        contador_id[0] += 1

        tabla.insert("", tk.END, values=(
            id_compra,
            fecha_hora,
            f"${monto_val:.2f}",
            id_proveedor,
            id_vendedor,
        ))
        for entry in (entrada_monto_total, entrada_id_proveedor, entrada_id_vendedor):
            entry.delete(0, tk.END)

    tk.Button(
        form,
        text="Registrar Compra",
        command=agregar_compra,
        bg="forestgreen", fg="white",
        activebackground="green", activeforeground="white",
        font=("Arial", 10, "bold"),
        cursor="hand2",
    ).pack(anchor="w", pady=(0, 12))




def mostrar_ventana_ciclo_compra():
    ventana = tk.Tk()
    ventana.title("Ciclo de Compra — Almacén de Don Mario")
    ventana.minsize(1200, 500)
    ventana.resizable(False, False)
    ventana.configure(bg="darkslategray")

    try:
        logo = tk.PhotoImage(file=ruta_logo)
        ventana.iconphoto(False, logo)
    except Exception:
        pass

    ttk.Label(
        ventana,
        text="Almacén de Don Mario",
        font=("Times New Roman", 20, "bold"),
        background="darkslategray",
        foreground="white",
    ).pack(pady=15)

    main_frame = tk.Frame(ventana, bg="darkslategray")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    Proveedor(main_frame)
    Compra(main_frame)

    ventana.mainloop()


if __name__ == "__main__":
    mostrar_ventana_ciclo_compra()