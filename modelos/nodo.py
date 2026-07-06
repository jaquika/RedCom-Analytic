from abc import ABC, abstractmethod

class Nodo(ABC):
    """Clase base para los dispositivos de la red."""
    def __init__(self, nombre: str, ip: str):
        self._nombre = nombre
        self._ip = ip
        self._estado = "Activo"

    @property
    def nombre(self):
        return self._nombre

    @property
    def ip(self):
        return self._ip

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    def mostrar_info(self) -> str:
        return f"{self.nombre} | IP: {self.ip} | Estado: {self.estado}"

    @abstractmethod
    def procesar_paquete(self, paquete) -> str:
        pass
