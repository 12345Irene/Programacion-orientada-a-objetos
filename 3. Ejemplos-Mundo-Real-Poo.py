class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def devolver(self):
        self.disponible = True


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        else:
            return False

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            return True
        else:
            return False


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def prestar_libro(self, usuario, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                return usuario.tomar_prestado(libro)
        return False

    def devolver_libro(self, usuario, titulo):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                usuario.devolver_libro(libro)
                return True
        return False


# Ejemplo de uso del sistema

# Crear algunos libros
libro1 = Libro("El principito", "Antoine de Saint-Exupéry")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro3 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling")

# Crear usuarios
usuario1 = Usuario("Juan")
usuario2 = Usuario("María")

# Crear una biblioteca
biblioteca = Biblioteca()

# Agregar libros al catálogo de la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Juan toma prestado "El principito"
biblioteca.prestar_libro(usuario1, "El principito")

# Intentar que María tome prestado "El principito" (ya prestado por Juan)
biblioteca.prestar_libro(usuario2, "El principito")

# Juan devuelve "El principito"
biblioteca.devolver_libro(usuario1, "El principito")

# María toma prestado "El principito" (ahora está disponible)
biblioteca.prestar_libro(usuario2, "El principito")

# Mostrar los libros prestados por cada usuario
print(f"{usuario1.nombre} tiene prestados: {[libro.titulo for libro in usuario1.libros_prestados]}")
print(f"{usuario2.nombre} tiene prestados: {[libro.titulo for libro in usuario2.libros_prestados]}")

