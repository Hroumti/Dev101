from abc import ABC, abstractmethod
from datetime import datetime

class InvalidDateError(Exception):
    pass
class InvalidHeightError(Exception):
    pass
class InvalidDroughtResistanceError(Exception):
    pass

class plant(ABC):
    def __init__(self, name:str, plant_type:str, last_irrigation_date:str, needs_irrigation:bool = False):
        self.name = name
        self.plant_type = plant_type
        self.last_irrigation_date = datetime.strptime(last_irrigation_date, "%d/%m/%Y")
        self.needs_irrigation = needs_irrigation
        
        if self.last_irrigation_date > datetime.now():
            raise InvalidDateError("The last irrigation date cannot be in the future")
        
    def __str__(self):
        return f"\nName: {self.name}\tPlant type: {self.plant_type}\tLast irrigation date: {self.last_irrigation_date}\tNeeds irrigation: {self.needs_irrigation}"
    @abstractmethod
    def plant_needs_irrigation(self):
        pass

class flower(plant):
    def __init__(self, name:str, plant_type:str, last_irrigation_date:str, needs_irrigation:bool = False):
        super().__init__(name, plant_type, last_irrigation_date, needs_irrigation)
        if self.plant_needs_irrigation():
            self.needs_irrigation = True
    def plant_needs_irrigation(self):
        if (datetime.now() - self.last_irrigation_date).days >= 7:
            return True
        else:
            return False
        
        

class tree(plant):
    def __init__(self, name:str, plant_type:str, last_irrigation_date:str,height:float, needs_irrigation:bool = False):
        super().__init__(name, plant_type, last_irrigation_date, needs_irrigation)
        self.height = height
        if height < 0 or height > 10:
            raise InvalidHeightError('Height must be between 0 and 10 meters')
        if self.plant_needs_irrigation():
            self.needs_irrigation = True
    def plant_needs_irrigation(self):
        if (self.height < 3 and (datetime.now() - self.last_irrigation_date).days >= 15) or ((datetime.now() - self.last_irrigation_date).days >= 30):
            return True
        else:
            return False
        
    def __str__(self):
        return f'{super().__str__()}\tHeight: {self.height}\t'
        
class cactus(plant):
    def __init__(self, name:str, plant_type:str, last_irrigation_date:str, drought_resistance:int, needs_irrigation:bool = False):
        super().__init__(name, plant_type, last_irrigation_date, needs_irrigation)
        self.drought_resistance = drought_resistance
        if drought_resistance < 0 or drought_resistance > 10:
            raise InvalidDroughtResistanceError('Drought resistance must be between 0 and 10')
        self.needs_irrigation=self.plant_needs_irrigation()
    def plant_needs_irrigation(self):
        irrigation_cycle = self.drought_resistance * 4.2
        if (datetime.now() - self.last_irrigation_date).days >= irrigation_cycle:
            return True
        else:
            return False
        
    def __str__(self):
        return f'{super().__str__()}\tDrought resistance: {self.drought_resistance}\t'
        
class nursery:
    def __init__(self, name:str):
        self.name = name
        self.plants = []
    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"\tAdded {plant.name} to the nursery\t")

    def search_plant(self, name):
        for i in self.plants:
            if i.name == name:
                return i

    def modify_plant(self,name,criteria,new_value):
        plant = self.search_plant(name)
        if plant == None:
            raise ValueError("Plant not found")
        if criteria == "last_irrigation_date":
            plant.last_irrigation_date = new_value
        elif criteria == "needs_irrigation":
            plant.needs_irrigation = new_value
        else:
            raise ValueError("Invalid criteria")
        
        print(f"\tModified {plant.name}'s {criteria} to {new_value}\t")

    def remove_plant(self, name):
        plant = self.search_plant(name)
        if plant == None:
            raise ValueError("Plant not found")
        self.plants.remove(plant)
        print(f"\tRemoved {plant.name} from the nursery\t")

    def plants_in_need_of_irrigation(self):
        result = [plant for plant in self.plants if plant.needs_irrigation]
        for i in result:
            print(i)
        return result
    


n = nursery("My Nursery")
n.add_plant(flower("Rose", "flower", "01/01/2025"))
n.add_plant(tree("Pine Tree", "tree", "01/01/2025", 5))
n.add_plant(cactus("Cactus", "cactus", "01/01/2024", 5))
n.add_plant(flower("Sunflower", "flower", "01/01/2025"))
n.add_plant(cactus("Cactus2", "cactus", "01/01/2025", 10))
n.add_plant(tree("zzz", "zzz", "01/10/2024",9))

n.modify_plant("Rose", "last_irrigation_date", "01/01/2025")
n.remove_plant("Pine Tree")

n.plants_in_need_of_irrigation()

