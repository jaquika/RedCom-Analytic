from pathlib import Path
import numpy as np
import pandas as pd

def resumen_metricas(metricas: dict) -> str:
    return (
        f"Paquetes enviados: {metricas['paquetes_enviados']}\n"
        f"Paquetes recibidos: {metricas['paquetes_recibidos']}\n"
        f"Paquetes perdidos: {metricas['paquetes_perdidos']}\n"
        f"Tasa de pérdida: {metricas['tasa_perdida']}%\n"
        f"Latencia promedio: {metricas['latencia_promedio']} ms\n"
        f"Throughput: {metricas['throughput']} Mbps\n"
        f"Eventos de congestión: {metricas['eventos_congestion']}"
    )

def cargar_resultados_csv(ruta_csv: str | Path = "exports/csv/resultados_simulacion.csv") -> pd.DataFrame:
    ruta = Path(ruta_csv)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo CSV: {ruta}")
    return pd.read_csv(ruta)

def analizar_resultados_con_pandas(ruta_csv: str | Path = "exports/csv/resultados_simulacion.csv") -> dict:
    df = cargar_resultados_csv(ruta_csv)

    enviados = len(df)
    recibidos = int((df["estado"] == "Recibido").sum())
    perdidos = int((df["estado"] == "Perdido").sum())
    tasa_perdida = round((perdidos / enviados) * 100, 2) if enviados > 0 else 0

    latencias = pd.to_numeric(df["latencia_ms"], errors="coerce").dropna()
    if len(latencias) > 0:
        latencia_promedio = round(float(np.mean(latencias)), 2)
        latencia_minima = round(float(np.min(latencias)), 2)
        latencia_maxima = round(float(np.max(latencias)), 2)
        latencia_desviacion = round(float(np.std(latencias)), 2)
    else:
        latencia_promedio = latencia_minima = latencia_maxima = latencia_desviacion = 0

    congestiones = int(df["congestion"].astype(str).str.lower().isin(["true", "1", "sí", "si"]).sum())

    return {
        "paquetes_enviados": enviados,
        "paquetes_recibidos": recibidos,
        "paquetes_perdidos": perdidos,
        "tasa_perdida": tasa_perdida,
        "latencia_promedio": latencia_promedio,
        "latencia_minima": latencia_minima,
        "latencia_maxima": latencia_maxima,
        "latencia_desviacion": latencia_desviacion,
        "eventos_congestion": congestiones
    }

def imprimir_analisis_pandas(ruta_csv: str | Path = "exports/csv/resultados_simulacion.csv") -> None:
    analisis = analizar_resultados_con_pandas(ruta_csv)
    print("\n========== ANÁLISIS CON PANDAS Y NUMPY ==========")
    print(f"Paquetes enviados: {analisis['paquetes_enviados']}")
    print(f"Paquetes recibidos: {analisis['paquetes_recibidos']}")
    print(f"Paquetes perdidos: {analisis['paquetes_perdidos']}")
    print(f"Tasa de pérdida: {analisis['tasa_perdida']}%")
    print(f"Latencia promedio: {analisis['latencia_promedio']} ms")
    print(f"Latencia mínima: {analisis['latencia_minima']} ms")
    print(f"Latencia máxima: {analisis['latencia_maxima']} ms")
    print(f"Desviación estándar de latencia: {analisis['latencia_desviacion']} ms")
    print(f"Eventos con congestión: {analisis['eventos_congestion']}")
    print("=================================================")
