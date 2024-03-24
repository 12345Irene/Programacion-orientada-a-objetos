import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Tareas")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        self.task_list = tk.Listbox(master, width=50)
        self.task_list.pack()

        self.task_entry.bind("<Return>", self.add_task_enter)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "Por favor ingrese una tarea válida.")

    def add_task_enter(self, event):
        self.add_task()

    def complete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.itemconfig(selected_index, {'bg': 'light green'})
        except IndexError:
            messagebox.showwarning("Atención", "Por favor seleccione una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Atención", "Por favor seleccione una tarea para eliminar.")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()