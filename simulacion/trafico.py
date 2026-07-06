from simulacion.eventos import RegistroEventos
from simulacion.metricas import calcular_metricas

class MotorSimulacion:
    """Ejecuta la transmisión masiva de paquetes dentro de una red."""
    def __init__(self, red):
        self.red = red
        self.resultados = []
        self.eventos = RegistroEventos()
        self.contador_paquetes = 1

        for enlace in self.red.enlaces:
            enlace.agregar_observador(self.eventos)

    def ejecutar(self, cantidad_paquetes: int = 20) -> dict:
        if not self.red.nodos or not self.red.enlaces:
            raise ValueError("La red no tiene nodos o enlaces configurados.")

        origen = self.red.nodos[0]
        destino = self.red.nodos[-1]

        self.eventos.agregar(f"Iniciando simulación en red {self.red.tipo}.")
        self.eventos.agregar(f"Origen: {origen.nombre} | Destino: {destino.nombre}")
        self.eventos.agregar(f"Cantidad de paquetes: {cantidad_paquetes}")

        for _ in range(cantidad_paquetes):
            paquete = origen.enviar_paquete(
                self.contador_paquetes, destino, "Datos de prueba RedCom Analytic"
            )

            self.eventos.agregar(
                f"Paquete {paquete.id_paquete} enviado desde {paquete.origen} hacia {paquete.destino}."
            )

            total_latencia = 0.0
            paquete_perdido = False
            hubo_congestion = False

            for enlace in self.red.enlaces:
                resultado = enlace.transmitir(paquete)

                if resultado["congestion"]:
                    hubo_congestion = True
                    # ya no se registra aquí manualmente: el enlace avisa solo a sus observadores

                if resultado["estado"] == "Perdido":
                    paquete_perdido = True
                    self.eventos.agregar(
                        f"Paquete {paquete.id_paquete} perdido en enlace {enlace.nodo_origen.nombre} -> {enlace.nodo_destino.nombre}."
                    )
                    break

                total_latencia += resultado["latencia_ms"]

            if paquete_perdido:
                estado_final = "Perdido"
                latencia_final = None
            else:
                estado_final = "Recibido"
                latencia_final = round(total_latencia, 2)
                self.eventos.agregar(
                    f"Paquete {paquete.id_paquete} recibido correctamente. Latencia total: {latencia_final} ms."
                )

            self.resultados.append({
                "id_paquete": paquete.id_paquete,
                "tipo_red": self.red.tipo,
                "origen": paquete.origen,
                "destino": paquete.destino,
                "estado": estado_final,
                "latencia_ms": latencia_final,
                "congestion": hubo_congestion
            })
            self.contador_paquetes += 1

        velocidad_minima = min(enlace.velocidad_mbps for enlace in self.red.enlaces)
        metricas = calcular_metricas(self.resultados, velocidad_minima)
        self.eventos.agregar("Simulación finalizada.")
        self.eventos.agregar(f"Métricas finales: {metricas}")

        return {"resultados": self.resultados, "metricas": metricas, "eventos": self.eventos.obtener_eventos()}
