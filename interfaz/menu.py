from modelos.red_lan import RedLAN
from modelos.red_wan import RedWAN
from simulacion.trafico import MotorSimulacion
from analisis.reportes import exportar_resultados_csv
from analisis.estadisticas import resumen_metricas, imprimir_analisis_pandas
from analisis.graficas import generar_todas_las_graficas, graficar_comparacion_escenarios
from analisis.informe import generar_informe_pdf
from base_datos.guardar_resultados import guardar_metricas
from base_datos.historial import obtener_historial
from base_datos.topologias import guardar_topologia, obtener_topologias
from utils.validaciones import leer_entero, leer_float, validar_porcentaje
from utils.logs import registrar_evento

class MenuPrincipal:
    """Interfaz por consola del sistema RedCom Analytic."""
    def __init__(self):
        self.red_actual = None
        self.ultimo_resultado = None

    def configurar_lan(self):
        print("\n--- CONFIGURACIÓN LAN ---")
        velocidad = leer_float("Velocidad Mbps", 100)
        latencia = leer_float("Latencia ms", 5)
        perdida = validar_porcentaje(leer_float("Pérdida de paquetes %", 1))
        cola = leer_entero("Capacidad de cola", 10)

        self.red_actual = RedLAN(
            velocidad_mbps=velocidad, latencia_ms=latencia,
            perdida=perdida, capacidad_cola=cola
        )
        registrar_evento("Red LAN configurada.")
        self.red_actual.mostrar_topologia()

        guardar_topologia("LAN_Principal", "LAN", velocidad, latencia, perdida, cola)

    def configurar_wan(self):
        print("\n--- CONFIGURACIÓN WAN ---")
        velocidad = leer_float("Velocidad Mbps", 10)
        latencia = leer_float("Latencia ms", 100)
        perdida = validar_porcentaje(leer_float("Pérdida de paquetes %", 5))
        cola = leer_entero("Capacidad de cola", 8)

        self.red_actual = RedWAN(
            velocidad_mbps=velocidad, latencia_ms=latencia,
            perdida=perdida, capacidad_cola=cola
        )
        registrar_evento("Red WAN configurada.")
        self.red_actual.mostrar_topologia()

        guardar_topologia("WAN_Principal", "WAN", velocidad, latencia, perdida, cola)

    def cargar_topologia_guardada(self):
        topologias = obtener_topologias()
        print("\n--- TOPOLOGÍAS GUARDADAS ---")
        if not topologias:
            print("No hay topologías guardadas todavía.")
            return

        for fila in topologias:
            print(f"{fila[0]}. {fila[1]} ({fila[2]}) - {fila[3]} Mbps, {fila[4]} ms, "
                  f"pérdida {fila[5]}, cola {fila[6]}")

        id_elegido = leer_entero("ID de la topología a cargar", topologias[0][0])
        elegida = next((fila for fila in topologias if fila[0] == id_elegido), None)
        if elegida is None:
            print("ID no encontrado.")
            return

        _, nombre, tipo_red, velocidad, latencia, perdida, cola, _fecha = elegida
        if tipo_red == "LAN":
            self.red_actual = RedLAN(velocidad_mbps=velocidad, latencia_ms=latencia,
                                      perdida=perdida, capacidad_cola=cola)
        else:
            self.red_actual = RedWAN(velocidad_mbps=velocidad, latencia_ms=latencia,
                                      perdida=perdida, capacidad_cola=cola)

        registrar_evento(f"Topología cargada desde SQLite: {nombre}")
        self.red_actual.mostrar_topologia()

    def ejecutar_simulacion(self):
        if self.red_actual is None:
            print("Primero configure una red LAN o WAN.")
            return
        cantidad = leer_entero("Cantidad de paquetes", 20)
        motor = MotorSimulacion(self.red_actual)
        self.ultimo_resultado = motor.ejecutar(cantidad)

        print("\n========== MÉTRICAS ==========")
        print(resumen_metricas(self.ultimo_resultado["metricas"]))
        print("==============================")

        guardar_metricas(self.red_actual.tipo, self.ultimo_resultado["metricas"])

    def exportar_csv(self):
        if self.ultimo_resultado is None:
            print("No hay resultados para exportar.")
            return
        ruta = exportar_resultados_csv(self.ultimo_resultado["resultados"])
        registrar_evento(f"Resultados exportados en CSV: {ruta}")

    def analizar_con_pandas(self):
        try:
            imprimir_analisis_pandas()
            registrar_evento("Análisis con Pandas y NumPy ejecutado correctamente.")
        except FileNotFoundError:
            print("Primero debe exportar los resultados en CSV.")

    def generar_graficas(self):
        try:
            rutas = generar_todas_las_graficas()
            for ruta in rutas:
                registrar_evento(f"Gráfica generada: {ruta}")
        except FileNotFoundError:
            print("Primero debe exportar los resultados en CSV.")

    def comparar_escenarios(self):
        print("\n--- COMPARACIÓN DE ESCENARIOS: LAN vs WAN ---")
        cantidad = leer_entero("Cantidad de paquetes por escenario", 20)

        resultado_lan = MotorSimulacion(RedLAN()).ejecutar(cantidad)
        resultado_wan = MotorSimulacion(RedWAN()).ejecutar(cantidad)

        print("\nLAN:")
        print(resumen_metricas(resultado_lan["metricas"]))
        print("\nWAN:")
        print(resumen_metricas(resultado_wan["metricas"]))

        ruta = graficar_comparacion_escenarios(resultado_lan["metricas"], resultado_wan["metricas"])
        if ruta:
            registrar_evento(f"Gráfica de comparación generada: {ruta}")
            print(f"\nGráfica guardada en: {ruta}")

    def generar_informe(self):
        try:
            ruta = generar_informe_pdf()
            registrar_evento(f"Informe PDF generado: {ruta}")
            print(f"\nInforme generado en: {ruta}")
        except FileNotFoundError:
            print("Primero debe exportar los resultados en CSV.")

    def ver_historial(self):
        historial = obtener_historial()
        print("\n========== HISTORIAL ==========")
        if not historial:
            print("No hay simulaciones registradas.")
            return
        for fila in historial:
            print(fila)
        print("===============================")

    def arrancar(self):
        while True:
            print("\n====================================")
            print("     REDCOM ANALYTIC - SIMULADOR    ")
            print("====================================")
            print("1. Configurar red LAN")
            print("2. Configurar red WAN")
            print("3. Ejecutar simulación")
            print("4. Exportar resultados CSV")
            print("5. Analizar resultados con Pandas y NumPy")
            print("6. Generar gráficas con Matplotlib")
            print("7. Comparar escenarios LAN vs WAN")
            print("8. Generar informe en PDF")
            print("9. Cargar topología guardada")
            print("10. Ver historial SQLite")
            print("11. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.configurar_lan()
            elif opcion == "2":
                self.configurar_wan()
            elif opcion == "3":
                self.ejecutar_simulacion()
            elif opcion == "4":
                self.exportar_csv()
            elif opcion == "5":
                self.analizar_con_pandas()
            elif opcion == "6":
                self.generar_graficas()
            elif opcion == "7":
                self.comparar_escenarios()
            elif opcion == "8":
                self.generar_informe()
            elif opcion == "9":
                self.cargar_topologia_guardada()
            elif opcion == "10":
                self.ver_historial()
            elif opcion == "11":
                registrar_evento("Sistema cerrado.")
                break
            else:
                print("Opción no válida.")
