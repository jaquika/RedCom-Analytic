def calcular_metricas(resultados: list, velocidad_minima_mbps: float) -> dict:
    """Calcula métricas principales de rendimiento de red."""
    enviados = len(resultados)
    recibidos = len([r for r in resultados if r["estado"] == "Recibido"])
    perdidos = len([r for r in resultados if r["estado"] == "Perdido"])
    congestiones = len([r for r in resultados if r["congestion"]])

    latencias = [r["latencia_ms"] for r in resultados if r["latencia_ms"] is not None]
    latencia_promedio = sum(latencias) / len(latencias) if latencias else 0
    tasa_perdida = (perdidos / enviados) * 100 if enviados > 0 else 0
    throughput = (recibidos / enviados) * velocidad_minima_mbps if enviados > 0 else 0

    return {
        "paquetes_enviados": enviados,
        "paquetes_recibidos": recibidos,
        "paquetes_perdidos": perdidos,
        "tasa_perdida": round(tasa_perdida, 2),
        "latencia_promedio": round(latencia_promedio, 2),
        "throughput": round(throughput, 2),
        "eventos_congestion": congestiones
    }
