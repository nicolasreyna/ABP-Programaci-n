from BASE_DE_DATOS.conexion import obtener_conexion

def crear_tabla_compra():
    sql = """
    CREATE TABLE IF NOT EXISTS COMPRA (
        id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora DATETIME NOT NULL,
        monto_total NUMERIC(10,2) CHECK (monto_total >= 0),
        id_proveedor INTEGER NOT NULL,
        id_vendedor INTEGER NOT NULL,
        FOREIGN KEY (id_proveedor) REFERENCES PROVEEDOR(id_proveedor) ON DELETE RESTRICT,
        FOREIGN KEY (id_vendedor) REFERENCES VENDEDOR(id_vendedor) ON DELETE RESTRICT
    );
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def agregar_compra(fecha_hora, monto_total, id_proveedor, id_vendedor):
    sql = """
    INSERT INTO COMPRA (fecha_hora, monto_total, id_proveedor, id_vendedor)
    VALUES (?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (fecha_hora, monto_total, id_proveedor, id_vendedor))
    conexion.commit()
    id_creado = cursor.lastrowid
    conexion.close()
    return id_creado

def obtener_compras():
    sql = "SELECT id_compra, fecha_hora, monto_total, id_proveedor, id_vendedor FROM COMPRA;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    filas = cursor.fetchall()
    conexion.close()
    return filas

def modificar_compra(id_compra, fecha_hora, monto_total, id_proveedor, id_vendedor):
    sql = """
    UPDATE COMPRA
    SET fecha_hora = ?, monto_total = ?, id_proveedor = ?, id_vendedor = ?
    WHERE id_compra = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (fecha_hora, monto_total, id_proveedor, id_vendedor, id_compra))
    conexion.commit()
    conexion.close()

def eliminar_compra(id_compra):
    sql = "DELETE FROM COMPRA WHERE id_compra = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (id_compra,))
    conexion.commit()
    conexion.close()