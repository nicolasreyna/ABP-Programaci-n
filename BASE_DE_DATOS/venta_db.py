from BASE_DE_DATOS.conexion import obtener_conexion

def crear_tabla_venta():
    sql = """
    CREATE TABLE IF NOT EXISTS VENTA (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora DATETIME NOT NULL,
        monto_total NUMERIC(10,2) CHECK (monto_total >= 0),
        id_cliente INTEGER NOT NULL,
        id_vendedor INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente) ON DELETE RESTRICT,
        FOREIGN KEY (id_vendedor) REFERENCES VENDEDOR(id_vendedor) ON DELETE RESTRICT
    );
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def agregar_venta(fecha_hora, monto_total, id_cliente, id_vendedor):
    sql = """
    INSERT INTO VENTA (fecha_hora, monto_total, id_cliente, id_vendedor)
    VALUES (?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (fecha_hora, monto_total, id_cliente, id_vendedor))
    conexion.commit()
    id_creado = cursor.lastrowid
    conexion.close()
    return id_creado

def obtener_ventas():
    sql = "SELECT id_venta, fecha_hora, monto_total, id_cliente, id_vendedor FROM VENTA;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    filas = cursor.fetchall()
    conexion.close()
    return filas

def modificar_venta(id_venta, fecha_hora, monto_total, id_cliente, id_vendedor):
    sql = """
    UPDATE VENTA
    SET fecha_hora = ?, monto_total = ?, id_cliente = ?, id_vendedor = ?
    WHERE id_venta = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (fecha_hora, monto_total, id_cliente, id_vendedor, id_venta))
    conexion.commit()
    conexion.close()

def eliminar_venta(id_venta):
    sql = "DELETE FROM VENTA WHERE id_venta = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (id_venta,))
    conexion.commit()
    conexion.close()