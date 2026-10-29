# database/conexion.py
import sqlite3
import os
from contextlib import contextmanager

# Guardar la base junto al proyecto, independientemente de desde dónde se inicie la app.
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "almacen.db")

def obtener_conexion():
    """Crea o se conecta a la base de datos SQLite y activa claves foráneas."""
    conexion = sqlite3.connect(DB_PATH)
    # Habilitar soporte para Foreign Keys en SQLite
    conexion.execute("PRAGMA foreign_keys = ON;")
    return conexion

@contextmanager
def conexion_segura():
    """Gestiona la transacción y garantiza cerrar la conexión."""
    conexion = obtener_conexion()
    try:
        with conexion:
            yield conexion
    finally:
        conexion.close()

def crear_tablas():
    """Crea todas las tablas si no existen. Se llama una sola vez al iniciar."""
    with conexion_segura() as con:
        cur = con.cursor()
        cur.executescript("""
        CREATE TABLE IF NOT EXISTS vendedor (
            id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT    NOT NULL,
            apellido    TEXT    NOT NULL,
            dni         TEXT    NOT NULL UNIQUE,
            celular     TEXT    NOT NULL
        );

        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente  INTEGER PRIMARY KEY AUTOINCREMENT,
            dni         TEXT    NOT NULL UNIQUE,
            nombre      TEXT    NOT NULL,
            apellido    TEXT    NOT NULL,
            metodo_pago TEXT    NOT NULL
        );

        CREATE TABLE IF NOT EXISTS producto (
            codigo  TEXT    PRIMARY KEY,
            nombre  TEXT    NOT NULL,
            precio  REAL    NOT NULL CHECK(precio >= 0),
            stock   INTEGER NOT NULL CHECK(stock  >= 0)
        );

        CREATE TABLE IF NOT EXISTS proveedor (
            id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
            cuit         TEXT    NOT NULL UNIQUE,
            nombre       TEXT    NOT NULL,
            direccion    TEXT    NOT NULL,
            celular      TEXT    NOT NULL,
            email        TEXT    NOT NULL
        );

        CREATE TABLE IF NOT EXISTS compra (
            id_compra    INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_hora   TEXT    NOT NULL,
            monto_total  REAL    NOT NULL CHECK(monto_total > 0),
            id_proveedor INTEGER NOT NULL REFERENCES proveedor(id_proveedor),
            id_vendedor  INTEGER NOT NULL REFERENCES vendedor(id_vendedor)
        );

        CREATE TABLE IF NOT EXISTS venta (
            id_venta    INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_hora  TEXT    NOT NULL,
            monto_total REAL    NOT NULL CHECK(monto_total > 0),
            id_cliente  INTEGER NOT NULL REFERENCES cliente(id_cliente),
            id_vendedor INTEGER NOT NULL REFERENCES vendedor(id_vendedor)
        );
        """)
