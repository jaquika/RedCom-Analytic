def detectar_congestion(cola_paquetes: int, capacidad_cola: int) -> bool:
    """Detecta congestión cuando la cola supera la capacidad máxima permitida."""
    return cola_paquetes > capacidad_cola
