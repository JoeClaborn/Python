import tkinter as tk
from tkinter import messagebox
import pickle
import os
from datetime import datetime

# Task class for setting the name, description, date, and time of the task input by the user.
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

# Class for adding, removing, getting, saving, and loading the tasks.
class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    # Add task definition for adding a task to the list. Returns success if the task was added.
    def add_task(self, task):
        for t in self.tasks:
            if t.name == task.name:
                return ("name", t)
            if t.date == task.date and t.time == task.time:
                return ("datetime", t)
        self.tasks.append(task)
        return ("success", None)

    # Remove task definition for removing a task from the list. Checks if the name of the task is
    # a saved task's name, if so, remove the task input by the user. Otherwise, return false.
    def remove_task(self, task_name):
        for t in self.tasks:
            if t.name == task_name:
                self.tasks.remove(t)
                return True
        return False

    def get_tasks(self):
        return self.tasks

    # Save task definition for saving the tasks to the list. Happens by opening the 'todo.pickle' file
    # and dump the tasks in the list to the file for saving.
    def save_tasks(self):
        with open("todo.pickle", "wb") as f:
            pickle.dump(self.tasks, f)

    # Load task definition for loading the tasks from the list when GUI is opened. Happens by checking
    # if the file exists 'todo.pickle', then opens the file and sets the tasks list to the load of the pickle file.
    def load_tasks(self):
        if os.path.exists("todo.pickle"):
            with open("todo.pickle", "rb") as f:
                self.tasks = pickle.load(f)

# Main class for the GUI. Sets all of the labels, size, titles, etc.
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App") # Sets the title of the GUI to 'To-Do List App'.
        self.root.geometry("400x350") # Sets the size of the GUI window to '400x350'.
        self.todo_list = TodoList()

        self.frame = tk.Frame(root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.name_label = tk.Label(self.frame, text="Task Name:") # Sets the label of the task name input for clarity.
        self.name_entry = tk.Entry(self.frame) # Entry box for user input.

        self.description_label = tk.Label(self.frame, text="Description:") # Sets the label of the description input for clarity.
        self.description_entry = tk.Entry(self.frame) # Entry box for user input.

        self.date_label = tk.Label(self.frame, text="Date:") # Sets the label of the date input for clarity.
        self.date_entry = tk.Entry(self.frame) # Entry box for user input.

        self.time_label = tk.Label(self.frame, text="Time:")# Sets the label of the time input for clarity.
        self.hour_entry = tk.Entry(self.frame, width=10) # Entry box for user input.
        self.colon_label = tk.Label(self.frame, text=":") # Label to add a ':' to the middle of the two input boxes for the time.
        self.minute_entry = tk.Entry(self.frame, width=10) # Entry box for user input.

        self.type_label = tk.Label(self.frame, text="Task Type:") # Label for task type with buttons below for what type of task it is.
        self.type_var = tk.StringVar(value="Generic") # Default button
        self.type_menu = tk.OptionMenu(self.frame, self.type_var, "Generic", "Personal", "School", "Work") # Adds an option menu for the task types for the user to choose from.

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task) # Button for adding a task to the list.
        self.display_button = tk.Button(self.frame, text="Display Tasks", command=self.display_tasks) # Button for displaying the tasks saved in the list.
        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task) # Button to remove a task from the list.
        self.quit_button = tk.Button(self.frame, text="Save and Quit", command=self.on_closing) # Button to save and quit the GUI program.

        # Code below used for the design of the GUI with where the text boxes, labels, buttons, etc. are held.
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

    # Definition for adding a task to the list. Happens by stripping/getting all of the required values of a given task.
    def add_task(self):
        name = self.name_entry.get().strip()
        description = self.description_entry.get().strip()
        date = self.date_entry.get().strip()
        hour = self.hour_entry.get().strip()
        minute = self.minute_entry.get().strip()
        task_type = self.type_var.get()

        # Checks for if the user input is not missing. If the user input is missing, then it prompts the user what they are missing.
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

        # Strips the date and format used for such. If the date format is incorrect, print a message box to the user.
        try:
            datetime.strptime(date, "%m/%d/%Y")
        except ValueError:
            messagebox.showerror("Oops!", "Date format is incorrect. Use MM/DD/YYYY!")
            return

        # Checks for if the hour and minute inputs are within constraint. If they are, accept the format as HH:MM,
        # if they are not, display a message box to the user showing the time format is incorrect.
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
        # Checks if the the input task's name or date and time already exists and if so, display a message box to the user.
        # Otherwise, print that the task was added sucessfully.
        if result == "name":
            messagebox.showwarning("Oops!", "There already exists a task with that name!")
        elif result == "datetime":
            messagebox.showwarning("Oops!", f"The task {existing_task.name} is already scheduled for {task.date} at {task.time}")
        else:
            messagebox.showinfo("Success", "Task added successfully.")

    # Displays the tasks in the list. If there are no tasks in the list, show a message box as such, if there is
    # display the tasks to the user.
    def display_tasks(self):
        tasks = self.todo_list.get_tasks()
        if not tasks:
            messagebox.showinfo("Tasks", "No tasks available.")
        else:
            task_text = "\n".join(str(task) for task in tasks)
            messagebox.showinfo("Tasks", task_text)

    # Removes a task from the list. If the task name does not match to a task in the list, display a message box
    # saying such. If the task name does exist and is the same as entered, then remove the task and display a success message.
    # If the user does not enter a task name when removing a task, show a message box saying the name is required.
    def remove_task(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Oops!", "Task name is required to remove a task.")
            return
        if self.todo_list.remove_task(name):
            messagebox.showinfo("Success", "Task removed successfully.")
        else:
            messagebox.showwarning("Oops!", "No task found with that name.")

    # Definition for when the GUI is closed.
    def on_closing(self):
        self.todo_list.save_tasks() # When the GUI is closed, save the tasks to the todo_list file.
        self.root.destroy() # Destroy the GUI, causing it to close.

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
