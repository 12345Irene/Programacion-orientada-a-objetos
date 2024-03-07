import tkinter as tk

class AplicacionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Creación de una Aplicación GUI Básica")

        # Etiqueta y campo de texto para ingresar información
        self.label = tk.Label(master, text="Ingrese información:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        # Botón para agregar la información ingresada
        self.agregar_button = tk.Button(master, text="Agregar", command=self.agregar_info)
        self.agregar_button.pack()

        # Lista para mostrar la información agregada
        self.lista = tk.Listbox(master)
        self.lista.pack()

        # Botón para limpiar la lista
        self.limpiar_button = tk.Button(master, text="Limpiar", command=self.limpiar_lista)
        self.limpiar_button.pack()

    def agregar_info(self):
        info = self.entry.get()
        if info:
            self.lista.insert(tk.END, info)
            self.entry.delete(0, tk.END)

    def limpiar_lista(self):
        self.lista.delete(0, tk.END)

root = tk.Tk()
app = AplicacionGUI(root)
root.mainloop()
