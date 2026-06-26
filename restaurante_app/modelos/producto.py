# ==========================================================
# CLASE: Producto
# ==========================================================

class Producto:

    def __init__(self, nombre: str, precio: float, categoria: str, stock: int, disponible: bool):
        self.nombre = nombre # Almacena el nombre del producto.
        self.precio = precio # Almacena el precio del producto.        
        self.categoria = categoria # Almacena la categoría del producto.
        self.stock = stock  # Almacena la cantidad disponible en stock del producto.
        self.disponible = disponible  # Indica si el producto está disponible para la venta

    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        # Retorna una cadena de texto con la información principal del producto.
        return (
            f"Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"stock: {self.stock} | "
            f"{estado}"
            )

    def __str__(self) -> str:
        # Representación en texto del objeto producto, útil para imprimirlo directamente.
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} | ${self.precio:.2f} | Stock: {self.stock} | {estado}"