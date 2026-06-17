# ==========================================================
# CLASE: Cliente
# ----------------------------------------------------------
# Esta clase representa a un cliente dentro de un sistema
# de gestión de restaurante.
#
# Cada objeto creado a partir de esta clase almacenará la
# información básica de una persona que realiza pedidos
# en el restaurante.
#
# Atributos:
# - nombre    : Nombre completo del cliente.
# - telefono  : Número de teléfono del cliente.
# - email     : Correo electrónico del cliente.
#
# Ejemplo de creación:
#
# cliente1 = Cliente(
#     "Carlos López",
#     "0987654321",
#     "carlos@email.com"
# )
# ==========================================================

class Cliente:

    def __init__(self, nombre, telefono, email):
        """
        Constructor de la clase Cliente.

        Este método se ejecuta automáticamente cuando se crea
        un nuevo objeto Cliente.

        Parámetros:
            nombre (str): Nombre completo del cliente.
            telefono (str): Número de teléfono del cliente.
            email (str): Correo electrónico del cliente.

        Los datos recibidos se almacenan como atributos de
        instancia para que cada objeto tenga su propia
        información.
        """

        # Almacena el nombre del cliente.
        self.nombre = nombre

        # Almacena el teléfono del cliente.
        self.telefono = telefono

        # Almacena el correo electrónico del cliente.
        self.email = email

    def mostrar_informacion(self):
        """
        Devuelve una cadena de texto con la información
        principal del cliente.

        Retorna:
            str: Nombre, teléfono y correo electrónico.

        Ejemplo de salida:
            Carlos López - Tel: 0987654321 - Email: carlos@email.com
        """
        return f"{self.nombre} - Tel: {self.telefono} - Email: {self.email}"

    def __str__(self):
        """
        Método especial utilizado por Python para definir
        cómo se mostrará el objeto cuando se imprima con
        la función print().

        Retorna:
            str: Nombre del cliente.

        Ejemplo:
            print(cliente1)

        Salida:
            Carlos López
        """
        return self.nombre