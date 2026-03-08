from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():
    print("\n 📚 SISTEMA BIBLIOTECA 📚")
    print("1. ➕ Añadir libro")
    print("2. ❌ Quitar libro")
    print("3. 👤 Registrar usuario")
    print("4. 🚫 Eliminar usuario")
    print("5. 📖➡️ Prestar libro")
    print("6. ⬅️📖 Devolver libro")
    print("7. 🔎 Buscar por titulo")
    print("8. 🔎 Buscar por autor")
    print("9. 🏷️ Buscar por categoria")
    print("10. 📚 Ver libros de usuario")
    print("0. 🚪 Salir")


def main():

    biblioteca = BibliotecaServicio()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            while not autor.replace(" ", "").isalpha():
                print("❌ El autor solo debe contener letras.")
                autor = input("Autor: ")
            categoria = input("Categoria: ")
            isbn = input("ISBN: ")
            while not isbn.isdigit():
                print("❌ El ISBN debe contener solo números.")
                isbn = input("ISBN: ")

            biblioteca.agregar_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":
            isbn = input("ISBN del libro: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre: ")
            while not nombre.replace(" ", "").isalpha():
                print("❌ El nombre solo debe contener letras.")
                nombre = input("Nombre: ")
            user_id = input("ID usuario: ")

            biblioteca.registrar_usuario(nombre, user_id)

        elif opcion == "4":
            user_id = input("ID usuario: ")
            biblioteca.eliminar_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            titulo = input("Titulo a buscar: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "8":
            autor = input("Autor a buscar: ")
            biblioteca.buscar_por_autor(autor)

        elif opcion == "9":
            categoria = input("Categoria: ")
            biblioteca.buscar_por_categoria(categoria)

        elif opcion == "10":
            user_id = input("ID usuario: ")
            biblioteca.listar_libros_usuario(user_id)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()