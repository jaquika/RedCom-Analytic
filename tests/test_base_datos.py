from base_datos.conexion_sqlite import crear_tablas
from base_datos.guardar_resultados import guardar_metricas
from base_datos.historial import obtener_historial
from base_datos.topologias import guardar_topologia, obtener_topologias, obtener_topologia_por_id

def test_crear_tablas_no_falla(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    crear_tablas()
    assert (tmp_path / "data" / "simulaciones.db").exists()

def test_guardar_y_obtener_metricas(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    metricas = {
        "paquetes_enviados": 10, "paquetes_recibidos": 8, "paquetes_perdidos": 2,
        "tasa_perdida": 20.0, "latencia_promedio": 15.5, "throughput": 80.0,
        "eventos_congestion": 1
    }
    guardar_metricas("LAN", metricas)
    historial = obtener_historial()
    assert len(historial) == 1
    assert historial[0][1] == "LAN"

def test_guardar_y_obtener_topologia(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    guardar_topologia("LAN_Principal", "LAN", 100, 5, 0.01, 10)
    topologias = obtener_topologias()
    assert len(topologias) == 1
    assert topologias[0][1] == "LAN_Principal"
    assert topologias[0][2] == "LAN"

def test_obtener_topologia_por_id(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    guardar_topologia("WAN_Principal", "WAN", 10, 100, 0.05, 8)
    topologias = obtener_topologias()
    id_guardado = topologias[0][0]
    fila = obtener_topologia_por_id(id_guardado)
    assert fila is not None
    assert fila[2] == "WAN"

def test_obtener_topologia_id_inexistente(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    fila = obtener_topologia_por_id(999)
    assert fila is None
