from pathlib import Path
from modelos.red_lan import RedLAN
from modelos.red_wan import RedWAN
from simulacion.trafico import MotorSimulacion
from analisis.reportes import exportar_resultados_csv
from analisis.graficas import graficar_histograma_latencia, graficar_comparacion_escenarios

def test_simulacion_lan_basica():
    red = RedLAN(perdida=0.0)
    motor = MotorSimulacion(red)
    resultado = motor.ejecutar(5)
    assert resultado["metricas"]["paquetes_enviados"] == 5
    assert resultado["metricas"]["paquetes_recibidos"] >= 0

def test_graficar_histograma_latencia(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    red = RedLAN(perdida=0.0)
    resultado = MotorSimulacion(red).ejecutar(10)
    ruta_csv = exportar_resultados_csv(resultado["resultados"])
    ruta_grafica = graficar_histograma_latencia(ruta_csv)
    assert ruta_grafica is not None
    assert Path(ruta_grafica).exists()

def test_graficar_comparacion_escenarios(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    metricas_lan = MotorSimulacion(RedLAN(perdida=0.0)).ejecutar(10)["metricas"]
    metricas_wan = MotorSimulacion(RedWAN(perdida=0.0)).ejecutar(10)["metricas"]
    ruta_grafica = graficar_comparacion_escenarios(metricas_lan, metricas_wan)
    assert ruta_grafica is not None
    assert Path(ruta_grafica).exists()
