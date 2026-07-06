import csv
from pathlib import Path

def exportar_resultados_csv(resultados: list, nombre_archivo: str = "resultados_simulacion.csv") -> Path:
    ruta = Path("exports/csv") / nombre_archivo
    ruta.parent.mkdir(parents=True, exist_ok=True)

    columnas = ["id_paquete", "tipo_red", "origen", "destino", "estado", "latencia_ms", "congestion"]
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(resultados)
    return ruta
