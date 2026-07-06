from pathlib import Path

def preparar_entorno() -> None:
    carpetas = [
        Path("data"), Path("data/resultados"), Path("logs"),
        Path("exports/csv"), Path("exports/pdf"), Path("exports/graficas")
    ]
    for carpeta in carpetas:
        carpeta.mkdir(parents=True, exist_ok=True)
