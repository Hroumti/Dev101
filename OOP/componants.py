import json
import csv



class componant:
    def __init__(self, id:int, name:str, brand:str, price:float):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
    
    def show_details(self):
        print(f"\nID: {self.id}\tName: {self.name}\tBrand: {self.brand}\tPrice: {self.price}")

    def modify(self, name=None, brand=None, price=None):
        if name is not None:
            self.name = name
        if brand is not None:
            self.brand = brand
        if price is not None:
            self.price = price
        

    def __str__(self):
        return f"\nID: {self.id}\tName: {self.name}\tBrand: {self.brand}\tPrice: {self.price}"

class CPU(componant):
    def __init__(self, id, name, brand, price, frequency:float, cores:int):
        super().__init__(id, name, brand, price)
        self.frequency = frequency
        self.cores = cores
        if self.frequency < 0 or self.cores < 1:
            raise ValueError
        
    def show_details(self):
        print(super().__str__() + f"\tFrequency: {self.frequency}\tCores: {self.cores}")
    
    def modify(self, name=None, brand=None, price=None, frequency=None, cores=None):
        super().modify(name, brand, price)
        if frequency is not None:
            self.frequency = frequency
        if cores is not None:
            self.cores = cores

    def __str__(self):
        return super().__str__() + f"\tFrequency: {self.frequency}\tCores: {self.cores}"
        
class RAM(componant):
    def __init__(self, id, name, brand, price, capacity:int, type:str):
        super().__init__(id, name, brand, price)
        self.capacity = capacity
        self.type = type
        if self.capacity < 0 or self.type not in ["DDR3", "DDR4", "DDR5"]:
            raise ValueError
        
    def show_details(self):
        print(super().__str__() + f"\tCapacity: {self.capacity}\tType: {self.type}")
    
    def modify(self, name=None, brand=None, price=None, capacity=None, type=None):
        super().modify(name, brand, price)
        if capacity is not None:
            self.capacity = capacity
        if type in ["DDR3", "DDR4", "DDR5"]:
            self.type = type
        elif type is not None:
            raise ValueError("Invalid RAM type")
        
    def __str__(self):
        return super().__str__() + f"\tCapacity: {self.capacity}\tType: {self.type}"
    
class mother_board:
    def __init__(self, name,ram_slots:int,price:float):
        self.name = name
        self.ram_slots = ram_slots
        self.price = price
        self.componants = []
        if ram_slots < 2:
            raise ValueError

    def add_componant(self, c):
        if isinstance(c, CPU):
            for componant in self.componants:
                if componant.__class__ == c.__class__:
                    raise ValueError("CPU already exists")
            self.componants.append(c)
        elif isinstance(c, RAM):
            rams = [componant for componant in self.componants if componant.__class__ == c.__class__]
            if len(rams) >= self.ram_slots:
                raise ValueError("No more RAM slots available")
            self.componants.append(c)

    def find_componant(self, id):
        for componant in self.componants:
            if componant.id == id:
                return componant

    def remove_componant(self, id):
        componant = self.find_componant(id)
        if componant:
            self.componants.remove(componant)
    
    def upgrade_componant(self, id, c):
        componant = self.find_componant(id)
        if componant:
            if componant.__class__ == c.__class__:
                self.componants.remove(componant)
                self.componants.append(c)
                return
            else:
                raise TypeError("Invalid componant type")
        
        raise ValueError("Componant not found")
    
    def show_details(self):
        print(f"Motherboard: {self.name}")
        print(f"RAM slots: {self.ram_slots}")
        for componant in self.componants:
            print(componant)

    def filter_componants(self, criteria=("CPU", "RAM")):
        filtered_componants = []
        for componant in self.componants:
            if componant.__class__.__name__ in criteria:
                filtered_componants.append(componant)
        return filtered_componants
    
    def total_price(self):
        return self.price + sum(componant.price for componant in self.componants)
    
    def search_by_name(self, name):
        for componant in self.componants:
            if componant.name == name:
                return componant
            
        return None
    
    def serialize(self):
        mother_board_json = {
            "name": self.name,
            "ram_slots": self.ram_slots,
            "price": self.total_price(),
            "componants": [componant.__dict__ for componant in self.componants]
        }
        file_name = self.name.replace(" ", "_") + ".json"
        with open(file_name, "w") as f:
            json.dump(mother_board_json, f)
        print("Motherboard serialized successfully")

    def deserialize(self, file_name):
        with open(file_name, "r") as f:
            mother_board_json = json.load(f)
        self.name = mother_board_json["name"]
        self.ram_slots = mother_board_json["ram_slots"]
        self.price = mother_board_json["price"]
        self.componants = [componant for componant in mother_board_json["componants"]]

        print("Motherboard deserialized successfully")

    def save_csv(self):
        filename = self.name.replace(" ", "_") + ".csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for componant in self.componants:
                writer.writerow(componant.__dict__.values())
        print("Componants saved successfully")


        
mother_board = mother_board("Motherboard", 4, 500)
mother_board.add_componant(CPU(1, "CPU", "Intel", 500, 3.5, 4))
mother_board.add_componant(RAM(2, "RAM", "Corsair", 100, 8, "DDR4"))
mother_board.add_componant(RAM(3, "RAM", "Corsair", 100, 8, "DDR4"))
mother_board.add_componant(RAM(4, "RAM", "Corsair", 100, 8, "DDR4"))

mother_board.remove_componant(2)
mother_board.upgrade_componant(1, CPU(1, "CPU", "Intel", 500, 4.2, 8))

mother_board.show_details()

mother_board.serialize()