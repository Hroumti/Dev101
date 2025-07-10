import json
class StockInvalid(Exception):
    pass
class equipement:
    def __init__(self, id,name, price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.id} {self.name} {self.price} {self.quantity}"
    def __eq__(self, value):
        return self.id == value
    
class storage:
    def __init__(self):
        self.equipements = []

    def add(self, equipement):
        for e in self.equipements:
            if e.id == equipement.id:
                print("Equipement already exists")
                return
        self.equipements.append(equipement)
        print("Equipement added successfully")
    
    def remove(self, id):
        for e in self.equipements:
            if e.id == id:
                self.equipements.remove(e)
                print("Equipement removed successfully")
                return
        print("Equipement not found")

    def modify_quantity(self, id, quantity):
        if quantity < 0:
            raise StockInvalid
        for e in self.equipements:
            if e.id == id:
                e.quantity = quantity
                print("Equipement quantity modified successfully")
                return
        print("Equipement not found")
    def search(self, id):
        for e in self.equipements:
            if e.id == id:
                print(e)
                return
            
    def serialize(self):
        data = []
        for e in self.equipements:
            data.append(e.__dict__)
            print(e.__dict__)
        with open("equipements.json", "w") as f:
            json.dump(data, f)
        print("Equipements serialized successfully")

    def __str__(self):
        s = ""
        for e in self.equipements:
            s += str(e) + "\n"
        return s

    def menu(self):
        while True:
            print('-------------------------')
            print("1. Add equipement")
            print("2. Remove equipement")
            print("3. Modify quantity")
            print("4. Search equipement")
            print("5. Show equipements")
            print("6. Serialize equipements")
            print("7. Exit")
            print('-------------------------')
            try:
                x = int(input("Enter your choice: "))
            except:
                print("Invalid choice")
                continue
            print('-------------------------')
            match x:
                case 1:
                    id = int(input("Enter equipement id: "))
                    name = input("Enter equipement name: ")
                    price = float(input("Enter equipement price: "))
                    quantity = int(input("Enter equipement quantity: "))
                    equipement = equipement(id, name, price, quantity)
                    self.add(equipement)
                case 2:
                    id = int(input("Enter equipement id: "))
                    self.remove(id)
                case 3:
                    id = int(input("Enter equipement id: "))
                    quantity = int(input("Enter equipement quantity: "))
                    self.modify_quantity(id, quantity)
                case 4:
                    id = int(input("Enter equipement id: "))
                    self.search(id)
                case 5:
                    print(self)
                case 6:
                    self.serialize()
                case 7:
                    break
                case _:
                    print("Invalid choice")
    
sss = storage()
sss.add(equipement(1, "a", 10, 10))
sss.add(equipement(2, "b", 20, 25))
sss.add(equipement(3, "c", 30, 13))
sss.add(equipement(4, "d", 40, 64))

sss.menu()
            