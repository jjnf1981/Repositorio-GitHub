# 🍽️ Sistema de Gestión de Restaurante - Semana 5

**Estudiante:** Joe Jairo Nieto Flores

## 📖 Descripción del sistema

Este proyecto es un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). Permite registrar productos (platos, bebidas) y clientes, y administrarlos mediante una clase central llamada `Restaurante`.

## 🏗️ Estructura del proyecto

restaurante_app/
├── modelos/
│ ├── init.py
│ ├── producto.py
│ └── cliente.py
├── servicios/
│ ├── init.py
│ └── restaurante.py
├── main.py
└── README.md

## 🧩 Tipos de datos utilizados

| Clase | Atributo | Tipo de dato |
|-------|----------|--------------|
| Producto | nombre | `str` |
| Producto | precio | `float` |
| Producto | categoria | `str` |
| Producto | stock | `int` |
| Producto | disponible | `bool` |
| Cliente | nombre | `str` |
| Cliente | telefono | `str` |
| Cliente | email | `str` |
| Restaurante | productos | `list` |
| Restaurante | clientes | `list` |

## 🤔 Reflexión personal

Usar identificadores descriptivos como `nombre`, `precio`, `stock` o `disponible` hace que el código sea más fácil de leer y entender. Los tipos de datos adecuados (`str` para texto, `float` para precios, `int` para cantidades, `bool` para estados y `list` para colecciones) ayudan a evitar errores y dejan claro qué tipo de información maneja cada variable. Las listas permiten almacenar múltiples objetos y recorrerlos fácilmente, lo que simplifica la gestión de productos y clientes en el restaurante.