from .conexion import obtener_conexion


def crear_tabla_cliente():
    sql = """
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        dni TEXT NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        metodo_pago TEXT NOT NULL
    );
    """
    conexion = obtener_conexion()
    conexion.execute(sql)
    conexion.commit()
    conexion.close()


def agregar_cliente(dni, nombre, apellido, pago):
    sql = """
    INSERT INTO cliente (dni, nombre, apellido, metodo_pago)
    VALUES (?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (dni, nombre, apellido, pago))
    conexion.commit()
    id_creado = cursor.lastrowid
    conexion.close()
    return id_creado


def obtener_clientes():
    sql = "SELECT id_cliente, dni, nombre, apellido, metodo_pago FROM cliente;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()
    conexion.close()
    return registros


def modificar_cliente(id_cliente, dni, nombre, apellido, pago):
    sql = """
    UPDATE cliente
    SET dni = ?, nombre = ?, apellido = ?, metodo_pago = ?
    WHERE id_cliente = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (dni, nombre, apellido, pago, id_cliente))
    conexion.commit()
    conexion.close()


def eliminar_cliente(id_cliente):
    sql = "DELETE FROM cliente WHERE id_cliente = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (id_cliente,))
    conexion.commit()
    conexion.close()
