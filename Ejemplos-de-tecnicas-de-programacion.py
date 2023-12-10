class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10
        print(f"El {self.marca} {self.modelo} está acelerando. Velocidad: {self.velocidad} km/h")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10
            print(f"El {self.marca} {self.modelo} está frenando. Velocidad: {self.velocidad} km/h")
        else:
            print(f"El {self.marca} {self.modelo} está detenido.")


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Depósito exitoso. Saldo actual: {self.__saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes.")


class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Rectangulo(Figura):
    def __init__(self, color, ancho, altura):
        super().__init__(color)
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura


class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

def calcular_area(figura):
    return figura.area()

# Uso del polimorfismo
rectangulo = Rectangulo("Rojo", 5, 10)
circulo = Circulo("Azul", 7)

print("Área del rectángulo:", calcular_area(rectangulo))  # Área del rectángulo: 50
print("Área del círculo:", calcular_area(circulo))      # Área del círculo: 153.9384
