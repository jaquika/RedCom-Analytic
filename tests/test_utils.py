from pathlib import Path
from utils.helpers import preparar_entorno
from utils.logs import registrar_evento
from utils.validaciones import validar_porcentaje

def test_preparar_entorno_crea_carpetas(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    preparar_entorno()
    assert (tmp_path / "data").exists()
    assert (tmp_path / "exports" / "csv").exists()
    assert (tmp_path / "exports" / "pdf").exists()
    assert (tmp_path / "exports" / "graficas").exists()

def test_registrar_evento_escribe_log(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    registrar_evento("mensaje de prueba")
    contenido = (tmp_path / "logs" / "eventos_redcom.txt").read_text(encoding="utf-8")
    assert "mensaje de prueba" in contenido

def test_validar_porcentaje_normal():
    assert validar_porcentaje(50) == 0.5

def test_validar_porcentaje_negativo():
    assert validar_porcentaje(-10) == 0.0

def test_validar_porcentaje_mayor_a_100():
    assert validar_porcentaje(150) == 1.0
