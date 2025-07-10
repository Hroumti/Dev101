from datetime import datetime
from datetime import timedelta
import re
class FormatInvalid(Exception):
    pass
class TimeInvalid(Exception):
    pass
class Employee:
    def __init__(self, id, name, salary, birth_date, start_date):
        self.id = id
        self.name = name
        self.salary = salary
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        if self.start_date > datetime.now():
            raise TimeInvalid("Start date cannot be in the future")
        if self.birth_date > datetime.now():
            raise TimeInvalid("Birth date cannot be in the future")
        if (self.start_date - self.birth_date).days < 24 * 365: 
            raise TimeInvalid("Employee must be at least 24 years old")
    
    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nSalary: {self.salary}\nStart date: {self.start_date.strftime('%d/%m/%Y')}\nBirth date: {self.birth_date.strftime('%d/%m/%Y')}"   
    
    def __eq__(self, value):
        return self.name == value
    
    def seniority(self):
        today = datetime.now()
        return today.year - self.start_date.year - ((today.month, today.day) < (self.start_date.month, self.start_date.day))
    
    def age(self):
        today = datetime.now()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        
    def retirement(self,retirement_age = 60):
        time = retirement_age - self.age()
        return self.start_date + timedelta(days=time * 365)
    
ss = Employee(1, "John Doe", 1000, "01/01/1990", "01/01/2016")
print(ss)
print('')
print(ss.age())
print('')
print(ss.seniority())
print('')
print(ss.retirement())
