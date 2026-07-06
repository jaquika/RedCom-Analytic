from modelos.nodo import Nodo
from modelos.paquete import Paquete

class Host(Nodo):
    """Dispositivo final que puede enviar o recibir paquetes."""
    def __init__(self, nombre: str, ip: str):
        super().__init__(nombre, ip)
        self._puerta_enlace = ""

    @property
    def puerta_enlace(self):
        return self._puerta_enlace

    @puerta_enlace.setter
    def puerta_enlace(self, valor):
        self._puerta_enlace = valor

    def enviar_paquete(self, id_paquete: int, destino: "Host", contenido: str) -> Paquete:
        return Paquete(id_paquete, self.ip, destino.ip, contenido)

    def recibir_paquete(self, paquete: Paquete) -> str:
        paquete.estado = "Recibido"
        return f"{self.nombre} recibió el paquete {paquete.id_paquete}"

    def procesar_paquete(self, paquete: Paquete) -> str:
        return self.recibir_paquete(paquete)
