class Usuario:
    """
    Representa un usuario registrado en la biblioteca.
    """

    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id

        # Lista para almacenar los libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros(self):
        return self.libros_prestados