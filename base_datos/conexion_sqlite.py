import sqlite3
from pathlib import Path

DB_PATH = Path("data/simulaciones.db")

def obtener_conexion():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS simulaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_red TEXT,
        paquetes_enviados INTEGER,
        paquetes_recibidos INTEGER,
        paquetes_perdidos INTEGER,
        tasa_perdida REAL,
        latencia_promedio REAL,
        throughput REAL,
        eventos_congestion INTEGER,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topologias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        tipo_red TEXT,
        velocidad_mbps REAL,
        latencia_ms REAL,
        perdida REAL,
        capacidad_cola INTEGER,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conexion.commit()
    conexion.close()
