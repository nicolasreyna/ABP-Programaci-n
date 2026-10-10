from BASE_DE_DATOS.conexion import obtener_conexion

def crear_tabla_proveedor():
    sql = """
    CREATE TABLE IF NOT EXISTS PROVEEDOR (
        id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
        cuit VARCHAR(15) NOT NULL UNIQUE,
        nombre VARCHAR(100) NOT NULL,
        direccion VARCHAR(150),
        celular VARCHAR(20),
        email VARCHAR(100)
    );
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def agregar_proveedor(cuit, nombre, direccion, celular, email):
    sql = """
    INSERT INTO PROVEEDOR (cuit, nombre, direccion, celular, email)
    VALUES (?, ?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (cuit, nombre, direccion, celular, email))
    conexion.commit()
    id_creado = cursor.lastrowid
    conexion.close()
    return id_creado

def obtener_proveedores():
    sql = "SELECT id_proveedor, cuit, nombre, direccion, celular, email FROM PROVEEDOR;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    filas = cursor.fetchall()
    conexion.close()
    return filas

def modificar_proveedor(id_proveedor, cuit, nombre, direccion, celular, email):
    sql = """
    UPDATE PROVEEDOR
    SET cuit = ?, nombre = ?, direccion = ?, celular = ?, email = ?
    WHERE id_proveedor = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (cuit, nombre, direccion, celular, email, id_proveedor))
    conexion.commit()
    conexion.close()

def eliminar_proveedor(id_proveedor):
    sql = "DELETE FROM PROVEEDOR WHERE id_proveedor = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (id_proveedor,))
    conexion.commit()
    conexion.close()