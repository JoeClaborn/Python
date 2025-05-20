import tkinter as tk
import tkinter.messagebox

root = ""

class GUI:

    def __init__(self, root):
        self.counter = 0
        self.root = root
        self.root.title("Baby's First GUI")

        self.init_string_vars()

        self.init_widgets(root)

        self.pack_widgets()

    def init_string_vars(self):
        self.string_var_0 = tk.StringVar()
        self.string_var_1 = tk.StringVar()
        self.string_var_2 = tk.StringVar()
        self.string_var_2.set("Click me to select your option...")

    def init_widgets(self, root):
        self.label_0 = tk.Label(root, text="First Column", textvariable=self.string_var_0)
        self.label_1 = tk.Label(root, text="Welcome to My Counter Program!")
        self.entry_0 = tk.Entry(root, textvariable=self.string_var_1)
        self.button_0 = tk.Button(root, text="Change Counter", command=self.on_button_0_click)
        #self.button_1 = tk.Button(root, text="Decrement Counter", command=self.on_button_1_click)

        self.dropdown_0 = tk.OptionMenu(root, self.string_var_2, "Increment", "Decrement", "Multiply", "Divide", command=self.on_dropdown_selected)

        self.grid_canvas_0 = tk.Canvas(root)

        self.check_box_00 = tk.Checkbutton(self.grid_canvas_0)
        self.check_box_01 = tk.Checkbutton(self.grid_canvas_0)
        self.check_box_10 = tk.Checkbutton(self.grid_canvas_0)
        self.check_box_11 = tk.Checkbutton(self.grid_canvas_0)

        self.points = [100, 10, 150, 10, 150, 60, 100, 60]
        self.points_canvas_0 = tk.Canvas()
        self.points_canvas_0.create_polygon(self.points, outline = "blue", fill = "orange", width = 2)

    def pack_widgets(self):
        self.label_1.pack(padx=15, pady=(50, 10))#grid(row=0, column=1)
        self.entry_0.pack()
        self.label_0.pack(padx=30, pady=10)#grid(row=0, column=0)
        self.button_0.pack()
        self.grid_canvas_0.pack()
        #self.button_1.pack()

        self.dropdown_0.pack()

        self.check_box_00.grid(row=0, column=0)
        self.check_box_01.grid(row=0, column=1)
        self.check_box_10.grid(row=1, column=0)
        self.check_box_11.grid(row=1, column=1)

        self.points_canvas_0.pack()

    def on_button_0_click(self):
        try:
            user_input = int(self.string_var_1.get())
        except ValueError:
            tk.messagebox.showinfo("Oops!", "Please type a valid number before hitting the button!")
            self.string_var_0.set("You must type in a number!")
            return

        dropdown_selection = self.string_var_2.get()

        print(f"Selection is {dropdown_selection}")

        if dropdown_selection == "Increment":
            self.counter += user_input

        elif dropdown_selection == "Decrement":
            self.counter -= user_input

        elif dropdown_selection == "Multiply":
            self.counter *= user_input

        elif dropdown_selection == "Divide":
            self.counter /= user_input

        else:
            tk.messagebox.showinfo("Oops!", "Please make a selection before hitting the button!")
            return
        
        #print(f"Counter: {self.counter}")
        self.string_var_0.set(f"Counter: {self.counter}")

    def on_dropdown_selected(self, selected):
        self.string_var_0.set(f"You have selected {selected}")

    def on_button_1_click(self):
        try:
            user_input = int(self.string_var_1.get())
        except ValueError:
            self.string_var_0.set("You must type in a number!")
            return
        
        self.counter -= user_input
        #print(f"Counter: {self.counter}")
        self.string_var_0.set(f"Counter: {self.counter}")
        

def main():
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_quit)
    app = GUI(root)
    root.mainloop()

def on_quit():
    user_wants_to_quit = tk.messagebox.askokcancel("Quit?", "Are you sure you want to quit?")

    if user_wants_to_quit:
        # save progress
        root.destroy()

if __name__ == "__main__":
    main()
