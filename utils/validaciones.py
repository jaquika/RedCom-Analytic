def leer_entero(mensaje: str, valor_defecto: int) -> int:
    entrada = input(f"{mensaje} [{valor_defecto}]: ").strip()
    return valor_defecto if entrada == "" else int(entrada)

def leer_float(mensaje: str, valor_defecto: float) -> float:
    entrada = input(f"{mensaje} [{valor_defecto}]: ").strip()
    return valor_defecto if entrada == "" else float(entrada)

def validar_porcentaje(valor: float) -> float:
    if valor < 0:
        return 0.0
    if valor > 100:
        return 1.0
    return valor / 100
