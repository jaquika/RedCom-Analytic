class Red:
    """Agrupa nodos y enlaces dentro de una red."""
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo
        self.nodos = []
        self.enlaces = []

    def agregar_nodo(self, nodo) -> None:
        self.nodos.append(nodo)

    def agregar_enlace(self, enlace) -> None:
        self.enlaces.append(enlace)

    def mostrar_topologia(self) -> None:
        print(f"\nTopología: {self.nombre} | Tipo: {self.tipo}")
        print("\nNodos:")
        for nodo in self.nodos:
            print(f"- {nodo.mostrar_info()}")

        print("\nEnlaces:")
        for enlace in self.enlaces:
            print(
                f"- {enlace.nodo_origen.nombre} -> {enlace.nodo_destino.nombre} | "
                f"{enlace.velocidad_mbps} Mbps | {enlace.latencia_ms} ms | "
                f"Pérdida: {enlace.probabilidad_perdida * 100:.2f}%"
            )
