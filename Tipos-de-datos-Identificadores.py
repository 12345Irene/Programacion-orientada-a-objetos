# Programa: Calculadora de área de un rectángulo
# Este programa calcula el área de un rectángulo dados su base y altura.

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
    - base (float): La longitud de la base del rectángulo.
    - altura (float): La altura del rectángulo.

    Returns:
    - float: El área del rectángulo calculada como base * altura.
    """
    area = base * altura
    return area

# Ejemplo de uso
base_rectangulo = 5.0
altura_rectangulo = 10.0

# Calcula el área del rectángulo con las medidas dadas
area_resultante = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

# Imprime el resultado
print(f"El área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es: {area_resultante}")
