import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox

class PCPrice:
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.title("PC price")
        self.root.resizable('false','false')

        self.display()
        self.root.mainloop()
    
    def display(self):
        self.frame_1 = ttk.Frame(self.root)
        self.frame_2 = ttk.Frame(self.root)
        self.frame_3 = ttk.Frame(self.root)
        self.frame_4 = ttk.Frame(self.root)
        self.frame_5 = ttk.Frame(self.root)
        self.frame_6 = ttk.Frame(self.root)
        self.frame_7 = ttk.Frame(self.root)
        self.frame_8 = ttk.Frame(self.root)
        self.frame_9 = ttk.Frame(self.root)

        self.frame_1.grid(row=0, column=0, padx=10, pady=10)
        self.frame_2.grid(row=0, column=1, padx=10, pady=10)
        self.frame_3.grid(row=0, column=2, padx=10, pady=10)
        self.frame_4.grid(row=1, column=0, padx=10, pady=10)
        self.frame_5.grid(row=1, column=1, padx=10, pady=10)
        self.frame_6.grid(row=1, column=2, padx=10, pady=10)
        self.frame_7.grid(row=2, column=0, padx=10, pady=10)
        self.frame_8.grid(row=2, column=2, padx=10, pady=10)
        self.frame_9.grid(row=3, columnspan=3, padx=10, pady=10)

        ttk.Label(self.frame_1, text="Mother board").pack(padx=10,pady=10)
        ttk.Label(self.frame_2, text="CPU").pack(padx=10,pady=10)
        ttk.Label(self.frame_3, text="GPU").pack(padx=10,pady=10)
        ttk.Label(self.frame_4, text="RAM").pack(padx=10,pady=10)
        ttk.Label(self.frame_5, text="condition").pack(padx=10,pady=10)
        ttk.Label(self.frame_6, text="Screen resolution").pack(padx=10,pady=10)
        ttk.Label(self.frame_7, text="Other options").pack(padx=10,pady=10)
        ttk.Label(self.frame_8, text="Discounts").pack(padx=10,pady=10)

        self.mb = tk.StringVar()
        self.cpu = tk.StringVar()
        self.gpu = tk.StringVar()
        self.ram = tk.StringVar()
        self.condition = tk.StringVar()
        self.screen = tk.StringVar()
        self.other1 = tk.IntVar()
        self.other2 = tk.IntVar()
        self.other3 = tk.IntVar()
        self.discount = tk.StringVar()

        ttk.Radiobutton(self.frame_1, text="GIGABYTE Z390 UD (89.00$)", variable=self.mb, value="89.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_1, text="ASUS Prime Z390-P (103.00$)", variable=self.mb, value="103.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_1, text="ASUS ROG Strix B650E-F (160.00$)", variable=self.mb, value="160.00").pack(padx=10,pady=10)

        ttk.Radiobutton(self.frame_2, text="Intel Core i9-14900K (433.00$)", variable=self.cpu, value="433.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_2, text="Intel Core i5-14600K (209.00$)", variable=self.cpu, value="209.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_2, text="AMD Ryzen 9 7950X3D (690.00$)", variable=self.cpu, value="690.00").pack(padx=10,pady=10)

        ttk.Radiobutton(self.frame_3, text="GeForce RTX 4070 (489.00$)", variable=self.gpu, value="489.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_3, text="Radeon RX 7900 XTX (819.00$)", variable=self.gpu, value="819.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_3, text="GeForce RTX 4090 (1599.00$)", variable=self.gpu, value="1599.00").pack(padx=10,pady=10)

        ttk.Radiobutton(self.frame_4, text="CMS 16GB (71.00$)", variable=self.ram, value="71.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_4, text="Corsair Vengeance RGB PRO 32GB DDR4 (185.00$)", variable=self.ram, value="185.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_4, text="HyperX Fury 64GB DDR4 (250.00$)", variable=self.ram, value="250.00").pack(padx=10,pady=10)


        ttk.Radiobutton(self.frame_5, text="NEW parts", variable=self.condition, value="0").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_5, text="USED parts", variable=self.condition, value="0.3").pack(padx=10,pady=10)

        ttk.Radiobutton(self.frame_6, text="1920x1080 (79.00$)", variable=self.screen, value="79.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_6, text="2560x1440 (109.00$)", variable=self.screen, value="109.00").pack(padx=10,pady=10)
        ttk.Radiobutton(self.frame_6, text="3840x2160 (199.00$)", variable=self.screen, value="199.00").pack(padx=10,pady=10)

        ttk.Checkbutton(self.frame_7, text="Webcam (69.00$)", variable=self.other1).pack(padx=10,pady=10)
        ttk.Checkbutton(self.frame_7, text="Gaming keyboard (49.00$)", variable=self.other2).pack(padx=10,pady=10)
        ttk.Checkbutton(self.frame_7, text="Gaming mouse (39.00$)", variable=self.other3).pack(padx=10,pady=10)


        ttk.Combobox(self.frame_8, textvariable=self.discount, values=['None','Student','Employee']).pack(padx=10,pady=10)

        ttk.Button(self.frame_9, text="Calculate", width=30,command=self.calculate).pack(padx=10,pady=30)
        self.price = ttk.Label(self.frame_9, text = 'Total price : __.__$', font=('Arial',20))
        self.price.pack(padx=10,pady=10)

    def calculate(self):
        try:
            mb = float(self.mb.get())
            cpu = float(self.cpu.get())
            gpu = float(self.gpu.get())
            ram = float(self.ram.get())
            condition = float(self.condition.get())
            screen = float(self.screen.get())
            discount = self.discount.get()

            total_price = mb + cpu + gpu + ram + screen

            total_price = total_price - (total_price * condition)

            if self.other1.get():
                total_price = total_price + 69.00
            if self.other2.get():
                total_price = total_price + 49.00
            if self.other3.get():
                total_price = total_price + 39.00

            if discount == 'Employee':
                total_price = total_price - (total_price * 0.2)
            elif discount == 'Student':
                total_price = total_price - (total_price * 0.1)

            self.price.config(text = f'Total price : {total_price:.2f}$')

        except:
            messagebox.showerror("Error", "Please fill all the fields")

app = PCPrice()