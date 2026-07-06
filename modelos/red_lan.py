from modelos.red import Red
from modelos.host import Host
from modelos.switch import Switch
from modelos.router import Router
from modelos.enlace import Enlace

class RedLAN(Red):
    """Red de área local: alta velocidad, baja latencia y baja pérdida."""
    def __init__(self, nombre: str = "LAN_Principal", velocidad_mbps: float = 100,
                 latencia_ms: float = 5, perdida: float = 0.01, capacidad_cola: int = 10):
        super().__init__(nombre, "LAN")
        host_a = Host("Host_A", "192.168.1.10")
        switch = Switch("Switch_1", "192.168.1.2")
        router = Router("Router_LAN", "192.168.1.1")
        host_b = Host("Host_B", "192.168.1.20")

        for nodo in [host_a, switch, router, host_b]:
            self.agregar_nodo(nodo)

        self.agregar_enlace(Enlace(host_a, switch, velocidad_mbps, latencia_ms, perdida, capacidad_cola))
        self.agregar_enlace(Enlace(switch, router, velocidad_mbps, latencia_ms, perdida, capacidad_cola))
        self.agregar_enlace(Enlace(router, host_b, velocidad_mbps, latencia_ms, perdida, capacidad_cola))
