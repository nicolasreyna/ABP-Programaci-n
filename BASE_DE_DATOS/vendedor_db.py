from .conexion import conexion_segura


def crear_tabla_vendedor():
    sql = """
    CREATE TABLE IF NOT EXISTS vendedor (
        id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        dni TEXT NOT NULL UNIQUE,
        celular TEXT NOT NULL
    );
    """
    with conexion_segura() as conexion:
        conexion.execute(sql)


def agregar_vendedor(id_vendedor, nombre, apellido, dni, celular):
    sql = """
    INSERT INTO vendedor (id_vendedor, nombre, apellido, dni, celular)
    VALUES (?, ?, ?, ?, ?);
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (id_vendedor, nombre, apellido, dni, celular))


def obtener_vendedores():
    sql = """
    SELECT id_vendedor, nombre, apellido, dni, celular
    FROM vendedor;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
    return filas


def modificar_vendedor(id_vendedor, nombre, apellido, dni, celular):
    sql = """
    UPDATE vendedor
    SET nombre = ?, apellido = ?, dni = ?, celular = ?
    WHERE id_vendedor = ?;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (nombre, apellido, dni, celular, id_vendedor))


def eliminar_vendedor(id_vendedor):
    sql = "DELETE FROM vendedor WHERE id_vendedor = ?;"
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (id_vendedor,))
