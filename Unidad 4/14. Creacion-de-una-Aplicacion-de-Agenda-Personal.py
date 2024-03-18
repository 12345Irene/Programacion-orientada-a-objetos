import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Variables para almacenar la fecha, hora y descripción del evento
        self.date_var = tk.StringVar()
        self.time_var = tk.StringVar()
        self.description_var = tk.StringVar()

        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        # Frame para la lista de eventos
        self.events_frame = ttk.LabelFrame(self.main_frame, text="Eventos")
        self.events_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.events_frame, columns=("Fecha", "Hora", "Descripción"), selectmode="browse")
        self.tree.heading("#0", text="ID")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.column("#0", width=50)
        self.tree.column("Fecha", width=100)
        self.tree.column("Hora", width=80)
        self.tree.column("Descripción", width=200)
        self.tree.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Scrollbar para la lista de eventos
        scrollbar = ttk.Scrollbar(self.events_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscroll=scrollbar.set)

        # Frame para la entrada de datos
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Agregar Evento")
        self.input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Etiquetas y campos de entrada
        ttk.Label(self.input_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(self.input_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(self.input_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky="e")

        ttk.Entry(self.input_frame, textvariable=self.date_var).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Entry(self.input_frame, textvariable=self.time_var).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Entry(self.input_frame, textvariable=self.description_var).grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Botones
        ttk.Button(self.input_frame, text="Seleccionar Fecha", command=self.pick_date).grid(row=0, column=2, padx=5,
                                                                                            pady=5)
        ttk.Button(self.input_frame, text="Agregar Evento", command=self.add_event).grid(row=3, column=0, columnspan=2,
                                                                                         padx=5, pady=5)
        ttk.Button(self.main_frame, text="Eliminar Evento Seleccionado", command=self.delete_event).grid(row=1,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=5,
                                                                                                         sticky="w")
        ttk.Button(self.main_frame, text="Salir", command=self.root.quit).grid(row=1, column=1, padx=10, pady=5,
                                                                               sticky="e")

        # Ejemplo de evento predefinido
        self.tree.insert("", "end", text="1", values=("2024-03-17", "12:00", "Reunión de trabajo"))

    def pick_date(self):
        # Abrir un calendario para seleccionar la fecha
        top = tk.Toplevel(self.root)
        cal = Calendar(top, selectmode="day", year=2024, month=3, day=1)
        cal.pack(padx=10, pady=10)

        def select_date():
            self.date_var.set(cal.get_date())
            top.destroy()

        ttk.Button(top, text="Seleccionar", command=select_date).pack(pady=5)

    def add_event(self):
        # Obtener los valores de la entrada
        date = self.date_var.get()
        time = self.time_var.get()
        description = self.description_var.get()

        # Verificar si todos los campos están completos
        if date and time and description:
            # Agregar el evento a la TreeView
            self.tree.insert("", "end", text=str(len(self.tree.get_children()) + 1), values=(date, time, description))

            # Limpiar los campos de entrada
            self.date_var.set("")
            self.time_var.set("")
            self.description_var.set("")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def delete_event(self):
        # Obtener el item seleccionado
        selected_item = self.tree.selection()
        if selected_item:
            # Confirmar la eliminación
            if messagebox.askyesno("Eliminar", "¿Está seguro de que desea eliminar el evento seleccionado?"):
                self.tree.delete(selected_item)
        else:
            messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar.")


def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()