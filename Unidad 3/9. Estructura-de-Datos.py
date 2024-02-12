class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not self.buscar_producto_por_id(producto.id):
            self.productos.append(producto)
            print("Producto agregado exitosamente.")
        else:
            print("Ya existe un producto con ese ID.")

    def eliminar_producto_por_id(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("No se encontró ningún producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_producto_por_id(id)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado exitosamente.")
        else:
            print("No se encontró ningún producto con ese ID.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                resultados.append(producto)
        return resultados

    def buscar_producto_por_id(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return None

    def mostrar_productos(self):
        if self.productos:
            print("Lista de Productos:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos en el inventario")
    print("6. Salir")


if __name__ == "__main__":
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = input("Ingrese el ID del producto que desea eliminar: ")
            inventario.eliminar_producto_por_id(id)
        elif opcion == "3":
            id = input("Ingrese el ID del producto que desea actualizar: ")
            cantidad = input("Ingrese la nueva cantidad del producto (deje en blanco para no actualizar): ")
            precio = input("Ingrese el nuevo precio del producto (deje en blanco para no actualizar): ")
            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre (o parte del nombre) del producto que desea buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                print("Resultados de la búsqueda:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
