# PasswordManager

**PasswordManager** es una aplicación que permite gestionar y generar contraseñas de forma segura. Incluye una interfaz gráfica (GUI) y una interfaz de línea de comandos (CLI) para adaptarse a las necesidades del usuario.

## Características

- **Gestor de Contraseñas**:
  - Guardar contraseñas con un nombre y usuario asociado.
  - Buscar contraseñas por nombre.
  - Eliminar contraseñas de forma segura.
  - Mostrar una lista de los nombres de las contraseñas guardadas.

- **Generador de Contraseñas**:
  - Generar contraseñas seguras con opciones personalizables:
    - Longitud de la contraseña.
    - Inclusión de mayúsculas, números y caracteres especiales.

- **Seguridad**:
  - Las contraseñas se almacenan en un archivo encriptado utilizando la biblioteca `cryptography`.

## Requisitos

- **Python 3.10 o superior**
- Bibliotecas necesarias (ver `requirements.txt`):
  - `cryptography`
  - `pyperclip`
  - `dearpygui`
  - `passlib`
  - `python-dotenv`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/PasswordManager.git
   cd PasswordManager