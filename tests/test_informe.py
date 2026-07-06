from pathlib import Path
from modelos.red_lan import RedLAN
from simulacion.trafico import MotorSimulacion
from analisis.reportes import exportar_resultados_csv
from analisis.informe import generar_informe_pdf

def test_generar_informe_pdf(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    red = RedLAN(perdida=0.0)
    resultado = MotorSimulacion(red).ejecutar(10)
    ruta_csv = exportar_resultados_csv(resultado["resultados"])

    ruta_pdf = generar_informe_pdf(ruta_csv)
    assert Path(ruta_pdf).exists()
    assert Path(ruta_pdf).stat().st_size > 0

def test_informe_falla_sin_csv(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    try:
        generar_informe_pdf("no_existe.csv")
        assert False, "debería haber lanzado FileNotFoundError"
    except FileNotFoundError:
        pass
