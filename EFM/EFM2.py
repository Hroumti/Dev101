import ttkbootstrap as ttk
from abc import ABC, abstractmethod
from tkinter import messagebox

class capacity_error(Exception):    
    pass
class NotImplementedError(Exception):
    pass

class Vehicle(ABC):
    def __init__(self, client, reg_num, capacity):
        self.client = client
        self.reg_num = reg_num
        self.capacity = capacity
        if capacity < 0:
            raise capacity_error("Capacity cannot be negative")
        
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity < 0:
            raise capacity_error("Capacity cannot be negative")
        self._capacity = new_capacity

    def __str__(self):
        return f"client {self.client}; reg_num {self.reg_num}; capacity {self.capacity}"

    def __eq__(self, value):
        return self.reg_num == value.reg_num
    
    @abstractmethod
    def calculate_efficiency(self):
        raise NotImplementedError
class Car(Vehicle):
    def __init__(self, client, reg_num, capacity, consumption):
        super().__init__(client, reg_num, capacity)
        self.consumption = consumption

    def calculate_efficiency(self):
        return self.consumption / self.capacity if self.capacity != 0 else 0
    
    
class Truck(Vehicle):
    def __init__(self,  client, reg_num, capacity, load_capacity):
        super().__init__( client, reg_num, capacity)
        self.load_capacity = load_capacity

    def calculate_efficiency(self):
        return self.load_capacity / self.capacity if self.capacity != 0 else 0
    
class Motorcycle(Vehicle):
    def __init__(self,  client, reg_num, capacity):
        super().__init__( client, reg_num, capacity)

    def calculate_efficiency(self):
        return super().calculate_efficiency()
    
#----------------------------------------------------------------------

class app():
    def __init__(self):
        self.root = ttk.Window(themename="morph")
        self.root.title("Vehicle Manager")
        self.root.geometry("800x500")
        self.list = []
        

        self.display()
        self.root.mainloop()

    def display(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        ttk.Label(self.frame, text="Registration number").grid(row=0, column=0)
        self.reg_entry = ttk.Entry(self.frame)
        self.reg_entry.grid(row=0, column=1, padx=10, pady=10)
        
        ttk.Label(self.frame, text="Capacity").grid(row=1, column=0, padx=10, pady=10)
        self.capacity_entry = ttk.Entry(self.frame)
        self.capacity_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.frame, text="Type").grid(row=2, column=0, padx=10, pady=10)
        self.type = ttk.Combobox(self.frame, values=["Car", "Truck", "Motorcycle"])
        self.type.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = ttk.Button(self.frame, text="Add", command=self.add_vehicle)
        self.add_button.grid(row=4, columnspan=2, pady=10)

        self.delete_button = ttk.Button(self.frame, text="Delete", command=self.delete_vehicle)
        self.delete_button.grid(row=5, columnspan=2, pady=10)

        self.update_button = ttk.Button(self.frame, text="Update", command=self.update_vehicle)
        self.update_button.grid(row=6, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Registration number", "Capacity", "type", "Efficiency"), show="headings")
        self.tree.heading("Registration number", text="Registration number")
        self.tree.heading("Capacity", text="Capacity")
        self.tree.heading("type", text="type")
        self.tree.heading("Efficiency", text="Efficiency")
        self.tree.pack(padx=10, pady=20)




    def add_vehicle(self):
        
            reg_num = self.reg_entry.get()
            capacity = int(self.capacity_entry.get())
            if self.type.get() == "Car":
                consumption = float(input("Enter consumption: "))
                v = Car("client", reg_num, capacity, consumption)

            elif self.type.get() == "Truck":
                load = float(input("Enter load: "))
                v = Truck("client", reg_num, capacity, load)
            else:
                v = Motorcycle("client", reg_num, capacity)

            self.list.append(v)
            self.update_tree()

        

    def update_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for v in self.list:
            if isinstance(v, Car):
                self.tree.insert("", "end", values=(v.reg_num, v.capacity, "Car", v.calculate_efficiency()))
            elif isinstance(v, Truck):
                self.tree.insert("", "end", values=(v.reg_num, v.capacity, "Truck", v.calculate_efficiency()))
            else:
                self.tree.insert("", "end", values=(v.reg_num, v.capacity, "Motorcycle", 'None'))

    def delete_vehicle(self):
        self.tree.delete(self.tree.selection()[0])

    def update_vehicle(self):
        if self.reg_entry.get():
            for v in self.list:
                if v.reg_num == self.reg_entry.get():
                    if self.type.get() == "Car":
                        consumption = float(input("Enter consumption: "))
                        v = Car("client", self.reg_entry.get(), int(self.capacity_entry.get()), consumption)
                    elif self.type.get() == "Truck":
                        load = float(input("Enter load: "))
                        v = Truck("client", self.reg_entry.get(), int(self.capacity_entry.get()), load)
                    else:
                        v = Motorcycle("client", self.reg_entry.get(), int(self.capacity_entry.get()))

                    self.update_tree()
                    break

        

        

        












app = app()
