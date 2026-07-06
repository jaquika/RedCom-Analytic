from pathlib import Path
import pandas as pd

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

CSV_DEFECTO = Path("exports/csv/resultados_simulacion.csv")
GRAFICAS_DIR = Path("exports/graficas")

def _cargar_dataframe(ruta_csv: str | Path = CSV_DEFECTO) -> pd.DataFrame:
    ruta = Path(ruta_csv)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo CSV: {ruta}")
    return pd.read_csv(ruta)

def graficar_latencia(ruta_csv: str | Path = CSV_DEFECTO, nombre_archivo: str = "01_latencia_por_paquete.png"):
    if plt is None:
        print("Matplotlib no está instalado.")
        return None
    df = _cargar_dataframe(ruta_csv)
    df["latencia_ms"] = pd.to_numeric(df["latencia_ms"], errors="coerce")
    df_latencia = df.dropna(subset=["latencia_ms"])

    GRAFICAS_DIR.mkdir(parents=True, exist_ok=True)
    ruta = GRAFICAS_DIR / nombre_archivo

    plt.figure(figsize=(10, 5))
    plt.plot(df_latencia["id_paquete"], df_latencia["latencia_ms"], marker="o")
    plt.title("Evolución de latencia por paquete")
    plt.xlabel("ID del paquete")
    plt.ylabel("Latencia (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(ruta)
    plt.close()
    return ruta

def graficar_paquetes_recibidos_perdidos(ruta_csv: str | Path = CSV_DEFECTO, nombre_archivo: str = "02_paquetes_recibidos_vs_perdidos.png"):
    if plt is None:
        print("Matplotlib no está instalado.")
        return None
    df = _cargar_dataframe(ruta_csv)
    conteo = df["estado"].value_counts()

    GRAFICAS_DIR.mkdir(parents=True, exist_ok=True)
    ruta = GRAFICAS_DIR / nombre_archivo

    plt.figure(figsize=(8, 5))
    plt.bar(conteo.index, conteo.values)
    plt.title("Paquetes recibidos vs perdidos")
    plt.xlabel("Estado del paquete")
    plt.ylabel("Cantidad")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(ruta)
    plt.close()
    return ruta

def graficar_congestion_por_paquete(ruta_csv: str | Path = CSV_DEFECTO, nombre_archivo: str = "03_congestion_por_paquete.png"):
    if plt is None:
        print("Matplotlib no está instalado.")
        return None
    df = _cargar_dataframe(ruta_csv)
    df["congestion_num"] = df["congestion"].astype(str).str.lower().isin(["true", "1", "sí", "si"]).astype(int)

    GRAFICAS_DIR.mkdir(parents=True, exist_ok=True)
    ruta = GRAFICAS_DIR / nombre_archivo

    plt.figure(figsize=(10, 5))
    plt.bar(df["id_paquete"], df["congestion_num"])
    plt.title("Congestión detectada por paquete")
    plt.xlabel("ID del paquete")
    plt.ylabel("Congestión (1 = Sí, 0 = No)")
    plt.yticks([0, 1])
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(ruta)
    plt.close()
    return ruta

def graficar_histograma_latencia(ruta_csv: str | Path = CSV_DEFECTO, nombre_archivo: str = "04_histograma_latencia.png"):
    # Histograma: cuántos paquetes cayeron en cada rango de latencia
    if plt is None:
        print("Matplotlib no está instalado.")
        return None
    df = _cargar_dataframe(ruta_csv)
    df["latencia_ms"] = pd.to_numeric(df["latencia_ms"], errors="coerce")
    latencias = df["latencia_ms"].dropna()

    if latencias.empty:
        print("No hay datos de latencia para graficar.")
        return None

    GRAFICAS_DIR.mkdir(parents=True, exist_ok=True)
    ruta = GRAFICAS_DIR / nombre_archivo

    plt.figure(figsize=(8, 5))
    plt.hist(latencias, bins=10, edgecolor="black")
    plt.title("Distribución de la latencia")
    plt.xlabel("Latencia (ms)")
    plt.ylabel("Cantidad de paquetes")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(ruta)
    plt.close()
    return ruta

def graficar_comparacion_escenarios(metricas_lan: dict, metricas_wan: dict, nombre_archivo: str = "05_comparacion_escenarios.png"):
    # Compara LAN vs WAN en 3 indicadores: tasa de pérdida, latencia y throughput
    if plt is None:
        print("Matplotlib no está instalado.")
        return None

    GRAFICAS_DIR.mkdir(parents=True, exist_ok=True)
    ruta = GRAFICAS_DIR / nombre_archivo

    etiquetas = ["Tasa de pérdida (%)", "Latencia promedio (ms)", "Throughput (Mbps)"]
    valores_lan = [metricas_lan["tasa_perdida"], metricas_lan["latencia_promedio"], metricas_lan["throughput"]]
    valores_wan = [metricas_wan["tasa_perdida"], metricas_wan["latencia_promedio"], metricas_wan["throughput"]]

    posiciones = [0, 1, 2]
    posiciones_wan = [p + 0.35 for p in posiciones]

    plt.figure(figsize=(9, 5))
    plt.bar(posiciones, valores_lan, width=0.35, label="LAN")
    plt.bar(posiciones_wan, valores_wan, width=0.35, label="WAN")
    plt.xticks([p + 0.175 for p in posiciones], etiquetas)
    plt.title("Comparación LAN vs WAN")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(ruta)
    plt.close()
    return ruta

def generar_todas_las_graficas(ruta_csv: str | Path = CSV_DEFECTO) -> list:
    rutas = [
        graficar_latencia(ruta_csv),
        graficar_paquetes_recibidos_perdidos(ruta_csv),
        graficar_congestion_por_paquete(ruta_csv),
        graficar_histograma_latencia(ruta_csv),
    ]
    return [ruta for ruta in rutas if ruta is not None]
