from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
import subprocess

def open_manager():
    subprocess.Popen(["python", "students_interface.py"])


root = ttk.Window(themename="minty")
root.title("Students Manager")
root.resizable(FALSE,FALSE)

ttk.Label(root, text="Students Manager",font=("Arial", 30,'bold')).pack(pady=10,padx=10)

ttk.Button(root, text="Open manager",bootstyle="primary-outline", width=30,command=open_manager).pack(pady=50)
root.mainloop()