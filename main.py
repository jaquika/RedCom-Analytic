from interfaz.menu import MenuPrincipal
from utils.helpers import preparar_entorno
from utils.logs import registrar_evento

def main():
    preparar_entorno()
    registrar_evento("Sistema RedCom Analytic iniciado.")
    menu = MenuPrincipal()
    menu.arrancar()

if __name__ == "__main__":
    main()
