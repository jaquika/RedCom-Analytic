from abc import ABC, abstractmethod

class ObservadorCongestion(ABC):
    """Cualquier clase que quiera enterarse cuando un enlace se congestiona
    debe heredar de aquí e implementar notificar()."""
    @abstractmethod
    def notificar(self, mensaje: str) -> None:
        pass
