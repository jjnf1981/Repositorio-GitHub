# ==========================================================
# CLASE: Restaurante
# ----------------------------------------------------------
# Esta clase representa un restaurante encargado de
# administrar colecciones de productos y clientes.
#
# Su función principal es almacenar, organizar y mostrar
# la información de los productos y clientes registrados.
#
# El restaurante utiliza listas para guardar múltiples
# objetos creados a partir de las clases Producto y Cliente.
#
# Atributos:
# - productos : Lista que almacena los objetos Producto.
# - clientes  : Lista que almacena los objetos Cliente.
#
# Ejemplo de creación:
#
# restaurante = Restaurante()
# ==========================================================

class Restaurante:

    def __init__(self):
        """
        Constructor de la clase Restaurante.

        Este método se ejecuta automáticamente al crear un
        nuevo objeto Restaurante.

        Inicializa dos listas vacías que permitirán almacenar
        productos y clientes durante la ejecución del programa.
        """

        # Lista donde se almacenarán los objetos Producto.
        self.productos = []

        # Lista donde se almacenarán los objetos Cliente.
        self.clientes = []

    def agregar_producto(self, producto):
        """
        Agrega un producto a la colección del restaurante.

        Parámetros:
            producto (Producto): Objeto de tipo Producto que será
                                 almacenado en el restaurante.

        Funcionamiento:
            Utiliza el método append() para insertar el
            objeto al final de la lista de productos.
        """

        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el restaurante.

        Parámetros:
            cliente (Cliente): Objeto de tipo Cliente que
                               será agregado al sistema.

        Funcionamiento:
            Utiliza el método append() para almacenar el
            cliente en la lista correspondiente.
        """

        self.clientes.append(cliente)

    def mostrar_productos(self):
        """
        Muestra todos los productos registrados en el restaurante.

        Funcionamiento:
            Recorre la lista de productos utilizando un ciclo
            for y muestra cada objeto mediante print().

        Nota:
            Cuando se imprime un objeto Producto, Python ejecuta
            automáticamente el método especial __str__()
            definido en dicha clase.
        """

        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        """
        Muestra todos los clientes registrados en el restaurante.

        Funcionamiento:
            Recorre la lista de clientes utilizando un ciclo
            for y muestra cada objeto mediante print().

        Nota:
            Cuando se imprime un objeto Cliente, Python ejecuta
            automáticamente el método especial __str__()
            definido en dicha clase.
        """

        for cliente in self.clientes:
            print(cliente)