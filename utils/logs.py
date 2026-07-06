from datetime import datetime
from pathlib import Path

LOGS_DIR = Path("logs")

def preparar_logs() -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

def registrar_evento(mensaje: str, nombre_archivo: str = "eventos_redcom.txt") -> str:
    preparar_logs()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{timestamp}] {mensaje}"
    print(linea)
    with (LOGS_DIR / nombre_archivo).open("a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")
    return linea
