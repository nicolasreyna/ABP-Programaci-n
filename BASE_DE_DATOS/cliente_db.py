from .conexion import conexion_segura


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
    with conexion_segura() as conexion:
        conexion.execute(sql)


def agregar_cliente(dni, nombre, apellido, pago):
    sql = """
    INSERT INTO cliente (dni, nombre, apellido, metodo_pago)
    VALUES (?, ?, ?, ?);
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (dni, nombre, apellido, pago))
        id_creado = cursor.lastrowid
    return id_creado


def obtener_clientes():
    sql = "SELECT id_cliente, dni, nombre, apellido, metodo_pago FROM cliente;"
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
    return registros


def modificar_cliente(id_cliente, dni, nombre, apellido, pago):
    sql = """
    UPDATE cliente
    SET dni = ?, nombre = ?, apellido = ?, metodo_pago = ?
    WHERE id_cliente = ?;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (dni, nombre, apellido, pago, id_cliente))


def eliminar_cliente(id_cliente):
    sql = "DELETE FROM cliente WHERE id_cliente = ?;"
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (id_cliente,))
