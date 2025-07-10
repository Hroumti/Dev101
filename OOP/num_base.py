

class converter:
    def __init__(self, num):
        self.num = num
    
    def get_base(self):
        if (self.num.startswith("0b") or self.num.startswith("0B")):
            return 2
        elif (self.num.startswith("0o") or self.num.startswith("0O")):
            return 8
        elif (self.num.startswith("0x") or self.num.startswith("0X")):
            return 16
        try:
            int(self.num)
            return 10
        except:
            return None
    def convert(self, base):
        if not self.get_base():
            return None
        if base == self.get_base():
            return self.num
        elif base == 10:
            return str(int(self.num, self.get_base()))
        elif base == 2:
            return str(bin(int(self.num, self.get_base())))
        elif base == 8:
            return str(oct(int(self.num, self.get_base())))
        else:
            return str(hex(int(self.num, self.get_base())))
        
        


c = converter("0x65")
print(c.get_base())
print(c.convert(2))
print(bin(0x65))