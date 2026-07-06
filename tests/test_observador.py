from modelos.host import Host
from modelos.enlace import Enlace
from modelos.paquete import Paquete
from simulacion.observador import ObservadorCongestion

class ObservadorDePrueba(ObservadorCongestion):
    def __init__(self):
        self.mensajes = []

    def notificar(self, mensaje):
        self.mensajes.append(mensaje)

def test_enlace_notifica_congestion_a_sus_observadores():
    host_a = Host("A", "192.168.1.10")
    host_b = Host("B", "192.168.1.20")
    enlace = Enlace(host_a, host_b, 100, 5, 0.0, capacidad_cola=2)

    observador = ObservadorDePrueba()
    enlace.agregar_observador(observador)

    for i in range(1, 5):
        paquete = Paquete(i, host_a.ip, host_b.ip, "prueba")
        enlace.transmitir(paquete)

    assert len(observador.mensajes) > 0
    assert "Congestión" in observador.mensajes[0]

def test_enlace_sin_congestion_no_notifica():
    host_a = Host("A", "192.168.1.10")
    host_b = Host("B", "192.168.1.20")
    enlace = Enlace(host_a, host_b, 100, 5, 0.0, capacidad_cola=100)

    observador = ObservadorDePrueba()
    enlace.agregar_observador(observador)

    paquete = Paquete(1, host_a.ip, host_b.ip, "prueba")
    enlace.transmitir(paquete)

    assert len(observador.mensajes) == 0
