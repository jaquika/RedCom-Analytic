from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from analisis.estadisticas import analizar_resultados_con_pandas, cargar_resultados_csv

def generar_informe_pdf(ruta_csv: str = "exports/csv/resultados_simulacion.csv",
                         ruta_pdf: str = "exports/pdf/informe_simulacion.pdf"):
    ruta_pdf = Path(ruta_pdf)
    ruta_pdf.parent.mkdir(parents=True, exist_ok=True)

    df = cargar_resultados_csv(ruta_csv)
    analisis = analizar_resultados_con_pandas(ruta_csv)

    df["latencia_ms"] = pd.to_numeric(df["latencia_ms"], errors="coerce")
    df_lat = df.dropna(subset=["latencia_ms"])

    with PdfPages(ruta_pdf) as pdf:
        # pagina 1: resumen en texto
        fig = plt.figure(figsize=(8.5, 11))
        texto = (
            "INFORME DE SIMULACION - RedCom Analytic\n\n"
            f"Paquetes enviados: {analisis['paquetes_enviados']}\n"
            f"Paquetes recibidos: {analisis['paquetes_recibidos']}\n"
            f"Paquetes perdidos: {analisis['paquetes_perdidos']}\n"
            f"Tasa de perdida: {analisis['tasa_perdida']}%\n"
            f"Latencia promedio: {analisis['latencia_promedio']} ms\n"
            f"Latencia minima: {analisis['latencia_minima']} ms\n"
            f"Latencia maxima: {analisis['latencia_maxima']} ms\n"
            f"Desviacion estandar: {analisis['latencia_desviacion']} ms\n"
            f"Eventos de congestion: {analisis['eventos_congestion']}\n"
        )
        fig.text(0.1, 0.5, texto, fontsize=12, va="center")
        pdf.savefig(fig)
        plt.close(fig)

        # pagina 2: latencia por paquete
        fig = plt.figure(figsize=(8.5, 11))
        plt.plot(df_lat["id_paquete"], df_lat["latencia_ms"], marker="o")
        plt.title("Evolucion de latencia por paquete")
        plt.xlabel("ID del paquete")
        plt.ylabel("Latencia (ms)")
        plt.grid(True)
        pdf.savefig(fig)
        plt.close(fig)

        # pagina 3: recibidos vs perdidos
        fig = plt.figure(figsize=(8.5, 11))
        conteo = df["estado"].value_counts()
        plt.bar(conteo.index, conteo.values)
        plt.title("Paquetes recibidos vs perdidos")
        pdf.savefig(fig)
        plt.close(fig)

        # pagina 4: histograma de latencia
        fig = plt.figure(figsize=(8.5, 11))
        plt.hist(df_lat["latencia_ms"], bins=10, edgecolor="black")
        plt.title("Distribucion de la latencia")
        pdf.savefig(fig)
        plt.close(fig)

    return ruta_pdf
