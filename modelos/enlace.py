import random
from modelos.paquete import Paquete
from simulacion.congestion import detectar_congestion

class Enlace:
    """Conexión física o lógica entre dos nodos de red."""
    def __init__(self, nodo_origen, nodo_destino, velocidad_mbps: float,
                 latencia_ms: float, probabilidad_perdida: float, capacidad_cola: int = 10):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.velocidad_mbps = velocidad_mbps
        self.latencia_ms = latencia_ms
        self.probabilidad_perdida = probabilidad_perdida
        self.capacidad_cola = capacidad_cola
        self.cola_paquetes = 0
        self.eventos_congestion = 0
        self.observadores = []

    def agregar_observador(self, observador) -> None:
        self.observadores.append(observador)

    def _notificar_congestion(self) -> None:
        mensaje = f"Congestión detectada en enlace {self.nodo_origen.nombre} -> {self.nodo_destino.nombre}."
        for observador in self.observadores:
            observador.notificar(mensaje)

    def transmitir(self, paquete: Paquete) -> dict:
        self.cola_paquetes += 1
        congestion = detectar_congestion(self.cola_paquetes, self.capacidad_cola)

        if congestion:
            self.eventos_congestion += 1
            self._notificar_congestion()
            probabilidad_real = min(self.probabilidad_perdida + 0.10, 1.0)
            penalizacion_latencia = (self.cola_paquetes - self.capacidad_cola) * 2
        else:
            probabilidad_real = self.probabilidad_perdida
            penalizacion_latencia = 0

        if random.random() < probabilidad_real:
            paquete.estado = "Perdido"
            return {"estado": "Perdido", "latencia_ms": None, "congestion": congestion}

        variacion = random.uniform(0, 5)
        latencia_final = round(self.latencia_ms + variacion + penalizacion_latencia, 2)
        paquete.estado = "Transmitido"
        return {"estado": "Transmitido", "latencia_ms": latencia_final, "congestion": congestion}
