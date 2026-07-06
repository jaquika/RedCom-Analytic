import pytest
from modelos.nodo import Nodo
from modelos.dispositivo_red import DispositivoRed
from modelos.host import Host
from modelos.router import Router
from modelos.switch import Switch
from modelos.enlace import Enlace
from modelos.paquete import Paquete
from modelos.red_lan import RedLAN
from modelos.red_wan import RedWAN
from simulacion.congestion import detectar_congestion
from simulacion.metricas import calcular_metricas

def test_crear_host():
    host = Host("Host_A", "192.168.1.10")
    assert host.nombre == "Host_A"
    assert host.ip == "192.168.1.10"

def test_crear_router():
    router = Router("Router_1", "192.168.1.1")
    assert router.estado == "Activo"
    assert router.tabla_enrutamiento == {}

def test_crear_switch():
    switch = Switch("Switch_1", "192.168.1.2")
    assert switch.puertos == 8

def test_crear_paquete():
    paquete = Paquete(1, "192.168.1.10", "192.168.1.20", "Prueba")
    assert paquete.id_paquete == 1
    assert paquete.estado == "Creado"

def test_crear_enlace():
    host_a = Host("A", "192.168.1.10")
    host_b = Host("B", "192.168.1.20")
    enlace = Enlace(host_a, host_b, 100, 5, 0.01)
    assert enlace.velocidad_mbps == 100
    assert enlace.latencia_ms == 5

def test_crear_red_lan():
    red = RedLAN()
    assert red.tipo == "LAN"
    assert len(red.nodos) == 4
    assert len(red.enlaces) == 3

def test_crear_red_wan():
    red = RedWAN()
    assert red.tipo == "WAN"
    assert len(red.nodos) == 4
    assert len(red.enlaces) == 3

def test_detectar_congestion_true():
    assert detectar_congestion(12, 10) is True

def test_detectar_congestion_false():
    assert detectar_congestion(5, 10) is False

def test_calcular_metricas():
    resultados = [
        {"estado": "Recibido", "latencia_ms": 10, "congestion": False},
        {"estado": "Perdido", "latencia_ms": None, "congestion": True},
        {"estado": "Recibido", "latencia_ms": 20, "congestion": False},
    ]
    metricas = calcular_metricas(resultados, 100)
    assert metricas["paquetes_enviados"] == 3
    assert metricas["paquetes_recibidos"] == 2
    assert metricas["paquetes_perdidos"] == 1

def test_nodo_es_abstracto():
    with pytest.raises(TypeError):
        Nodo("Generico", "0.0.0.0")

def test_router_y_switch_heredan_de_dispositivo_red():
    router = Router("Router_1", "192.168.1.1")
    switch = Switch("Switch_1", "192.168.1.2")
    assert isinstance(router, DispositivoRed)
    assert isinstance(switch, DispositivoRed)

def test_polimorfismo_procesar_paquete():
    host = Host("Host_A", "192.168.1.10")
    router = Router("Router_1", "192.168.1.1")
    switch = Switch("Switch_1", "192.168.1.2")
    paquete = Paquete(1, "192.168.1.10", "192.168.1.20", "Prueba")

    assert "recibió" in host.procesar_paquete(paquete)
    assert "procesó" in router.procesar_paquete(paquete)
    assert "reenvió" in switch.procesar_paquete(paquete)
