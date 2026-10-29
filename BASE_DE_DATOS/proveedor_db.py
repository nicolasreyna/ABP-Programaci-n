from .conexion import conexion_segura


def crear_tabla_proveedor():
    sql = """
    CREATE TABLE IF NOT EXISTS proveedor (
        id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
        cuit TEXT NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        direccion TEXT NOT NULL,
        celular TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    with conexion_segura() as conexion:
        conexion.execute(sql)


def agregar_proveedor(id_proveedor, cuit, nombre, direccion, celular, email):
    sql = """
    INSERT INTO proveedor (id_proveedor, cuit, nombre, direccion, celular, email)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (id_proveedor, cuit, nombre, direccion, celular, email))


def obtener_proveedores():
    sql = """
    SELECT id_proveedor, cuit, nombre, direccion, celular, email
    FROM proveedor;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
    return filas


def modificar_proveedor(id_proveedor, cuit, nombre, direccion, celular, email):
    sql = """
    UPDATE proveedor
    SET cuit = ?, nombre = ?, direccion = ?, celular = ?, email = ?
    WHERE id_proveedor = ?;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (cuit, nombre, direccion, celular, email, id_proveedor))


def eliminar_proveedor(id_proveedor):
    sql = "DELETE FROM proveedor WHERE id_proveedor = ?;"
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (id_proveedor,))
