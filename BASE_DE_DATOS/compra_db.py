from .conexion import conexion_segura


def crear_tabla_compra():
    sql = """
    CREATE TABLE IF NOT EXISTS compra (
        id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora TEXT NOT NULL,
        monto_total REAL NOT NULL CHECK (monto_total > 0),
        id_proveedor INTEGER NOT NULL REFERENCES proveedor(id_proveedor),
        id_vendedor INTEGER NOT NULL REFERENCES vendedor(id_vendedor)
    );
    """
    with conexion_segura() as conexion:
        conexion.execute(sql)


def agregar_compra(id_compra, fecha_hora, monto_total, id_proveedor, id_vendedor):
    sql = """
    INSERT INTO compra (id_compra, fecha_hora, monto_total, id_proveedor, id_vendedor)
    VALUES (?, ?, ?, ?, ?);
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            sql,
            (
                id_compra,
                fecha_hora,
                float(str(monto_total).replace("$", "")),
                id_proveedor,
                id_vendedor,
            ),
        )
        id_creado = cursor.lastrowid
    return id_creado


def obtener_compras():
    sql = """
    SELECT id_compra, fecha_hora, monto_total, id_proveedor, id_vendedor
    FROM compra;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
    return filas


def modificar_compra(id_compra, fecha_hora, monto_total, id_proveedor, id_vendedor):
    sql = """
    UPDATE compra
    SET fecha_hora = ?, monto_total = ?, id_proveedor = ?, id_vendedor = ?
    WHERE id_compra = ?;
    """
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            sql,
            (
                fecha_hora,
                float(str(monto_total).replace("$", "")),
                id_proveedor,
                id_vendedor,
                id_compra,
            ),
        )


def eliminar_compra(id_compra):
    sql = "DELETE FROM compra WHERE id_compra = ?;"
    with conexion_segura() as conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, (id_compra,))
