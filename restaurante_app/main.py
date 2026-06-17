# ==========================================================
# ARCHIVO PRINCIPAL (main.py)
# ----------------------------------------------------------
# Este archivo representa el punto de inicio del programa.
#
# Su función es:
# 1. Importar las clases necesarias.
# 2. Crear objetos Producto y Cliente.
# 3. Crear una instancia de Restaurante.
# 4. Registrar los productos y clientes.
# 5. Mostrar la información almacenada.
#
# Este ejemplo permite observar cómo interactúan varias
# clases dentro de un programa orientado a objetos.
# ==========================================================


# ----------------------------------------------------------
# IMPORTACIÓN DE CLASES
# ----------------------------------------------------------
# Se importan las clases definidas en otros módulos del
# proyecto para poder utilizarlas en este archivo.
# ----------------------------------------------------------

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# ==========================================================
# CREACIÓN DE OBJETOS PRODUCTO
# ==========================================================
# A partir de la clase Producto se crean tres objetos diferentes.
#
# Aunque los tres pertenecen a la misma clase, cada objeto posee
# sus propios valores para nombre, precio y categoría.
# ==========================================================

producto1 = Producto(
    "Hamburguesa", 
    8.50, 
    "Comida rápida")

producto2 = Producto(
    "Pizza", 
    12.00, 
    "Italiana")

producto3 = Producto(
    "Ensalada César", 
    6.75, 
    "Saludable")


# ==========================================================
# CREACIÓN DE OBJETOS CLIENTE
# ==========================================================
# Se crean objetos de la clase Cliente con información
# específica de personas registradas en el restaurante.
# ==========================================================

cliente1 = Cliente(
    "Carlos López", 
    "0987654321", 
    "carlos@email.com")

cliente2 = Cliente(
    "María García", 
    "0998765432", 
    "maria@email.com")


# ==========================================================
# CREACIÓN DEL RESTAURANTE
# ==========================================================
# Se instancia un objeto Restaurante.
#
# Este objeto actuará como administrador central de los
# productos y clientes registrados en el sistema.
# ==========================================================

restaurante = Restaurante()


# ==========================================================
# REGISTRO DE PRODUCTOS
# ==========================================================
# Los productos creados previamente son agregados a la
# colección interna del restaurante.
# ==========================================================

restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)


# ==========================================================
# REGISTRO DE CLIENTES
# ==========================================================
# Se registran los clientes dentro del restaurante utilizando
# el método correspondiente.
# ==========================================================

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)


# ==========================================================
# VISUALIZACIÓN DE INFORMACIÓN
# ==========================================================
# Finalmente se muestran en pantalla todos los productos y
# clientes almacenados en el restaurante.
#
# Los métodos mostrar_productos() y mostrar_clientes()
# recorren las listas internas e imprimen cada objeto.
#
# Cuando se imprime un objeto (print(producto)), Python
# ejecuta automáticamente el método __str__() definido
# en la clase correspondiente.
# ==========================================================

print("=== PRODUCTOS DEL RESTAURANTE ===")
restaurante.mostrar_productos()

print("\n=== CLIENTES REGISTRADOS ===")
restaurante.mostrar_clientes()