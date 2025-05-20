<<<<<<< HEAD
import tkinter as tk

class GUI:

    def __init__(self, root):
        self.clicks = 0
        self.root = root
        self.root.title("Baby's First GUI")

        self.string_var_0 = tk.StringVar()
        self.string_var_1 = tk.StringVar()

        self.label_0 = tk.Label(root, text="First Column", textvariable=self.string_var_0)
        self.label_1 = tk.Label(root, text="Welcome to My Counter Program!")
        self.entry_0 = tk.Entry(root, textvariable=self.string_var_1)
        self.button_0 = tk.Button(root, text="Increment Counter", command=self.on_button_0_click)
        self.button_1 = tk.Button(root, text="Decrement Counter", command=self.on_button_1_click)

        self.label_1.pack(padx=15, pady=(50, 10))#grid(row=0, column=1)
        self.entry_0.pack()
        self.label_0.pack(padx=30, pady=10)#grid(row=0, column=0)
        self.button_0.pack()
        self.button_1.pack()

    def on_button_0_click(self):
        try:
            user_input = int(self.string_var_1.get())
        except ValueError:
            self.string_var_0.set("You must type in a number!")
            return
        
        self.clicks += user_input
        #print(f"Counter: {self.clicks}")
        self.string_var_0.set(f"Counter: {self.clicks}")
        

    def on_button_1_click(self):
        try:
            user_input = int(self.string_var_1.get())
        except ValueError:
            self.string_var_0.set("You must type in a number!")
            return
        
        self.clicks -= user_input
        #print(f"Counter: {self.clicks}")
        self.string_var_0.set(f"Counter: {self.clicks}")
        

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
=======
import tkinter as tk

class GUI:

    def __init__(self, root):
        self.clicks = 0
        self.root = root
        self.root.title("Baby's First GUI")

        self.string_var_0 = tk.StringVar()
        self.string_var_1 = tk.StringVar()

        self.label_0 = tk.Label(root, text="First Column", textvariable=self.string_var_0)
        self.label_1 = tk.Label(root, text="Welcome to My Counter Program!")
        self.entry_0 = tk.Entry(root, textvariable=self.string_var_1)
        self.button_0 = tk.Button(root, text="Increment Counter", command=self.on_button_0_click)
        self.button_1 = tk.Button(root, text="Decrement Counter", command=self.on_button_1_click)

        self.label_1.pack(padx=15, pady=(50, 10))#grid(row=0, column=1)
        self.entry_0.pack()
        self.label_0.pack(padx=30, pady=10)#grid(row=0, column=0)
        self.button_0.pack()
        self.button_1.pack()

    def on_button_0_click(self):
        try:
            user_input = int(self.string_var_1.get())
        except ValueError:
            self.string_var_0.set("You must type in a number!")
            return
        
        self.clicks += user_input
        #print(f"Counter: {self.clicks}")
        self.string_var_0.set(f"Counter: {self.clicks}")
        

    def on_button_1_click(self):
        try:
            user_input = int(self.string_var_1.get())
        except ValueError:
            self.string_var_0.set("You must type in a number!")
            return
        
        self.clicks -= user_input
        #print(f"Counter: {self.clicks}")
        self.string_var_0.set(f"Counter: {self.clicks}")
        

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
