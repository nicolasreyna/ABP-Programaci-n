from .conexion import obtener_conexion


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
    conexion = obtener_conexion()
    conexion.execute(sql)
    conexion.commit()
    conexion.close()


def agregar_vendedor(id_vendedor, nombre, apellido, dni, celular):
    sql = """
    INSERT INTO vendedor (id_vendedor, nombre, apellido, dni, celular)
    VALUES (?, ?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (id_vendedor, nombre, apellido, dni, celular))
    conexion.commit()
    conexion.close()


def obtener_vendedores():
    sql = """
    SELECT id_vendedor, nombre, apellido, dni, celular
    FROM vendedor;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    filas = cursor.fetchall()
    conexion.close()
    return filas


def modificar_vendedor(id_vendedor, nombre, apellido, dni, celular):
    sql = """
    UPDATE vendedor
    SET nombre = ?, apellido = ?, dni = ?, celular = ?
    WHERE id_vendedor = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (nombre, apellido, dni, celular, id_vendedor))
    conexion.commit()
    conexion.close()


def eliminar_vendedor(id_vendedor):
    sql = "DELETE FROM vendedor WHERE id_vendedor = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (id_vendedor,))
    conexion.commit()
    conexion.close()
