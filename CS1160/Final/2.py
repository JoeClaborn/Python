import tkinter as tk
from tkinter import messagebox
import random

class RandNumApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Number Game")
        self.master.geometry("800x400")
        self.v = tk.StringVar()
        self.v.set("A random number between 1 and 100 has been generated, \nmake your guess!")

        self.label = tk.Label(master, text=self.v.get())
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.random_number = random.randint(1, 100)
        self.guesses = 0
        self.button_guess = tk.Button(master, text="Make a Guess", command=self.check_guess)
        self.button_guess.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 100:
                raise ValueError("Guess must be between 1 and 100.")
            if guess == self.random_number:
                messagebox.showinfo("Congrats!", f"You Win!\nIt took you {self.guesses} guesses!")
                self.master.quit()
            elif guess < self.random_number:
                self.v.set("Your guess was too low!")
                self.label = tk.Label(self.master, text=self.v.get())
                self.label.pack(pady=10)
                self.guesses += 1
            else:
                self.v.set("Your guess was too high!")
                self.label = tk.Label(self.master, text=self.v.get())
                self.label.pack(pady=10)
                self.guesses += 1
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = RandNumApp(root)
    root.mainloop()