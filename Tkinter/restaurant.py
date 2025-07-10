from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from random import randint
from datetime import datetime
class billing_system:
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.title("billing system")
        self.root.resizable(FALSE,FALSE)

        self.display()
        
        self.root.mainloop()

    def display(self):
        ttk.Label(self.root, text="Da Ali Bighrdayn Resturant", font=("Arial", 30,'bold','underline'),bootstyle="light").grid(row=0, columnspan=2,pady=10,padx=30)
        self.left = Frame(self.root)
        self.entries = []
        for i in range(7):
            ttk.Label(self.left, text=f"Food {i+1}").grid(row=i, column=0,padx=40, pady=10)
            self.entries.append((ttk.Spinbox(self.left,from_=0, to=10)))
            self.entries[i].grid(row=i, column=1, padx=10, pady=10)

        self.reset()
        
        self.prices = [randint(7,30) for i in range(7)]
        for i in range(7):
            ttk.Label(self.left, text=f'{self.prices[i]:02d} DH').grid(row=i, column=2, padx=10, pady=10)

        ttk.Button(self.left, text="Generate the bill",bootstyle="success-outline",width=40,command=self.calculate).grid(row=7, columnspan=2, padx=10, pady=10)

        self.left.grid(row=1, column=0, padx=100, pady=50)

        self.right = ttk.Frame(self.root)

        ttk.Label(self.right, text="Bill number").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.right, text="Date").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.right, text="Total").grid(row=2, column=0, padx=10, pady=10)
        ttk.Label(self.right, text="Service fee").grid(row=3, column=0, padx=10, pady=10)
        ttk.Label(self.right, text="Tax").grid(row=4, column=0, padx=10, pady=10)
        ttk.Label(self.right, text="Grand total").grid(row=5, column=0, padx=10, pady=10)


        self.num_entry = StringVar()
        self.date = StringVar()
        self.total = DoubleVar()
        self.service_fee = DoubleVar()
        self.tax = DoubleVar()
        self.grand_total = DoubleVar()

        self.num = IntVar()
        self.num.set(0)

        ttk.Entry(self.right,state='readonly',bootstyle='danger' ,textvariable=self.num_entry).grid(row=0, column=1, padx=10, pady=10)
        ttk.Entry(self.right,state='readonly',bootstyle='success' ,textvariable=self.date).grid(row=1, column=1, padx=10, pady=10)
        ttk.Entry(self.right,state='readonly',bootstyle='success' ,textvariable=self.total).grid(row=2, column=1, padx=10, pady=10)
        ttk.Entry(self.right,state='readonly',bootstyle='success' ,textvariable=self.service_fee).grid(row=3, column=1, padx=10, pady=10)
        ttk.Entry(self.right,state='readonly',bootstyle='success' ,textvariable=self.tax).grid(row=4, column=1, padx=10, pady=10)
        ttk.Entry(self.right,state='readonly',bootstyle='success' ,textvariable=self.grand_total).grid(row=5, column=1, padx=10, pady=10)

        self.right.grid(row=1, column=1, padx=100, pady=50)

    def calculate(self):
        try:
            self.num.set(self.num.get() + 1)
            total = 0
            for i in range(7):
                entry = float(self.entries[i].get())
                total += entry*self.prices[i]
            self.num_entry.set(f"{self.num.get():04d}")
            self.total.set(total)
            self.service_fee.set(round(total * 0.1,2))
            self.tax.set(round(total * 0.05,2))
            self.grand_total.set(round(total + self.service_fee.get() + self.tax.get(),2))

            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.date.set(date)
            for entry in self.entries:
                entry.set(0)
        except:
            messagebox.showerror("Error", "Please enter a valid number")

    def reset(self):
        for entry in self.entries:
            entry.set(0)
app = billing_system()