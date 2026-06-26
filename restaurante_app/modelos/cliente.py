# ==========================================================
# CLASE: Cliente
# ==========================================================

class Cliente:

    def __init__(self, nombre: str, telefono: str, email: str):
        
        # Almacena el nombre del cliente.
        self.nombre = nombre

        # Almacena el teléfono del cliente.
        self.telefono = telefono

        # Almacena el correo electrónico del cliente.
        self.email = email

    def mostrar_informacion(self) -> str:
        # Retorna una cadena de texto con la información principal del cliente.
        return f"{self.nombre} | Tel: {self.telefono} | Email: {self.email}"

    def __str__(self) -> str:
        # Representación en texto del objeto cliente, útil para imprimirlo directamente.
        return self.nombre