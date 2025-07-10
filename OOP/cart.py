class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = 0

    def __str__(self):
        return f"{self.id} {self.name} {self.price} {self.quantity}"
    def __eq__(self, id):
        return self.id == id
    def show(self):
        print(f"{self.name} {self.price}")

class cart:
    def __init__(self):
        self.products = []
    def add(self, product):
        product.quantity = 1
        for p in self.products:
            if p.id == product.id:
                p.quantity += 1
                return
        self.products.append(product)
        print("Product added successfully\n")

    def remove(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print("Product removed successfully\n")
                return
        print("Product not found")

    def increase(self, id):
        for product in self.products:
            if product.id == id:
                product.quantity += 1
                print(f"Quantity of {product.name} increased by One ")
                return

        

    def decrease(self, id):
        for product in self.products:
            if product.id == id and product.quantity > 0:
                product.quantity -= 1
                print(f"Quantity of {product.name} decreased by One ")
                return
        print("Product not found or quantity is 0")

    def total(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    
    def __str__(self):
        s = ""
        for product in self.products:
            s += f"{product.id} {product.name} {product.price} {product.quantity}\n"
        return s

    def menu(self):
        while True:
            print('-------------------------')
            print("1. Add product")
            print("2. Remove product")
            print("3. Increase quantity")
            print("4. Decrease quantity")
            print("5. Total")
            print("6. Show cart")
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
                    id = int(input("Enter product id: "))
                    name = input("Enter product name: ")
                    price = float(input("Enter product price: "))
                    product = Product(id, name, price)
                    self.add(product)
                case 2:
                    id = int(input("Enter product id: "))
                    self.remove(id)
                case 3:
                    id = int(input("Enter product id: "))
                    self.increase(id)
                case 4:
                    id = int(input("Enter product id: "))
                    self.decrease(id)
                case 5:
                    print(f"Total: {self.total()}$")
                case 6:
                    print(self)
                case 7:
                    print("Goodbye")
                    break
                case _:
                    print("Invalid choice")

sss = cart()
sss.add(Product(1, "a", 10))
sss.add(Product(2, "b", 20))
sss.add(Product(3, "c", 30))
sss.add(Product(4, "d", 40))
sss.add(Product(5, "e", 50))
sss.add(Product(6, "f", 60))
sss.increase(3)
sss.menu()
