import argparse
from src.core.password_generator import generate_password

def run_cli():
    """
    Ejecuta la interfaz de línea de comandos (CLI).
    """
    parser = argparse.ArgumentParser(description="Gestor de contraseñas - Generador básico")

    subparsers = parser.add_subparsers(dest='command')

    # Subcomando: generate
    generate_parser = subparsers.add_parser('generate', help="Generar una contraseña segura")
    generate_parser.add_argument('--length', type=int, default=12, help='Longitud de la contraseña')
    generate_parser.add_argument('--no-upper', action='store_true', help='Excluir mayúsculas')
    generate_parser.add_argument('--no-numbers', action='store_true', help='Excluir números')
    generate_parser.add_argument('--symbols', action='store_false', help='Incluir símbolos')
    args = parser.parse_args()

    if args.command == 'generate':
        password = generate_password(
            length=args.length,
            include_uppercase=not args.no_upper,
            include_numbers=not args.no_numbers,
            include_special_chars=not args.symbols
        )
        print(f"\nContraseña generada:\n{password}")

    elif args.command is None:
        parser.print_help()
