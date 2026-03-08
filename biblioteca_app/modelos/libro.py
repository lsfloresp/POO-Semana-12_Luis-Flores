class Libro:
    """
    Clase que representa un libro dentro de la biblioteca.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa una tupla porque el enunciado pide que título y autor sean inmutables
        self.info = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        return f"{self.info[0]} - {self.info[1]} | Categoria: {self.categoria} | ISBN: {self.isbn}"