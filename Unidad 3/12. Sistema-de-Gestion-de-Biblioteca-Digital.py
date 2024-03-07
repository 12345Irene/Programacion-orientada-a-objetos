class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Utilizamos una tupla para almacenar título y autor
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista para gestionar los libros prestados al usuario

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para almacenar los libros por ISBN
        self.usuarios_registrados = set()  # Conjunto para almacenar IDs de usuarios únicos

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
        else:
            print("El libro con ISBN {} no está disponible en la biblioteca.".format(isbn))

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.user_id)
            print("Usuario {} registrado correctamente.".format(usuario.nombre))
        else:
            print("El usuario con ID {} ya está registrado.".format(usuario.user_id))

    def dar_baja_usuario(self, usuario):
        if usuario.user_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario.user_id)
            print("Usuario {} dado de baja correctamente.".format(usuario.nombre))
        else:
            print("El usuario con ID {} no está registrado.".format(usuario.user_id))

    def prestar_libro(self, libro, usuario):
        if libro.isbn in self.libros_disponibles:
            self.libros_disponibles.pop(libro.isbn)
            usuario.libros_prestados.append(libro)
            print("Libro '{}' prestado a {}.".format(libro.titulo_autor[0], usuario.nombre))
        else:
            print("El libro '{}' no está disponible para préstamo.".format(libro.titulo_autor[0]))

    def devolver_libro(self, libro, usuario):
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            self.libros_disponibles[libro.isbn] = libro
            print("Libro '{}' devuelto por {}.".format(libro.titulo_autor[0], usuario.nombre))
        else:
            print("El usuario {} no tiene prestado el libro '{}'.".format(usuario.nombre, libro.titulo_autor[0]))

    def buscar_libro(self, criterio, valor):
        libros_encontrados = []
        for isbn, libro in self.libros_disponibles.items():
            if criterio == 'titulo':
                if valor.lower() in libro.titulo_autor[0].lower():
                    libros_encontrados.append(libro)
            elif criterio == 'autor':
                if valor.lower() in libro.titulo_autor[1].lower():
                    libros_encontrados.append(libro)
            elif criterio == 'categoria':
                if valor.lower() == libro.categoria.lower():
                    libros_encontrados.append(libro)
        return libros_encontrados

    def listar_libros_prestados(self, usuario):
        print("Libros prestados a {}: ".format(usuario.nombre))
        for libro in usuario.libros_prestados:
            print("- {}".format(libro.titulo_autor[0]))


# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "978-8445072577")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "978-0307356547")
    libro3 = Libro("1984", "George Orwell", "Ciencia ficción", "978-9877490598")

    # Crear algunos usuarios
    usuario1 = Usuario("Juan", 1)
    usuario2 = Usuario("María", 2)

    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar usuarios en la biblioteca
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro(libro1, usuario1)
    biblioteca.prestar_libro(libro2, usuario1)
    biblioteca.prestar_libro(libro3, usuario2)

    # Listar libros prestados a un usuario
    biblioteca.listar_libros_prestados(usuario1)

    # Devolver un libro
    biblioteca.devolver_libro(libro1, usuario1)

    # Buscar libros por autor
    libros_encontrados = biblioteca.buscar_libro('autor', 'tolkien')
    print("\nLibros de Tolkien encontrados:")
    for libro in libros_encontrados:
        print("- {} ({})".format(libro.titulo_autor[0], libro.categoria))
