from base_datos.conexion_sqlite import obtener_conexion, crear_tablas

def guardar_topologia(nombre: str, tipo_red: str, velocidad_mbps: float,
                       latencia_ms: float, perdida: float, capacidad_cola: int) -> None:
    crear_tablas()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
    INSERT INTO topologias (nombre, tipo_red, velocidad_mbps, latencia_ms, perdida, capacidad_cola)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, tipo_red, velocidad_mbps, latencia_ms, perdida, capacidad_cola))
    conexion.commit()
    conexion.close()

def obtener_topologias() -> list:
    crear_tablas()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM topologias ORDER BY fecha DESC")
    filas = cursor.fetchall()
    conexion.close()
    return filas

def obtener_topologia_por_id(id_topologia: int):
    crear_tablas()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM topologias WHERE id = ?", (id_topologia,))
    fila = cursor.fetchone()
    conexion.close()
    return fila
