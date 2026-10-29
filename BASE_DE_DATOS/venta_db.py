from .conexion import conexion_segura


def crear_tabla_venta():
    sql = """
    CREATE TABLE IF NOT EXISTS venta (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora TEXT NOT NULL,
        monto_total REAL NOT NULL CHECK (monto_total > 0),
        id_cliente INTEGER NOT NULL REFERENCES cliente(id_cliente),
        id_vendedor INTEGER NOT NULL REFERENCES vendedor(id_vendedor)
    );
    """
    with conexion_segura() as conexion:
        conexion.execute(sql)


def agregar_venta(id_venta, fecha_hora, monto_total, id_cliente, id_vendedor):
    sql = """
    INSERT INTO venta (id_venta, fecha_hora, monto_total, id_cliente, id_vendedor)
    VALUES (?, ?, ?, ?, ?);
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            sql,
            (
                id_venta,
                fecha_hora,
                float(str(monto_total).replace("$", "")),
                id_cliente,
                id_vendedor,
            ),
        )
        id_creado = cursor.lastrowid
    return id_creado


def obtener_ventas():
    sql = """
    SELECT id_venta, fecha_hora, monto_total, id_cliente, id_vendedor
    FROM venta;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
    return filas


def modificar_venta(id_venta, fecha_hora, monto_total, id_cliente, id_vendedor):
    sql = """
    UPDATE venta
    SET fecha_hora = ?, monto_total = ?, id_cliente = ?, id_vendedor = ?
    WHERE id_venta = ?;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            sql,
            (
                fecha_hora,
                float(str(monto_total).replace("$", "")),
                id_cliente,
                id_vendedor,
                id_venta,
            ),
        )


def eliminar_venta(id_venta):
    sql = "DELETE FROM venta WHERE id_venta = ?;"
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (id_venta,))
