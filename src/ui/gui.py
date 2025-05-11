import customtkinter as ctk
from src.core.password_generator import generate_password

class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Generador de Contraseñas")
        self.geometry("400x400")
        self.resizable(False, False)

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de longitud
        self.length_label = ctk.CTkLabel(self, text="Longitud de la contraseña:")
        self.length_label.pack(pady=(20, 5))

        # Entrada de longitud
        self.length_entry = ctk.CTkEntry(self, placeholder_text="12")
        self.length_entry.pack(pady=5)

        # Opciones booleanas
        self.uppercase_var = ctk.BooleanVar(value=True)
        self.uppercase_checkbox = ctk.CTkCheckBox(self, text="Incluir mayúsculas", variable=self.uppercase_var)
        self.uppercase_checkbox.pack(pady=5)

        self.numbers_var = ctk.BooleanVar(value=True)
        self.numbers_checkbox = ctk.CTkCheckBox(self, text="Incluir números", variable=self.numbers_var)
        self.numbers_checkbox.pack(pady=5)

        self.special_chars_var = ctk.BooleanVar(value=False)
        self.special_chars_checkbox = ctk.CTkCheckBox(self, text="Incluir caracteres especiales", variable=self.special_chars_var)
        self.special_chars_checkbox.pack(pady=5)

        # Botón para generar contraseña
        self.generate_button = ctk.CTkButton(self, text="Generar Contraseña", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Resultado
        self.result_label = ctk.CTkLabel(self, text="Contraseña generada:")
        self.result_label.pack(pady=(20, 5))

        self.result_output = ctk.CTkLabel(self, text="", wraplength=350)
        self.result_output.pack(pady=5)

    def generate_password(self):
        try:
            # Obtener valores de los inputs
            if self.length_entry.get() == "":
                length = 12
            else:
                length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("La longitud debe ser mayor que 0.")
            # Obtener valores de las opciones
            include_uppercase = self.uppercase_var.get()
            include_numbers = self.numbers_var.get()
            include_special_chars = self.special_chars_var.get()

            # Generar contraseña
            password = generate_password(
                length=length,
                include_uppercase=include_uppercase,
                include_numbers=include_numbers,
                include_special_chars=include_special_chars
            )

            # Mostrar resultado
            self.result_output.configure(text=password)
        except ValueError:
            self.result_output.configure(text="Por favor, ingresa un número válido.")

def run_gui():
    app = PasswordGeneratorApp()
    app.mainloop()