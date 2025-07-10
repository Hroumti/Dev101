from tkinter import *
import ttkbootstrap as ttk
import subprocess

def open_app():
    subprocess.Popen(["python", "tkinter/DB_main.py"])

root = ttk.Window(themename="superhero")
root.title("Application DB")
root.geometry("700x300")

ttk.Label(root, text="Application DB", font=("Arial", 40,'italic')).pack(pady=10,padx=10)

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="DB-APP", command=open_app)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda :root.destroy())





root.mainloop()