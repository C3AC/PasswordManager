import sys
from src.ui.cli import run_cli
from src.ui.gui import run_gui

def main():
    """
    Punto de entrada principal del programa.
    Decide si ejecutar la interfaz de línea de comandos (CLI) o la interfaz gráfica (GUI).
    """
    if len(sys.argv) > 1:  # Si hay argumentos en la línea de comandos, usar CLI
        run_cli()
    else:  # Si no hay argumentos, usar GUI
        run_gui()
    # Ejecutar la función principal
if __name__ == "__main__":
    main()