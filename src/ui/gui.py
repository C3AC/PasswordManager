import customtkinter as ctk
from tkinter import messagebox
from src.storage.password_manager import save_password, buscar_password, eliminar_password, get_all_passwords
from src.core.password_generator import generate_password

class PasswordManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Gestor y Generador de Contraseñas")
        self.resizable(False, False)
        self.center_window()

        # Configuración de la apariencia
        ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
        ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"
        ctk.set_widget_scaling(1.0)  # Escala de widgets

        # Crear pestañas
        self.tabview = ctk.CTkTabview(self, width=1024, height=768)
        self.tabview.pack(expand=True, fill="both")

        # Pestaña: Gestor de Contraseñas
        self.password_manager_tab = self.tabview.add("Gestor de Contraseñas")
        self.create_password_manager_tab()

        # Pestaña: Generador de Contraseñas
        self.password_generator_tab = self.tabview.add("Generador de Contraseñas")
        self.create_password_generator_tab()

    def center_window(self):
        """
        Centra la ventana en la pantalla.
        """
        width = 1024
        height = 768
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_password_manager_tab(self):
        """
        Crea la interfaz para el gestor de contraseñas.
        """
        # Etiqueta y entrada para el nombre
        self.name_label = ctk.CTkLabel(self.password_manager_tab, text="Nombre:")
        self.name_label.pack(pady=(20, 5))
        self.name_entry = ctk.CTkEntry(self.password_manager_tab, placeholder_text="Ejemplo: Gmail")
        self.name_entry.pack(pady=5)

        # Etiqueta y entrada para el usuario
        self.user_label = ctk.CTkLabel(self.password_manager_tab, text="Usuario:")
        self.user_label.pack(pady=(20, 5))
        self.user_entry = ctk.CTkEntry(self.password_manager_tab, placeholder_text="Ejemplo: usuario@gmail.com")
        self.user_entry.pack(pady=5)

        # Etiqueta y entrada para la contraseña
        self.password_label = ctk.CTkLabel(self.password_manager_tab, text="Contraseña:")
        self.password_label.pack(pady=(20, 5))
        self.password_entry = ctk.CTkEntry(self.password_manager_tab, placeholder_text="Contraseña", show="*")
        self.password_entry.pack(pady=5)

        # Botón para guardar contraseña
        self.save_button = ctk.CTkButton(self.password_manager_tab, text="Guardar Contraseña", command=self.save_password)
        self.save_button.pack(pady=20)

        # Botón para buscar contraseña
        self.search_button = ctk.CTkButton(self.password_manager_tab, text="Buscar Contraseña", command=self.search_password)
        self.search_button.pack(pady=10)

        # Botón para eliminar contraseña
        self.delete_button = ctk.CTkButton(self.password_manager_tab, text="Eliminar Contraseña", command=self.delete_password)
        self.delete_button.pack(pady=10)

        # Botón para mostrar nombres de contraseñas
        self.show_names_button = ctk.CTkButton(self.password_manager_tab, text="Mostrar Nombres Guardados", command=self.show_saved_names)
        self.show_names_button.pack(pady=10)

        # Área para mostrar los nombres de las contraseñas
        self.names_listbox = ctk.CTkTextbox(self.password_manager_tab, width=500, height=150)
        self.names_listbox.pack(pady=10)

    def show_saved_names(self):
        """
        Muestra los nombres de las contraseñas guardadas.
        """
        self.names_listbox.delete("1.0", "end")  # Limpia el área de texto
        try:
            passwords = get_all_passwords()  # Obtiene todas las contraseñas
            if passwords:
                for password in passwords:
                    self.names_listbox.insert("end", f"{password[0]}\n")  # Muestra solo los nombres
            else:
                self.names_listbox.insert("end", "No hay contraseñas guardadas.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los nombres: {str(e)}")

    def create_password_generator_tab(self):
        """
        Crea la interfaz para el generador de contraseñas.
        """
        # Etiqueta de longitud
        self.length_label = ctk.CTkLabel(self.password_generator_tab, text="Longitud de la contraseña:")
        self.length_label.pack(pady=(20, 5))
        self.length_entry = ctk.CTkEntry(self.password_generator_tab, placeholder_text="12")
        self.length_entry.pack(pady=5)

        # Opciones booleanas
        self.uppercase_var = ctk.BooleanVar(value=True)
        self.uppercase_checkbox = ctk.CTkCheckBox(self.password_generator_tab, text="Incluir mayúsculas", variable=self.uppercase_var)
        self.uppercase_checkbox.pack(pady=5)

        self.numbers_var = ctk.BooleanVar(value=True)
        self.numbers_checkbox = ctk.CTkCheckBox(self.password_generator_tab, text="Incluir números", variable=self.numbers_var)
        self.numbers_checkbox.pack(pady=5)

        self.special_chars_var = ctk.BooleanVar(value=False)
        self.special_chars_checkbox = ctk.CTkCheckBox(self.password_generator_tab, text="Incluir caracteres especiales", variable=self.special_chars_var)
        self.special_chars_checkbox.pack(pady=5)

        # Botón para generar contraseña
        self.generate_button = ctk.CTkButton(self.password_generator_tab, text="Generar Contraseña", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Resultado
        self.result_label = ctk.CTkLabel(self.password_generator_tab, text="Contraseña generada:")
        self.result_label.pack(pady=(20, 5))

        self.result_output = ctk.CTkLabel(self.password_generator_tab, text="", wraplength=500)
        self.result_output.pack(pady=5)

    def save_password(self):
        """
        Lógica para guardar una contraseña.
        """
        nombre = self.name_entry.get().strip()
        usuario = self.user_entry.get().strip()
        contrasena = self.password_entry.get().strip()

        if not nombre or not usuario or not contrasena:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            save_password(nombre, usuario, contrasena)
            messagebox.showinfo("Éxito", f"Contraseña para '{nombre}' guardada exitosamente.")
            self.clear_entries()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def search_password(self):
        """
        Lógica para buscar una contraseña.
        """
        nombre = self.name_entry.get().strip()

        if not nombre:
            messagebox.showerror("Error", "El campo 'Nombre' es obligatorio para buscar.")
            return

        resultados = buscar_password(nombre)
        if resultados:
            usuario, contrasena = resultados[0][1], resultados[0][2]
            messagebox.showinfo("Resultado", f"Usuario: {usuario}\nContraseña: {contrasena}")
        else:
            messagebox.showwarning("No encontrado", f"No se encontró ninguna contraseña con el nombre '{nombre}'.")

    def delete_password(self):
        """
        Lógica para eliminar una contraseña.
        """
        nombre = self.name_entry.get().strip()

        if not nombre:
            messagebox.showerror("Error", "El campo 'Nombre' es obligatorio para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar la contraseña para '{nombre}'?")
        if confirm:
            try:
                eliminar_password(nombre)
                messagebox.showinfo("Éxito", f"Contraseña para '{nombre}' eliminada exitosamente.")
                self.clear_entries()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def generate_password(self):
        """
        Lógica para generar una contraseña.
        """
        try:
            length = int(self.length_entry.get())
            include_uppercase = self.uppercase_var.get()
            include_numbers = self.numbers_var.get()
            include_special_chars = self.special_chars_var.get()

            password = generate_password(
                length=length,
                include_uppercase=include_uppercase,
                include_numbers=include_numbers,
                include_special_chars=include_special_chars
            )

            self.result_output.configure(text=password)
        except ValueError:
            self.result_output.configure(text="Por favor, ingresa un número válido.")

    def clear_entries(self):
        """
        Limpia los campos de entrada.
        """
        self.name_entry.delete(0, "end")
        self.user_entry.delete(0, "end")
        self.password_entry.delete(0, "end")

def run_gui():
    app = PasswordManagerApp()
    app.mainloop()