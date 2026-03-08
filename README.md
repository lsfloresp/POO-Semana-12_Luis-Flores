# Sistema de Gestión de Biblioteca Digital

Este proyecto consiste en el desarrollo de un sistema de gestión de biblioteca digital utilizando **Python** y **Programación Orientada a Objetos (POO)**.
El sistema permite administrar libros, usuarios y préstamos mediante una arquitectura organizada por capas, separando los **modelos**, los **servicios** y el **punto de entrada del programa**.

El objetivo del programa es simular el funcionamiento básico de una biblioteca, permitiendo registrar usuarios, agregar libros al catálogo, realizar préstamos y devoluciones, además de buscar libros dentro del sistema.

---

# Arquitectura del Proyecto

El proyecto está organizado siguiendo una estructura por capas para separar las responsabilidades del sistema.

```
biblioteca_app/
│
├── modelos/
│   ├── libro.py
│   └── usuario.py
│
├── servicios/
│   └── biblioteca_servicio.py
│
└── main.py
```

### modelos

Contiene las clases que representan las entidades principales del sistema.

* **Libro:** representa un libro dentro del catálogo de la biblioteca.
* **Usuario:** representa a un usuario registrado que puede solicitar libros prestados.

### servicios

Contiene la lógica del sistema.

* **BibliotecaServicio:** se encarga de gestionar los libros disponibles, los usuarios registrados y las operaciones de préstamo y devolución.

### main.py

Es el punto de entrada del programa.
Aquí se ejecuta el sistema mediante un **menú interactivo en consola** que permite al usuario utilizar todas las funciones de la biblioteca.

---

# Uso de Colecciones en Python

Para cumplir con los requisitos del ejercicio se utilizaron diferentes estructuras de datos de Python:

* **Tupla:** utilizada para almacenar el título y autor del libro (datos que no cambian).
* **Lista:** utilizada para almacenar los libros prestados a cada usuario.
* **Diccionario:** utilizado para guardar los libros disponibles usando el ISBN como clave.
* **Conjunto (set):** utilizado para garantizar que los IDs de los usuarios sean únicos.

---

# Funcionalidades del Sistema

El sistema permite realizar las siguientes operaciones:

* Añadir libros al catálogo
* Quitar libros
* Registrar usuarios
* Eliminar usuarios
* Prestar libros a usuarios
* Devolver libros
* Buscar libros por:

  * Título
  * Autor
  * Categoría
* Listar los libros prestados a un usuario

---

# Ejecución del Programa

Para ejecutar el sistema se debe correr el archivo **main.py**.

```
python main.py
```

Una vez iniciado el programa, aparecerá un menú interactivo en la consola donde el usuario podrá seleccionar las diferentes opciones para gestionar la biblioteca.

---

# Objetivo Académico

Este proyecto fue desarrollado como parte de una actividad académica con el objetivo de aplicar:

* Programación Orientada a Objetos
* Arquitectura por capas
* Uso de colecciones en Python
* Separación entre modelos, servicios y punto de entrada
* Organización de proyectos en Python

---

# Autor

**Luis Santiago Flores Piña**
Estudiante de segundo semestre - UEA
