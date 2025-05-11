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
    fernet = load_or_create_key()
    datos = get_all_passwords()
    datos.append([nombre, usuario, contrasena])
    csv_data = "\n".join([",".join(row) for row in datos]).encode()
    encrypted = fernet.encrypt(csv_data)
    with open(DATA_PATH, "wb") as f:
        f.write(encrypted)

def get_all_passwords():
    if not os.path.exists(DATA_PATH):
        return []
    fernet = load_or_create_key()
    with open(DATA_PATH, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted).decode()
    reader = csv.reader(decrypted.splitlines())
    return list(reader)

def buscar_password(nombre_objetivo):
    contraseñas = get_all_passwords()
    return [fila for fila in contraseñas if fila[0].lower() == nombre_objetivo.lower()]

def eliminar_password(nombre_objetivo):
    contraseñas = get_all_passwords()
    contraseñas_filtradas = [fila for fila in contraseñas if fila[0].lower() != nombre_objetivo.lower()]
    
    if len(contraseñas) == len(contraseñas_filtradas):
        print(f"No se encontró ninguna contraseña con el nombre '{nombre_objetivo}'.")
        return

    # Confirmación del usuario
    confirmacion = input(f"¿Estás seguro de que deseas eliminar la contraseña para '{nombre_objetivo}'? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("Operación cancelada.")
        return

    if contraseñas_filtradas:
        save_password(contraseñas_filtradas[0][0], contraseñas_filtradas[0][1], contraseñas_filtradas[0][2])
    else:
        os.remove(DATA_PATH)
    print(f"La contraseña para '{nombre_objetivo}' ha sido eliminada.")