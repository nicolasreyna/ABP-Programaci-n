from .conexion import conexion_segura


def crear_tabla_producto():
    """Crea la tabla PRODUCTO si no existe."""
    sql = """
    CREATE TABLE IF NOT EXISTS producto (
        codigo TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL CHECK (precio >= 0),
        stock INTEGER NOT NULL CHECK (stock >= 0)
    );
    """
    with conexion_segura() as conexion:
        conexion.execute(sql)


def agregar_producto(codigo, nombre, precio, stock):
    """Inserta un producto con los campos recibidos desde la interfaz."""
    sql = """
    INSERT INTO producto (codigo, nombre, precio, stock)
    VALUES (?, ?, ?, ?);
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (codigo, nombre, float(str(precio).replace("$", "")), stock))


def obtener_productos():
    """Devuelve código, nombre, precio y stock de cada producto."""
    sql = "SELECT codigo, nombre, precio, stock FROM producto;"
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
    return filas


def modificar_producto(codigo_anterior, codigo, nombre, precio, stock):
    """Actualiza los campos del producto identificado por su código anterior."""
    sql = """
    UPDATE producto
    SET codigo = ?, nombre = ?, precio = ?, stock = ?
    WHERE codigo = ?;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            sql,
            (codigo, nombre, float(str(precio).replace("$", "")), stock, codigo_anterior),
        )


def eliminar_producto(codigo):
    sql = "DELETE FROM producto WHERE codigo = ?;"
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (codigo,))
