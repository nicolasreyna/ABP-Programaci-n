from .conexion import obtener_conexion


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
    conexion = obtener_conexion()
    conexion.execute(sql)
    conexion.commit()
    conexion.close()


def agregar_producto(codigo, nombre, precio, stock):
    """Inserta un producto con los campos recibidos desde la interfaz."""
    sql = """
    INSERT INTO producto (codigo, nombre, precio, stock)
    VALUES (?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (codigo, nombre, float(str(precio).replace("$", "")), stock))
    conexion.commit()
    conexion.close()


def obtener_productos():
    """Devuelve código, nombre, precio y stock de cada producto."""
    sql = "SELECT codigo, nombre, precio, stock FROM producto;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    filas = cursor.fetchall()
    conexion.close()
    return filas


def modificar_producto(codigo_anterior, codigo, nombre, precio, stock):
    """Actualiza los campos del producto identificado por su código anterior."""
    sql = """
    UPDATE producto
    SET codigo = ?, nombre = ?, precio = ?, stock = ?
    WHERE codigo = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        sql,
        (codigo, nombre, float(str(precio).replace("$", "")), stock, codigo_anterior),
    )
    conexion.commit()
    conexion.close()


def eliminar_producto(codigo):
    sql = "DELETE FROM producto WHERE codigo = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (codigo,))
    conexion.commit()
    conexion.close()
