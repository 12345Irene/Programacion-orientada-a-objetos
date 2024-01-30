import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        #Archivo Semana 1
        '1': 'Semana1 - Programacion Orientada a Objetos',
        #Archivo Semana 2
        '2': 'Semana2 - Ejemplos-de-tecnicas-de-programacion.py ',
        # Archivo Semana 3
        '3': 'Semana3 - Programacion-Orientada.py',
        '3.1': 'Semana3 - Programacion-Tradicional.py',
        '3.2': 'Semana3 - Programacion-Orientada-a-Objetos(Poo).py',
        # Archivo Semana 4
        '4': 'Semana4 - Ejemplos-Mundo-Real-Poo.py',
        # Archivo Semana 5
        '5': 'Semana5 - Tipos-de-datos-Identificadores.py',
        # Archivo Semana 6
        '6': 'Semana6 - Clases-objetivos-herencia-Encapsulacion-y-polimorfismo.py',
        # Archivo Semana 7
        '7': 'Semana7 - Constructores-Destructores.py',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
