import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

class calculator:
    def __init__(self):
        self.root = ttk.Window(themename="morph")
        self.root.title("Calories Calculator")
        self.root.geometry("800x500")
        self.root.resizable('false','false')

        self.display()
        
    def display(self):
        ttk.Label(self.root, text="Calories Calculator", font=("Arial", 20)).pack(pady=10)

        self.frame_1 = ttk.Frame(self.root)
        self.frame_1.pack(pady=10)

    

        self.food1_check_var = tk.IntVar()
        self.food2_check_var = tk.IntVar()
        self.food3_check_var = tk.IntVar()
        self.food4_check_var = tk.IntVar()


        self.food1_check = ttk.Checkbutton(self.frame_1,variable=self.food1_check_var ,text="food1", command=self.enable_entry)
        self.food2_check = ttk.Checkbutton(self.frame_1,variable=self.food2_check_var ,text="food2", command=self.enable_entry)
        self.food3_check = ttk.Checkbutton(self.frame_1,variable=self.food3_check_var ,text="food3", command=self.enable_entry)
        self.food4_check = ttk.Checkbutton(self.frame_1,variable=self.food4_check_var ,text="food4", command=self.enable_entry)

        self.food1 = tk.IntVar()
        self.food2 = tk.IntVar()
        self.food3 = tk.IntVar()
        self.food4 = tk.IntVar()

        self.food1_check.grid(row = 0, column = 0, padx=10, pady=5)
        self.food2_check.grid(row = 1, column = 0, padx=10, pady=5)
        self.food3_check.grid(row = 2, column = 0, padx=10, pady=5)
        self.food4_check.grid(row = 3, column = 0, padx=10, pady=5)

        self.entry1 = ttk.Entry(self.frame_1, textvariable=self.food1, state="disabled")
        self.entry2 = ttk.Entry(self.frame_1, textvariable=self.food2, state="disabled")
        self.entry3 = ttk.Entry(self.frame_1, textvariable=self.food3, state="disabled")
        self.entry4 = ttk.Entry(self.frame_1, textvariable=self.food4, state="disabled")

        self.entry1.grid(row = 0, column = 1, padx=10, pady=5)
        self.entry2.grid(row = 1, column = 1, padx=10, pady=5)
        self.entry3.grid(row = 2, column = 1, padx=10, pady=5)
        self.entry4.grid(row = 3, column = 1, padx=10, pady=5)

        for i in range(3):
            ttk.Label(self.frame_1, text="Grammes").grid(row = i, column = 2, padx=10, pady=5)
        ttk.Label(self.frame_1, text="Units").grid(row = 3, column = 2, padx=10, pady=5)

        self.calculate = ttk.Button(self.frame_1, text="Calculate", width=20, command=self.calculate)
        self.reset = ttk.Button(self.frame_1, text="Reset", width=20, command=self.reset)
        self.calculate.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.reset.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10)

        self.result = ttk.Label(self.root, text="the result is :", font=("Arial", 20))
        self.result.pack(pady=10)

        self.root.mainloop()

    def enable_entry(self):
        if self.food1_check_var.get() == 1:
            self.entry1.config(state="normal")
        else:
            self.entry1.config(state="disabled")
            self.food1.set(0)

        if self.food2_check_var.get() == 1:
            self.entry2.config(state="normal")
        else:
            self.entry2.config(state="disabled")
            self.food2.set(0)

        if self.food3_check_var.get() == 1:
            self.entry3.config(state="normal")
        else:
            self.entry3.config(state="disabled")
            self.food3.set(0)

        if self.food4_check_var.get() == 1:
            self.entry4.config(state="normal")
        else:
            self.entry4.config(state="disabled")
            self.food4.set(0)

    def calculate(self):
        try:
            food1 = self.entry1.get()
            food2 = self.entry2.get()
            food3 = self.entry3.get()
            food4 = self.entry4.get()


            total_calories = int(food1) * 27.5 + int(food2) * 25 + int(food3) * 12 + int(food4) * 116

            self.result.config(text="the result is : " + str(total_calories) + "Kcal")
        except:
            messagebox.showerror("Error", "Please enter a valid number")
        

    def reset(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)
        self.result.config(text="the result is : ")
        self.food1_check_var.set(0)
        self.food2_check_var.set(0)
        self.food3_check_var.set(0)
        self.food4_check_var.set(0)


app = calculator()

