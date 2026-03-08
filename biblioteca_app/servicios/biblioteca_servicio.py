from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Clase que maneja la lógica de la biblioteca.
    Aquí se gestionan libros, usuarios y préstamos.
    """

    def __init__(self):

        # Diccionario para almacenar libros disponibles
        # clave = ISBN, valor = objeto Libro
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Conjunto para controlar IDs únicos
        self.ids_usuarios = set()

    # ---------------- LIBROS ----------------

    def agregar_libro(self, titulo, autor, categoria, isbn):
        if isbn in self.libros:
            print("El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro
        print("Libro agregado correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ---------------- USUARIOS ----------------

    def registrar_usuario(self, nombre, user_id):

        if user_id in self.ids_usuarios:
            print("El ID ya existe.")
            return

        usuario = Usuario(nombre, user_id)

        self.usuarios[user_id] = usuario
        self.ids_usuarios.add(user_id)

        print("Usuario registrado correctamente.")

    def eliminar_usuario(self, user_id):

        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ---------------- PRESTAMOS ----------------

    def prestar_libro(self, user_id, isbn):

        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        libro = self.libros.pop(isbn)

        usuario = self.usuarios[user_id]
        usuario.prestar_libro(libro)

        print("Libro prestado correctamente.")

    def devolver_libro(self, user_id, isbn):

        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[user_id]

        libro = usuario.devolver_libro(isbn)

        if libro:
            self.libros[isbn] = libro
            print("Libro devuelto correctamente.")
        else:
            print("El usuario no tenía ese libro.")

    # ---------------- BUSQUEDAS ----------------

    def buscar_por_titulo(self, titulo):

        encontrado = False

        for libro in self.libros.values():
            if (libro.obtener_titulo().lower() == titulo.lower()):
                print(libro)
                encontrado = True

        if not encontrado:
            print("❌ No se encontró ningún libro con ese título.")

    def buscar_por_autor(self, autor):

        encontrado = False

        for libro in self.libros.values():
            if libro.obtener_autor().lower() == autor.lower():
                print(libro)
                encontrado = True

        if not encontrado:
            print("❌ No se encontraron libros de ese autor.")

    def buscar_por_categoria(self, categoria):

        encontrado = False

        for libro in self.libros.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro)
                encontrado = True

        if not encontrado:
            print("❌ No se encontraron libros en esa categoría.")

    # ---------------- LISTADOS ----------------

    def listar_libros_usuario(self, user_id):

        if user_id not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[user_id]

        libros = usuario.listar_libros()

        if not libros:
            print("El usuario no tiene libros prestados.")
            return

        for libro in libros:
            print(libro)