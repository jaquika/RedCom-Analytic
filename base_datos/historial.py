from base_datos.conexion_sqlite import obtener_conexion, crear_tablas

def obtener_historial() -> list:
    crear_tablas()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM simulaciones ORDER BY fecha DESC")
    filas = cursor.fetchall()
    conexion.close()
    return filas
