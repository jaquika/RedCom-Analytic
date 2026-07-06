from modelos.red import Red
from modelos.host import Host
from modelos.router import Router
from modelos.enlace import Enlace

class RedWAN(Red):
    """Red de área amplia: menor velocidad, mayor latencia y mayor pérdida."""
    def __init__(self, nombre: str = "WAN_Principal", velocidad_mbps: float = 10,
                 latencia_ms: float = 100, perdida: float = 0.05, capacidad_cola: int = 8):
        super().__init__(nombre, "WAN")
        host_origen = Host("Host_Origen", "10.0.0.10")
        router_lima = Router("Router_Lima", "10.0.0.1")
        router_remoto = Router("Router_Remoto", "172.16.0.1")
        host_destino = Host("Host_Destino", "172.16.0.20")

        for nodo in [host_origen, router_lima, router_remoto, host_destino]:
            self.agregar_nodo(nodo)

        self.agregar_enlace(Enlace(host_origen, router_lima, velocidad_mbps, latencia_ms, perdida, capacidad_cola))
        self.agregar_enlace(Enlace(router_lima, router_remoto, velocidad_mbps, latencia_ms, perdida, capacidad_cola))
        self.agregar_enlace(Enlace(router_remoto, host_destino, velocidad_mbps, latencia_ms, perdida, capacidad_cola))
