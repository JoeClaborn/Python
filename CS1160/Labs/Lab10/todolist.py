import tkinter as tk
from tkinter import messagebox
import pickle
import os
from datetime import datetime

class Task:
    def __init__(self, name, description, date, time):
        self.name = name
        self.description = description
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.name} - {self.description} - Due: {self.date} at {self.time}"

class PersonalTask(Task):
    pass

class SchoolTask(Task):
    pass

class WorkTask(Task):
    pass

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        for t in self.tasks:
            if t.name == task.name:
                return ("name", t)
            if t.date == task.date and t.time == task.time:
                return ("datetime", t)
        self.tasks.append(task)
        return ("success", None)

    def remove_task(self, task_name):
        for t in self.tasks:
            if t.name == task_name:
                self.tasks.remove(t)
                return True
        return False

    def get_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open("todo.pickle", "wb") as f:
            pickle.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists("todo.pickle"):
            with open("todo.pickle", "rb") as f:
                self.tasks = pickle.load(f)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x350")
        self.todo_list = TodoList()

        self.frame = tk.Frame(root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.name_label = tk.Label(self.frame, text="Task Name:")
        self.name_entry = tk.Entry(self.frame)

        self.description_label = tk.Label(self.frame, text="Description:")
        self.description_entry = tk.Entry(self.frame)

        self.date_label = tk.Label(self.frame, text="Date:")
        self.date_entry = tk.Entry(self.frame)

        self.time_label = tk.Label(self.frame, text="Time:")
        self.hour_entry = tk.Entry(self.frame, width=10)
        self.colon_label = tk.Label(self.frame, text=":")
        self.minute_entry = tk.Entry(self.frame, width=10)

        self.type_label = tk.Label(self.frame, text="Task Type:")
        self.type_var = tk.StringVar(value="Generic")
        self.type_menu = tk.OptionMenu(self.frame, self.type_var, "Generic", "Personal", "School", "Work")

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.display_button = tk.Button(self.frame, text="Display Tasks", command=self.display_tasks)
        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task)
        self.quit_button = tk.Button(self.frame, text="Save and Quit", command=self.on_closing)

        self.name_label.grid(row=0, column=0, columnspan=2, sticky="w")
        self.name_entry.grid(row=1, column=0, columnspan=2, sticky="we")

        self.description_label.grid(row=2, column=0, columnspan=2, sticky="w")
        self.description_entry.grid(row=3, column=0, columnspan=2, sticky="we")

        self.date_label.grid(row=4, column=0, columnspan=2, sticky="w")
        self.date_entry.grid(row=5, column=0, columnspan=2, sticky="we")

        self.time_label.grid(row=6, column=0, columnspan=2, sticky="w")
        self.hour_entry.grid(row=7, column=0, sticky="e")
        self.colon_label.grid(row=7, column=1, sticky="w")
        self.minute_entry.grid(row=7, column=1, sticky="e")

        self.type_label.grid(row=8, column=0, columnspan=2, sticky="w")
        self.type_menu.grid(row=9, column=0, columnspan=2, sticky="we")

        self.add_button.grid(row=10, column=0, pady=5)
        self.display_button.grid(row=10, column=1, pady=5)
        self.remove_button.grid(row=11, column=0, columnspan=2, pady=5)
        self.quit_button.grid(row=12, column=0, columnspan=2, pady=5)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        name = self.name_entry.get().strip()
        description = self.description_entry.get().strip()
        date = self.date_entry.get().strip()
        hour = self.hour_entry.get().strip()
        minute = self.minute_entry.get().strip()
        task_type = self.type_var.get()

        if not name:
            messagebox.showerror("Oops!", "You are missing a name for the task!")
            return
        elif not description:
            messagebox.showerror("Oops!", "You are missing a description for the task!")
            return
        elif not date:
            messagebox.showerror("Oops", "You are missing the date for the task!")
            return
        elif not hour or not minute:
            messagebox.showerror("Oops!", "You are missing the time for the task!")
            return

        try:
            datetime.strptime(date, "%m/%d/%Y")
        except ValueError:
            messagebox.showerror("Oops!", "Date format is incorrect. Use MM/DD/YYYY!")
            return

        try:
            hour_int = int(hour)
            minute_int = int(minute)
            if not (0 <= hour_int <= 23 and 0 <= minute_int <= 59):
                raise ValueError
            time = f"{hour_int:02}:{minute_int:02}"
        except ValueError:
            messagebox.showerror("Oops!", "Time format is incorrect. Use 24hr HH:MM with valid numbers!")
            return

        if task_type == "Personal":
            task = PersonalTask(name, description, date, time)
        elif task_type == "School":
            task = SchoolTask(name, description, date, time)
        elif task_type == "Work":
            task = WorkTask(name, description, date, time)
        else:
            task = Task(name, description, date, time)

        result, existing_task = self.todo_list.add_task(task)
        if result == "name":
            messagebox.showwarning("Oops!", "There already exists a task with that name!")
        elif result == "datetime":
            messagebox.showwarning("Oops!", f"The task {existing_task.name} is already scheduled for {task.date} at {task.time}")
        else:
            messagebox.showinfo("Success", "Task added successfully.")

    def display_tasks(self):
        tasks = self.todo_list.get_tasks()
        if not tasks:
            messagebox.showinfo("Tasks", "No tasks available.")
        else:
            task_text = "\n".join(str(task) for task in tasks)
            messagebox.showinfo("Tasks", task_text)

    def remove_task(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Oops!", "Task name is required to remove a task.")
            return
        if self.todo_list.remove_task(name):
            messagebox.showinfo("Success", "Task removed successfully.")
        else:
            messagebox.showwarning("Oops!", "No task found with that name.")

    def on_closing(self):
        self.todo_list.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
