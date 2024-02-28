import json

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.inventario = self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo.")
            return {}
        except PermissionError:
            print(f"No se tienen permisos para leer el archivo {self.archivo}.")
            return {}

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(self.inventario, file, indent=4)
                print(f"Inventario guardado en {self.archivo} exitosamente.")
        except PermissionError:
            print(f"No se tienen permisos para escribir en el archivo {self.archivo}.")

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] += cantidad
        else:
            self.inventario[nombre] = cantidad
        self.guardar_inventario()

    def eliminar_producto(self, nombre):
        if nombre in self.inventario:
            del self.inventario[nombre]
            self.guardar_inventario()
        else:
            print(f"El producto {nombre} no existe en el inventario.")

    def actualizar_producto(self, nombre, nueva_cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] = nueva_cantidad
            self.guardar_inventario()
        else:
            print(f"El producto {nombre} no existe en el inventario.")

    def mostrar_inventario(self):
        print("Inventario:")
        for producto, cantidad in self.inventario.items():
            print(f"{producto}: {cantidad}")


def main():
    inventario = Inventario()

    while True:
        print("\n1. Agregar producto\n2. Eliminar producto\n3. Actualizar cantidad\n4. Mostrar inventario\n5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            inventario.agregar_producto(nombre, cantidad)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_producto(nombre, nueva_cantidad)
        elif opcion == '4':
            inventario.mostrar_inventario()
        elif opcion == '5':
            inventario.guardar_inventario()
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
    # Creación de una tupla
    mi_tupla = (1, "dos", 3.0)

    # Acceso a un elemento
    print(mi_tupla[1])  # Imprime "dos"

    # Desempaquetado de una tupla
    a, b, c = mi_tupla
    print(a, b, c)  # Imprime 1 dos 3.0

    # Concatenación de tuplas
    nueva_tupla = mi_tupla + (4, 5)
    print(nueva_tupla)  # Imprime (1, 'dos', 3.0, 4, 5)
