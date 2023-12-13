class InformacionClimatica:
    def __init__(self):
        self.__temperaturas_diarias = []  # Lista para almacenar las temperaturas diarias

    def ingresar_temperatura(self, temperatura):
        self.__temperaturas_diarias.append(temperatura)

    def promedio_semanal(self):
        if len(self.__temperaturas_diarias) < 7:
            return "No hay suficientes datos para calcular el promedio semanal"
        else:
            return sum(self.__temperaturas_diarias[-7:]) / 7


# Ejemplo de uso:
clima_semanal = InformacionClimatica()

# Ingresar temperaturas diarias
clima_semanal.ingresar_temperatura(25)
clima_semanal.ingresar_temperatura(24)
clima_semanal.ingresar_temperatura(26)
clima_semanal.ingresar_temperatura(23)
clima_semanal.ingresar_temperatura(27)
clima_semanal.ingresar_temperatura(22)
clima_semanal.ingresar_temperatura(26)

# Calcular y mostrar el promedio semanal
promedio = clima_semanal.promedio_semanal()
if isinstance(promedio, str):
    print(promedio)
else:
    print(f"El promedio semanal de temperaturas es: {promedio}")
