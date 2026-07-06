from utils.logs import registrar_evento
from simulacion.observador import ObservadorCongestion

class RegistroEventos(ObservadorCongestion):
    """Administra los eventos generados durante la simulación.
    También funciona como observador: los enlaces le avisan cuando hay congestión."""
    def __init__(self):
        self.eventos = []

    def agregar(self, mensaje: str) -> None:
        linea = registrar_evento(mensaje)
        self.eventos.append(linea)

    def obtener_eventos(self) -> list:
        return self.eventos

    def notificar(self, mensaje: str) -> None:
        self.agregar(mensaje)
