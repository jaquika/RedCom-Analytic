import pytest
from pathlib import Path
from modelos.red_lan import RedLAN
from simulacion.trafico import MotorSimulacion
from analisis.reportes import exportar_resultados_csv
from analisis.estadisticas import (
    resumen_metricas, cargar_resultados_csv,
    analizar_resultados_con_pandas, imprimir_analisis_pandas
)
from analisis.graficas import (
    graficar_latencia, graficar_paquetes_recibidos_perdidos,
    graficar_congestion_por_paquete, generar_todas_las_graficas
)

def _generar_csv_de_prueba(tmp_path):
    red = RedLAN(perdida=0.0)
    resultado = MotorSimulacion(red).ejecutar(15)
    return exportar_resultados_csv(resultado["resultados"])

def test_resumen_metricas():
    metricas = {
        "paquetes_enviados": 10, "paquetes_recibidos": 9, "paquetes_perdidos": 1,
        "tasa_perdida": 10.0, "latencia_promedio": 12.3, "throughput": 90.0,
        "eventos_congestion": 0
    }
    texto = resumen_metricas(metricas)
    assert "Paquetes enviados: 10" in texto
    assert "Throughput: 90.0 Mbps" in texto

def test_cargar_csv_inexistente_lanza_error(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        cargar_resultados_csv("no_existe.csv")

def test_analizar_resultados_con_pandas(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ruta_csv = _generar_csv_de_prueba(tmp_path)
    analisis = analizar_resultados_con_pandas(ruta_csv)
    assert analisis["paquetes_enviados"] == 15
    assert analisis["paquetes_recibidos"] + analisis["paquetes_perdidos"] == 15

def test_imprimir_analisis_pandas(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    ruta_csv = _generar_csv_de_prueba(tmp_path)
    imprimir_analisis_pandas(ruta_csv)
    salida = capsys.readouterr().out
    assert "ANÁLISIS CON PANDAS Y NUMPY" in salida

def test_graficar_latencia(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ruta_csv = _generar_csv_de_prueba(tmp_path)
    ruta = graficar_latencia(ruta_csv)
    assert Path(ruta).exists()

def test_graficar_recibidos_perdidos(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ruta_csv = _generar_csv_de_prueba(tmp_path)
    ruta = graficar_paquetes_recibidos_perdidos(ruta_csv)
    assert Path(ruta).exists()

def test_graficar_congestion(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ruta_csv = _generar_csv_de_prueba(tmp_path)
    ruta = graficar_congestion_por_paquete(ruta_csv)
    assert Path(ruta).exists()

def test_generar_todas_las_graficas(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ruta_csv = _generar_csv_de_prueba(tmp_path)
    rutas = generar_todas_las_graficas(ruta_csv)
    assert len(rutas) == 4
    for ruta in rutas:
        assert Path(ruta).exists()
