from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QCheckBox
from src.core.password_generator import generate_password

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Contraseñas")

        # Layout principal
        layout = QVBoxLayout()

        # Entrada de longitud
        self.length_label = QLabel("Longitud de la contraseña:")
        self.length_input = QLineEdit()
        self.length_input.setText("12")
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)

        # Opciones booleanas
        self.include_uppercase = QCheckBox("Incluir mayúsculas")
        self.include_uppercase.setChecked(True)  # Activado por defecto
        layout.addWidget(self.include_uppercase)

        self.include_numbers = QCheckBox("Incluir números")
        self.include_numbers.setChecked(True)  # Activado por defecto
        layout.addWidget(self.include_numbers)

        self.include_special_chars = QCheckBox("Incluir caracteres especiales")
        self.include_special_chars.setChecked(True)  # Activado por defecto
        layout.addWidget(self.include_special_chars)

        # Botón para generar contraseña
        self.generate_button = QPushButton("Generar Contraseña")
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        # Resultado
        self.result_label = QLabel("Contraseña generada:")
        self.result_output = QLabel("")
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)

        # Configurar el widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generate_password(self):
        try:
            length = int(self.length_input.text())
            password = generate_password(
                length=length,
                include_uppercase=self.include_uppercase.isChecked(),
                include_numbers=self.include_numbers.isChecked(),
                include_special_chars=self.include_special_chars.isChecked()
            )
            self.result_output.setText(password)
        except ValueError:
            self.result_output.setText("Por favor, ingresa un número válido.")

def run_gui():
    app = QApplication([])
    window = PasswordGeneratorApp()
    window.show()
    app.exec()
