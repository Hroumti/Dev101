import tkinter as tk
from tkinter import END, messagebox
import ttkbootstrap as ttk
from abc import ABC, abstractmethod
import math

class InvalidBudgetError(Exception):
    pass

class NotImplementedError(Exception):
    pass

class AdCampain(ABC):
    def __init__(self, name, budget, channel):
        self.name = name
        self.budget = budget
        self.channel = channel

    @abstractmethod
    def calculate_range(self):
        raise NotImplementedError
    def show_details(self):
        print(f"Name: {self.name}\tBudget: {self.budget}\tChannel: {self.channel}")

    def __str__(self):
        return f"Name: {self.name}\tBudget: {self.budget}\tChannel: {self.channel}"

    def __eq__(self, value):
        return self.campaign_name == value and self.channel == value and self.budget == value
    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 0:
            raise InvalidBudgetError("Budget cannot be negative")
        self._budget = value

class GoogleAdCampain(AdCampain):
    def __init__(self, name, budget, channel, cpc):
        super().__init__(name, budget, channel)
        self.cpc = cpc

    def calculate_range(self):
        return self.budget / self.cpc
    
    
class FacebookAdCampain(AdCampain):
    def __init__(self, name, budget, channel, cpm):
        super().__init__(name, budget, channel)
        self.cpm = cpm

    def calculate_range(self):
        return (self.budget / self.cpm) * 1000
    
class YoutubeAdCampain(AdCampain):
    def __init__(self, name, budget, channel, cpv):
        super().__init__(name, budget, channel)
        self.cpv = cpv

    def calculate_range(self):
        return self.budget / self.cpv


update_value=False
def submit():
    global update_value

    name = name_entry.get() 
    try:
        budget = float(budget_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the budget")
        return
    if budget <= 0:
        messagebox.showerror("Error", "Budget cannot be negative")
    channel = channel_entry.get()
    type = type_entry.get()
    if type == "Google":
        cpc = float(input("Enter CPC: "))
        campain = GoogleAdCampain(name, budget, channel, cpc)
    elif type == "Facebook":
        cpm = float(input("Enter CPM: "))
        campain = FacebookAdCampain(name, budget, channel, cpm)
    elif type == "Youtube":
        cpv = float(input("Enter CPV: "))
        campain = YoutubeAdCampain(name, budget, channel, cpv)
    else :
            raise NotImplementedError("Ad type not implemented")
    if not update_value:
        tree.insert("", "end", values=(name, budget, channel, type, round(campain.calculate_range(),2)))
    else:
        tree.item(tree.selection()[0], values=(name, budget, channel, type, round(campain.calculate_range(),2)))
        update_value=False



def delete():
    selected_item = tree.selection()[0]
    tree.delete(selected_item)

def update_form_fields():
    item = tree.selection()[0]
    name_entry.delete(0, END)
    name_entry.insert(0, tree.item(item)["values"][0])
    budget_entry.delete(0, END)
    budget_entry.insert(0, tree.item(item)["values"][1])
    channel_entry.delete(0, END)
    channel_entry.insert(0, tree.item(item)["values"][2])
    type_entry.delete(0, END)
    type_entry.insert(0, tree.item(item)["values"][3])

def on_double_click(event):
    global update_value
    update_value=True
    update_form_fields()
    

    


root = ttk.Window(themename="superhero")
root.title("Ad Campain")

ttk.Label(root, text="Ad Campain", font=("Arial", 40,'italic')).pack(pady=10,padx=10)
frame1 = ttk.Frame(root)
frame1.pack()

ttk.Label(frame1, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = ttk.Entry(frame1)
name_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(frame1, text="Budget").grid(row=1, column=0, padx=10, pady=10)
budget_entry = ttk.Entry(frame1)
budget_entry.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(frame1, text="Channel").grid(row=2, column=0, padx=10, pady=10)
channel_entry = ttk.Entry(frame1)
channel_entry.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(frame1, text="Type").grid(row=3, column=0, padx=10, pady=10)
type_entry = ttk.Combobox(frame1, values=["Google", "Facebook", "Youtube", "Influencer"])
type_entry.grid(row=3, column=1, padx=10, pady=10)


ttk.Button(frame1, text="Submit", command= submit).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
ttk.Button(frame1, text="Delete", command=delete).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

tree = ttk.Treeview(root, columns=("name", "budget", "channel", "type", "estimated range"), show="headings")
tree.heading("name", text="Name")
tree.heading("budget", text="Budget")
tree.heading("channel", text="Channel")
tree.heading("type", text="Type")
tree.heading("estimated range", text="Estimated Range")

tree.pack()
tree.bind("<Double-1>", on_double_click)





ads = [
    GoogleAdCampain("Ad 1", 1000, "Google", 0.1), 
    GoogleAdCampain("Ad 2", 2000, "Google", 0.2),
    GoogleAdCampain("Ad 3", 3000, "Google", 0.3),
    FacebookAdCampain("Ad 4", 4000, "Facebook", 0.4),
    FacebookAdCampain("Ad 5", 5000, "Facebook", 0.5),
    FacebookAdCampain("Ad 6", 6000, "Facebook", 0.6),
    YoutubeAdCampain("Ad 7", 7000, "Youtube", 0.7),
    YoutubeAdCampain("Ad 8", 8000, "Youtube", 0.8),
    YoutubeAdCampain("Ad 9", 9000, "Youtube", 0.9)]
for ad in ads:
    tree.insert("", "end", values=(ad.name, ad.budget, ad.channel, ad.channel, round(ad.calculate_range(), 2)))

root.mainloop()