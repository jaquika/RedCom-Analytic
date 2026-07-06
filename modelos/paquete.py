class Paquete:
    """Unidad de información transmitida dentro de la simulación."""
    def __init__(self, id_paquete: int, origen: str, destino: str, contenido: str):
        self.id_paquete = id_paquete
        self.origen = origen
        self.destino = destino
        self.contenido = contenido
        self.estado = "Creado"
        self.latencia_total_ms = 0.0
