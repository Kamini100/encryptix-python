import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Initialize tasks list
        self.tasks = []

        # Create GUI elements
        self.task_listbox = tk.Listbox(root,background="skyblue", height=15, width=50, borderwidth=2, relief="solid")
        self.task_listbox.pack(pady=10)

        self.task_entry = tk.Entry(root,background="skyblue", width=50, borderwidth=2, relief="solid")
        self.task_entry.pack()

        self.add_button = tk.Button(root, background="red", text="Add Task", width=48, command=self.add_task)
        self.add_button.pack(pady=10)

        self.update_button = tk.Button(root, background="red", text="Update Selected", width=48, command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root,background="red", text="Delete Selected", width=48, command=self.delete_task)
        self.delete_button.pack(pady=10)

        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index[0]] = updated_task
                self.refresh_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        else:
            messagebox.showwarning("Warning", "Please select a task to update!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
