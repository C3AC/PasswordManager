import os
import csv
from cryptography.fernet import Fernet

KEY_PATH = "clave.key"
DATA_PATH = "contraseñas_encriptado.bin"

def load_or_create_key():
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as f:
            f.write(key)
    else:
        with open(KEY_PATH, "rb") as f:
            key = f.read()
    return Fernet(key)

def save_password(nombre, usuario, contrasena):
    """
    Guarda una nueva contraseña en el almacenamiento encriptado.
    """
    fernet = load_or_create_key()
    datos = get_all_passwords()
    if not buscar_password(nombre):
        datos.append([nombre, usuario, contrasena])
        csv_data = "\n".join([",".join(row) for row in datos]).encode()
        encrypted = fernet.encrypt(csv_data)
        with open(DATA_PATH, "wb") as f:
            f.write(encrypted)
    else:
        raise ValueError(f"Ya existe una contraseña con el nombre '{nombre}'.")

def get_all_passwords():
    """
    Devuelve todas las contraseñas almacenadas como una lista de listas.
    """
    if not os.path.exists(DATA_PATH):
        return []
    fernet = load_or_create_key()
    with open(DATA_PATH, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted).decode()
    reader = csv.reader(decrypted.splitlines())
    return list(reader)

def buscar_password(nombre_objetivo):
    """
    Busca una contraseña por su nombre y devuelve una lista de coincidencias.
    """
    contraseñas = get_all_passwords()
    if not contraseñas:
        raise ValueError("No hay contraseñas almacenadas.")
    else:
        return [fila for fila in contraseñas if fila[0].lower() == nombre_objetivo.lower()]

def eliminar_password(nombre_objetivo):
    """
    Elimina una contraseña por su nombre. Devuelve True si se eliminó correctamente.
    """
    contraseñas = get_all_passwords()
    contraseñas_filtradas = [fila for fila in contraseñas if fila[0].lower() != nombre_objetivo.lower()]
    
    if len(contraseñas) == len(contraseñas_filtradas):
        raise ValueError(f"No se encontró ninguna contraseña con el nombre '{nombre_objetivo}'.")

    if contraseñas_filtradas:
        # Guardar las contraseñas restantes
        csv_data = "\n".join([",".join(row) for row in contraseñas_filtradas]).encode()
        fernet = load_or_create_key()
        encrypted = fernet.encrypt(csv_data)
        with open(DATA_PATH, "wb") as f:
            f.write(encrypted)
    else:
        # Si no quedan contraseñas, eliminar el archivo
        os.remove(DATA_PATH)
    return True