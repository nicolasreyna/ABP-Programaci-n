from database.conexion import obtener_conexion

def crear_tabla_producto():
    """Crea la tabla PRODUCTO si no existe."""
    sql = """
    CREATE TABLE IF NOT EXISTS PRODUCTO (
        codigo_producto VARCHAR(20) PRIMARY KEY,
        nombre_producto VARCHAR(100) NOT NULL,
        descripcion TEXT,
        precio_actual NUMERIC(10,2) NOT NULL CHECK (precio_actual >= 0),
        stock_actual INT NOT NULL DEFAULT 0 CHECK (stock_actual >= 0)
    );
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def agregar_producto(codigo_producto, nombre_producto, descripcion, precio_actual, stock_actual):
    """Inserta un nuevo producto (Alta)."""
    sql = """
    INSERT INTO PRODUCTO (codigo_producto, nombre_producto, descripcion, precio_actual, stock_actual)
    VALUES (?, ?, ?, ?, ?);
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (codigo_producto, nombre_producto, descripcion, precio_actual, stock_actual))
    conexion.commit()
    conexion.close()

def obtener_productos():
    """Devuelve la lista de todos los productos (Consulta)."""
    sql = """
    SELECT codigo_producto, nombre_producto, descripcion, precio_actual, stock_actual 
    FROM PRODUCTO;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql)
    filas = cursor.fetchall()
    conexion.close()
    return filas

def modificar_producto(codigo_producto, nombre_producto, descripcion, precio_actual, stock_actual):
    """Modifica los datos y stock de un producto existente."""
    sql = """
    UPDATE PRODUCTO
    SET nombre_producto = ?, descripcion = ?, precio_actual = ?, stock_actual = ?
    WHERE codigo_producto = ?;
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (nombre_producto, descripcion, precio_actual, stock_actual, codigo_producto))
    conexion.commit()
    conexion.close()

def eliminar_producto(codigo_producto):
    """Elimina un producto por su código."""
    sql = "DELETE FROM PRODUCTO WHERE codigo_producto = ?;"
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(sql, (codigo_producto,))
    conexion.commit()
    conexion.close()