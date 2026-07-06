from base_datos.conexion_sqlite import obtener_conexion, crear_tablas

def guardar_metricas(tipo_red: str, metricas: dict) -> None:
    crear_tablas()
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO simulaciones (
        tipo_red, paquetes_enviados, paquetes_recibidos, paquetes_perdidos,
        tasa_perdida, latencia_promedio, throughput, eventos_congestion
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        tipo_red,
        metricas["paquetes_enviados"],
        metricas["paquetes_recibidos"],
        metricas["paquetes_perdidos"],
        metricas["tasa_perdida"],
        metricas["latencia_promedio"],
        metricas["throughput"],
        metricas["eventos_congestion"]
    ))
    conexion.commit()
    conexion.close()
