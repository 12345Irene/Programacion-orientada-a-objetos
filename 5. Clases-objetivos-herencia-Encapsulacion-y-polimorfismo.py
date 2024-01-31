class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca  # Encapsulación usando el prefijo _
        self._modelo = modelo

    def obtener_informacion(self):
        return f"Vehículo: {self._marca} {self._modelo}"

    def conducir(self):
        return "El vehículo está en movimiento"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self._color = color

    def obtener_informacion(self):  # Polimorfismo: Sobrescritura del método obtener_informacion
        return f"Automóvil: {self._marca} {self._modelo}, Color: {self._color}"

    def conducir(self, velocidad):  # Polimorfismo: Método con argumentos diferentes
        return f"El automóvil de color {self._color} está conduciendo a {velocidad} km/h"


# Crear instancias de las clases
vehiculo_generico = Vehiculo("Toyota", "Corolla")
automovil_rojo = Automovil("Ford", "Mustang", "Rojo")

# Demostrar funcionalidad
print(vehiculo_generico.obtener_informacion())
print(vehiculo_generico.conducir())

print(automovil_rojo.obtener_informacion())
print(automovil_rojo.conducir(120))