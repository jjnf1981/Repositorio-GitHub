# ==========================================================
# ARCHIVO PRINCIPAL (main.py)
# ==========================================================

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    # Crear productos
    producto1 = Producto(
        "Hamburguesa", 
        8.50, 
        "Comida rápida",
        10,
        True
    )

    producto2 = Producto(
        "Pizza", 
        12.00, 
        "Italiana",
        0,
        False
    )

    producto3 = Producto(
        "Ensalada César", 
        6.75, 
        "Saludable",
        20,
        True
    )

    # Crear clientes
    cliente1 = Cliente(
        "Carlos López", 
        "0987654321", 
        "carlos@email.com")

    cliente2 = Cliente(
        "María García", 
        "0998765432", 
        "maria@email.com")

    # Crear restaurante
    restaurante = Restaurante()

    # Agregar productos y clientes
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)

    # Mostrar información
    print("=== PRODUCTOS DEL RESTAURANTE ===")
    restaurante.mostrar_productos()

    print("\n=== CLIENTES REGISTRADOS ===")
    restaurante.mostrar_clientes()

# Punto de inicio del programa
if __name__ == "__main__":
    main()