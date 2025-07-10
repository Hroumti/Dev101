from tkinter import *
from tkinter import ttk, messagebox
from DB_manager import manager
from tkcalendar import DateEntry


class DBApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Application DB")
        self.db = manager() #attribute
        self.create_form()
        self.create_treeview()
        self.populate_treeview()
        self.mainloop()

    def create_form(self):
        form = LabelFrame(self, text="Form")
        form.pack(pady=10)
        Label(form, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        Label(form, text="Description:").grid(row=1, column=0, padx=5, pady=5)
        Label(form, text="Priority:").grid(row=2, column=0, padx=5, pady=5)
        Label(form, text="Status:").grid(row=3, column=0, padx=5, pady=5)
        Label(form, text="Due Date:").grid(row=4, column=0, padx=5, pady=5)
        
        self.title_entry = Entry(form)
        self.description_entry = Entry(form)
        self.priority_entry = ttk.Combobox(form,values=["Low", "Medium", "High"])
        self.status_entry = StringVar(value="To Do")
        Radiobutton(form, text="To Do", variable=self.status_entry, value="To Do").grid(row=3, column=1, padx=5, pady=5, stick=W)
        Radiobutton(form, text="In Progress", variable=self.status_entry, value="In Progress").grid(row=3, column=2, padx=5, pady=5, sticky=N)
        Radiobutton(form, text="Done", variable=self.status_entry, value="Done").grid(row=3, column=3, padx=5, pady=5, sticky=E)
        self.due_date_entry = DateEntry(form)
        
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)
        self.priority_entry.grid(row=2, column=1, padx=5, pady=5)
        self.due_date_entry.grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(form, text="Add", command=self.add_entry).grid(row=5, columnspan=2, padx=5, pady=10)
        ttk.Button(form, text="Update", command=self.update_entry).grid(row=6, column=0, padx=5, pady=10)
        ttk.Button(form, text="Delete", command=self.delete_entry).grid(row=6, column=1, padx=5, pady=10)

    def create_treeview(self):
        self.tree = ttk.Treeview(self, columns=("ID", "Title", "Description", "Priority", "Status", "Creation Date", "Due Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Creation Date", text="Creation Date")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Title", width=150)
        self.tree.column("Description", width=200)
        self.tree.column("Priority", width=100)
        self.tree.column("Status", width=100)
        self.tree.column("Creation Date", width=100)
        self.tree.column("Due Date", width=100)
        self.tree.pack(pady=20)
        self.tree.bind("<Double-1>", self.on_click)

    def populate_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        data = self.db.read_all()
        for record in data:
            self.tree.insert("", "end", values=record)

    def add_entry(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_entry.get()
        status = self.status_entry.get()
        due_date = self.due_date_entry.get() 
        self.db.create(title, description, priority, status, due_date)
        self.populate_treeview()
        self.title_entry.delete(0, END)
        self.description_entry.delete(0, END)
        self.priority_entry.delete(0, END)
        self.due_date_entry.delete(0, END)

    def update_entry(self):
        try:
            record_id = self.tree.item(self.tree.selection())["values"][0]
            title = self.title_entry.get()
            description = self.description_entry.get()
            priority = self.priority_entry.get()
            status = self.status_entry.get()
            due_date = self.due_date_entry.get()
            self.db.update(record_id, title, description, priority, status, due_date)
            self.populate_treeview()
            self.title_entry.delete(0, END)
            self.description_entry.delete(0, END)
            self.priority_entry.delete(0, END)
            self.due_date_entry.delete(0, END)
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
            self.title_entry.delete(0, END)
            self.title_entry.insert(0, self.tree.item(item)["values"][1])
            self.description_entry.delete(0, END)
            self.description_entry.insert(0, self.tree.item(item)["values"][2])
            self.priority_entry.delete(0, END)
            self.priority_entry.insert(0, self.tree.item(item)["values"][3])
            self.status_entry.set(self.tree.item(item)["values"][4])
            self.due_date_entry.delete(0, END)
            self.due_date_entry.insert(0, self.tree.item(item)["values"][6])

app = DBApp()