import tkinter as tk
from tkinter import messagebox
import random

class RandNumApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Number Game")
        self.master.geometry("300x200")

        self.label = tk.Label(master, text="A random number between 1 and 100 has been generated, make your guess!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        # self.random_number = random.randint(1, 100)
        self.random_number = 3 # testing purposes
        self.guesses = 0
        self.button_guess = tk.Button(master, text="Make a Guess", command=self.check_guess)
        self.button_guess.pack(pady=10)

    def generate_random_number(self):
        try:
            num = int(self.entry.get())
            if num < 1:
                raise ValueError("Number must be positive.")
            random_number = random.randint(1, num)
            messagebox.showinfo("Random Number", f"Random number between 1 and {num}: {random_number}")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 100:
                raise ValueError("Guess must be between 1 and 100.")
            if guess == self.random_number:
                messagebox.showinfo("Congrats!", f"You Win!\nIt took you {self.guesses} guesses!")
            elif guess < self.random_number:
                messagebox.showinfo("Your guess was too low!")
            else:
                messagebox.showinfo("Your guess was too high!")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))