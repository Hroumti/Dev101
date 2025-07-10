

class IPv4:
    def __init__(self, ip):
        self.ip = ip
        self.ip_list = ip.split(".")

        if len(self.ip_list) != 4:
            raise ValueError("Invalid IP address")

        for i in self.ip_list:
            if not 0 <= int(i) <= 255:
                raise ValueError("Invalid IP address")
            
        self.mask = self.get_mask()
        self.clss = self.get_class()

    def __str__(self):
        return f"IP address: {self.ip}\nClass: {self.clss}\nMask: {self.mask}"
    
    def get_class(self):
        if int(self.ip_list[0]) <= 127:
            return "A"
        elif int(self.ip_list[0]) <= 191:
            return "B"
        elif int(self.ip_list[0]) <= 223:
            return "C"
        elif int(self.ip_list[0]) <= 239:
            return "D"
        else:
            return "E"
        
    def get_mask(self):
        
        if self.get_class() == "A":
            return "255.0.0.0"
        elif self.get_class() == "B":
            return "255.255.0.0"
        elif self.get_class() == "C":
            return "255.255.255.0"
        else:
            return "None"
        

ip = IPv4("128.84.244.178")
print(ip)
