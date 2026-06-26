# ==========================================================
# CLASE: Restaurante 
# ==========================================================

class Restaurante:

    def __init__(self):

        # Lista donde se almacenarán los objetos Producto.
        self.productos = []

        # Lista donde se almacenarán los objetos Cliente.
        self.clientes = []

    def agregar_producto(self, producto) -> None:
        self.productos.append(producto)

    def agregar_cliente(self, cliente) -> None:
        self.clientes.append(cliente)

    def mostrar_productos(self) -> None:
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self) -> None:
        for cliente in self.clientes:
            print(cliente)