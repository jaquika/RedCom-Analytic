from abc import abstractmethod
from modelos.nodo import Nodo

class DispositivoRed(Nodo):
    """Dispositivos de infraestructura de red (Router, Switch).
    Va entre Nodo y las clases finales para tener herencia de dos niveles."""
    def __init__(self, nombre: str, ip: str):
        super().__init__(nombre, ip)
        self._buffer = []

    @property
    def buffer(self):
        return self._buffer

    @abstractmethod
    def procesar_paquete(self, paquete) -> str:
        pass
