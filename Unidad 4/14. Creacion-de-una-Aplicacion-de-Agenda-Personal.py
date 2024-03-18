# Previo a ejecutar el programa es necesario instalar el componente tkcalendar
# Comando para instalar desde la consola o terminal
# pip install tkcalendar

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        self.event_frame = ttk.Frame(root)
        self.event_frame.pack(pady=10)

        # Lista de eventos
        self.event_list = ttk.Treeview(self.event_frame, columns=("Date", "Time", "Description"), selectmode="extended")
        self.event_list.heading("#0", text="ID")
        self.event_list.heading("Date", text="Date")
        self.event_list.heading("Time", text="Time")
        self.event_list.heading("Description", text="Description")
        self.event_list.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.event_frame, orient="vertical", command=self.event_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.event_list.configure(yscrollcommand=scrollbar.set)

        # Frame para la entrada de datos
        self.entry_frame = ttk.Frame(root)
        self.entry_frame.pack(pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(self.entry_frame, text="Date:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.date_entry = Calendar(self.entry_frame, selectmode="day", date_pattern="yyyy-mm-dd")
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.entry_frame, text="Time:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.time_entry = ttk.Entry(self.entry_frame)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.entry_frame, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.desc_entry = ttk.Entry(self.entry_frame)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones de acción
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)

        ttk.Button(self.button_frame, text="Add Event", command=self.add_event).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(self.button_frame, text="Delete Selected Event", command=self.delete_event).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.button_frame, text="Exit", command=root.quit).grid(row=0, column=2, padx=5, pady=5)

    def add_event(self):
        date = self.date_entry.get_date()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        if date and time and desc:
            self.event_list.insert("", "end", text=str(len(self.event_list.get_children()) + 1),
                                   values=(date, time, desc))
            self.date_entry.set_date(datetime.now())
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def delete_event(self):
        selected_items = self.event_list.selection()

        if selected_items:
            for item in selected_items:
                self.event_list.delete(item)
        else:
            messagebox.showerror("Error", "No event selected.")

def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

