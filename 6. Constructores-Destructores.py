class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        Se llama automáticamente al crear un nuevo objeto Persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una nueva persona llamada {self.nombre} de {self.edad} años.")

    def __del__(self):
        """
        Destructor de la clase Persona.
        Se llama automáticamente al destruir un objeto Persona.
        """
        print(f"{self.nombre} ha sido eliminado. Objeto destruido.")

# Crear instancias de la clase Persona
persona1 = Persona("Juan", 25)
persona2 = Persona("Maria", 30)

# Acceder a los atributos de las instancias
print(f"{persona1.nombre} tiene {persona1.edad} años.")
print(f"{persona2.nombre} tiene {persona2.edad} años.")

# El objeto persona1 será destruido automáticamente al salir de este bloque
