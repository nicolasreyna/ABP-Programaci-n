from BASE_DE_DATOS.conexion import obtener_conexion

def crear_tabla_vendedor():
    sql = """
    CREATE TABLE IF NOT EXISTS VENDEDOR (
        id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(10) NOT NULL UNIQUE,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        celular VARCHAR(20),
        turno VARCHAR(50)
    );
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def agregar_vendedor(dni, nombre, apellido, celular, turno):
    sql = """
    INSERT INTO VENDEDOR (dni, nombre, apellido, celular, turno)
    VALUES (?, ?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (dni, nombre, apellido, celular, turno))
    conexion.commit()
    id_creado = cursor.lastrowid
    conexion.close()
    return id_creado

def obtener_vendedores():
    sql = "SELECT id_vendedor, dni, nombre, apellido, celular, turno FROM VENDEDOR;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    filas = cursor.fetchall()
    conexion.close()
    return filas

def modificar_vendedor(id_vendedor, dni, nombre, apellido, celular, turno):
    sql = """
    UPDATE VENDEDOR
    SET dni = ?, nombre = ?, apellido = ?, celular = ?, turno = ?
    WHERE id_vendedor = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (dni, nombre, apellido, celular, turno, id_vendedor))
    conexion.commit()
    conexion.close()

def eliminar_vendedor(id_vendedor):
    sql = "DELETE FROM VENDEDOR WHERE id_vendedor = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (id_vendedor,))
    conexion.commit()
    conexion.close()