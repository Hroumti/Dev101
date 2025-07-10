from tkinter import *
from tkinter import  messagebox
import ttkbootstrap as ttk
from student_DB import students_DB


class students_manager(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("Students Manager")
        self.db = students_DB()
        self.create_form()
        self.create_treeview()
        self.populate_treeview()
        self.mainloop()

    def create_form(self):
        form = LabelFrame(self, text="Form")
        form.pack(pady=10,fill="both",expand=True)

        Label(form, text="name:").grid(row=0, column=0, padx=5, pady=5)
        Label(form, text="age:").grid(row=1, column=0, padx=5, pady=5)
        Label(form, text="major:").grid(row=2, column=0, padx=5, pady=5)
        
        
        self.name_entry = Entry(form)
        self.age_entry = Entry(form)
        self.major_entry = ttk.Combobox(form,values=["Computer science", "Physics", "Alchemy"])
        
        
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)
        self.major_entry.grid(row=2, column=1, padx=5, pady=5)
        

        ttk.Button(form,bootstyle="success-outline", text="Add", command=self.add_entry).grid(row=3, column=0, padx=5, pady=10)
        ttk.Button(form,bootstyle="info-outline", text="Update", command=self.update_entry).grid(row=3, column=1, padx=5, pady=10)
        ttk.Button(form,bootstyle="danger-outline", text="Delete", command=self.delete_entry).grid(row=4, column=0, padx=5, pady=10)
        self.show = ttk.Button(form,bootstyle="secondary-outline", text="show/hide", command=self.hide_show)
        self.show.grid(row=4, column=1, padx=5, pady=10)

        self.filter_frame = LabelFrame(self, text="Filter")
        self.filter_frame.pack(pady=10,fill="both",expand=True)
        self.filter_var = StringVar()
        self.filter_var.set("All")
        self.values = ["All", "Computer science", "Physics", "Alchemy"]
        for value in self.values:
            Radiobutton(self.filter_frame, text=value, variable=self.filter_var, value=value,command=self.populate_treeview).pack(side=LEFT, padx=5, pady=5)

        self.tree_frame = Frame(self)
        

    def create_treeview(self):
        
        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "name", "age", "major"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("name", text="name")
        self.tree.heading("age", text="age")
        self.tree.heading("major", text="major")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("name", width=150)
        self.tree.column("age", width=200)
        self.tree.column("major", width=100)

        self.tree.pack(pady=20)
        self.tree.bind("<Double-1>", self.on_click)

    def populate_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        data = self.db.read_all()
        for record in data:
            if self.filter_var.get() == "All":
                self.tree.insert("", "end", values=record)
            elif record[3] == self.filter_var.get():
                self.tree.insert("", "end", values=record)

    def add_entry(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        major = self.major_entry.get()
        self.db.create(name, age, major)
        self.populate_treeview()
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.major_entry.delete(0, END)

    def update_entry(self):
        try:
            record_id = self.tree.item(self.tree.selection())["values"][0]
            name = self.name_entry.get()
            age = self.age_entry.get()
            major = self.major_entry.get()
            self.db.update(record_id, name, age, major)
            self.populate_treeview()
            self.name_entry.delete(0, END)
            self.age_entry.delete(0, END)
            self.major_entry.delete(0, END)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a record to update.")

    def delete_entry(self):
        try:
            record_id = self.tree.item(self.tree.selection())["values"][0]
            choice = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
            if choice:
                self.db.delete(record_id)
                self.populate_treeview()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a record to delete.")
        except :
            messagebox.showwarning("Warning", "Error.")

    def on_click(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            record_id = self.tree.item(item)["values"][0]
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, self.tree.item(item)["values"][1])
            self.age_entry.delete(0, END)
            self.age_entry.insert(0, self.tree.item(item)["values"][2])
            self.major_entry.delete(0, END)
            self.major_entry.insert(0, self.tree.item(item)["values"][3])

    def hide_show(self):
        if self.tree.winfo_ismapped():
            self.tree_frame.pack_forget()
        else:
            self.tree_frame.pack()

app = students_manager()