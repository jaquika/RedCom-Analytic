from modelos.dispositivo_red import DispositivoRed
from modelos.paquete import Paquete

class Switch(DispositivoRed):
    """Dispositivo de interconexión dentro de una red LAN."""
    def __init__(self, nombre: str, ip: str, puertos: int = 8):
        super().__init__(nombre, ip)
        self._puertos = puertos
        self._tabla_mac = {}

    @property
    def puertos(self):
        return self._puertos

    @property
    def tabla_mac(self):
        return self._tabla_mac

    def procesar_paquete(self, paquete: Paquete) -> str:
        self._buffer.append(paquete)
        return f"Switch {self.nombre} reenvió el paquete {paquete.id_paquete}"

    def reenviar_paquete(self, paquete: Paquete) -> str:
        return self.procesar_paquete(paquete)
