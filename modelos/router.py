from modelos.dispositivo_red import DispositivoRed
from modelos.paquete import Paquete

class Router(DispositivoRed):
    """Dispositivo encargado del encaminamiento de paquetes entre redes."""
    def __init__(self, nombre: str, ip: str):
        super().__init__(nombre, ip)
        self._tabla_enrutamiento = {}

    @property
    def tabla_enrutamiento(self):
        return self._tabla_enrutamiento

    def agregar_ruta(self, destino: str, siguiente_salto: str) -> None:
        self._tabla_enrutamiento[destino] = siguiente_salto

    def procesar_paquete(self, paquete: Paquete) -> str:
        self._buffer.append(paquete)
        return f"Router {self.nombre} procesó el paquete {paquete.id_paquete}"
