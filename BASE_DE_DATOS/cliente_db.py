# database/cliente_db.py
from conexion import obtener_conexion

def crear_tabla_cliente():
    sql = """
    CREATE TABLE IF NOT EXISTS CLIENTE (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(10) NOT NULL UNIQUE,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        celular VARCHAR(20),
        domicilio VARCHAR(150)
    );
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def agregar_cliente(dni, nombre, apellido, celular, domicilio):
    sql = """
    INSERT INTO CLIENTE (dni, nombre, apellido, celular, domicilio)
    VALUES (?, ?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (dni, nombre, apellido, celular, domicilio))
    conexion.commit()
    id_creado = cursor.lastrowid
    conexion.close()
    return id_creado

def obtener_clientes():
    sql = "SELECT id_cliente, dni, nombre, apellido, celular, domicilio FROM CLIENTE;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()
    conexion.close()
    return registros

def modificar_cliente(id_cliente, dni, nombre, apellido, celular, domicilio):
    sql = """
    UPDATE CLIENTE
    SET dni = ?, nombre = ?, apellido = ?, celular = ?, domicilio = ?
    WHERE id_cliente = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (dni, nombre, apellido, celular, domicilio, id_cliente))
    conexion.commit()
    conexion.close()

def eliminar_cliente(id_cliente):
    sql = "DELETE FROM CLIENTE WHERE id_cliente = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (id_cliente,))
    conexion.commit()
    conexion.close()