# ==========================================================
# CLASE: Producto
# ----------------------------------------------------------
# Esta clase representa un producto (plato o bebida).
#
# Cada objeto creado a partir de esta clase almacenará la
# información correspondiente a un producto específico.
#
# Atributos:
# - nombre     : Nombre del producto (ej. "Hamburguesa").
# - precio     : Precio del producto en dólares (ej. 8.50).
# - categoria  : Categoría del producto (ej. "Comida rápida").
#
# Ejemplo de creación:
#
# producto1 = Producto(
#     "Hamburguesa",
#     8.50,
#     "Comida rápida"
# )
# ==========================================================

class Producto:

    def __init__(self, nombre, precio, categoria):
        """
        Constructor de la clase Producto.

        Este método se ejecuta automáticamente cuando se crea
        un nuevo objeto Producto.

        Parámetros:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            categoria (str): Categoría del producto.

        Los valores recibidos se almacenan dentro del objeto
        utilizando atributos de instancia.
        """

        # Almacena el nombre del producto.
        self.nombre = nombre

        # Almacena el precio del producto.
        self.precio = precio

        # Almacena la categoría del producto.
        self.categoria = categoria

    def mostrar_informacion(self):
        """
        Devuelve una cadena de texto con la información
        principal del producto.

        Retorna:
            str: Texto con el nombre, categoría y precio.

        Ejemplo de salida:
            Producto: Hamburguesa | Categoría: Comida rápida | Precio: $8.50
        """
        return f"Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"

    def __str__(self):
        """
        Método especial utilizado por Python para definir
        cómo se mostrará el objeto cuando se imprima con
        la función print().

        Retorna:
            str: Representación amigable del producto.

        Ejemplo:
            print(producto1)

        Salida:
            Hamburguesa - $8.50
        """
        return f"{self.nombre} - ${self.precio:.2f}"