from abc import ABC, abstractmethod
import re
class InvalidIP(Exception):
    pass

class network_component(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def function(self):
        pass

class IPV4(network_component):
    def __init__(self, ip):
        self.ip = ip

    def valid(self):
        ip = self.ip.split(".")
        if len(ip) != 4:
            raise InvalidIP("Invalid IP address")
        for i in ip:
            if not 0 <= int(i) <= 255:
                raise InvalidIP("Invalid IP address")
            
        return True
    
    def __str__(self):
        return self.ip
    
    def function(self):
        pass

    def info(self):
        return super().info()
    
    def get_class(self):
        ip_list = self.ip.split(".")
        if int(ip_list[0]) <= 127:
            return "A"
        elif int(ip_list[0]) <= 191:
            return "B"
        elif int(ip_list[0]) <= 223:
            return "C"
        elif int(ip_list[0]) <= 239:
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

    def id_reseau(self):
        ip_list = self.ip.split(".")
        if self.get_class() == "A":
            return ip_list[0] + '.0.0.0'
        elif self.get_class() == "B":
            return '.'.join(ip_list[:2]) + '.0.0'
        elif self.get_class() == "C":
            return '.'.join(ip_list[:3]) + '.0'
        else:
            return None
    
    def id_host(self):
        ip_list = self.ip.split(".")
        if self.get_class() == "A":
            return  '.'.join(self.ip.split(".")[1:])
        elif self.get_class() == "B":
            return '.'.join(self.ip.split(".")[2:])
        elif self.get_class() == "C":
            return ip_list[3]
        else:
            return None
    
    def host_num(self):
        if self.get_class() == 'A':
            return 16777214 # 2^24 - 2
        elif self.get_class() == 'B':
            return 65534 # 2^16 - 2
        elif self.get_class() == 'C':        
            return 254 # 2^8 - 2
        else:
            return None
        
    
    
class DNS(network_component):
    def __init__(self):
        self.register = []
        self.cache = []

    def add(self, domain, ip):
        try:
            if ip.valid() and re.match(r'^(www\.)?[a-zA-Z0-9\-]+\.[a-z]{2,3}$', domain):
                self.register.append({"domain": domain, "ip": ip.ip})
                self.cache.append({"domain": domain, "ip": ip.ip})
            else:
                raise InvalidIP("Invalid IP address or invalid domain")
            
        except:
            raise InvalidIP("Invalid IP address")
        
    def search(self, name):
        for i in self.register:
            if i["name"] == name:
                return i
        
    def delete(self, name):
        self.register.remove(self.search(name))

    def resolve(self, name):
        for i in self.cache:
            if i["name"] == name:
                return i
        return self.search(name)
    
    def clear_cache(self):
        self.cache = []

    def __str__(self):
        return self.register
    
    def show_register(self):
        for i in self.register:
            print(i)

    def show_cache(self):
        for i in self.cache:
            print(i)

    def info(self):
        return super().info()
    
    def function(self):
        return super().function()
    

class DHCP(network_component):
    def __init__(self):
        self.ip_pool = []
        self.assigned = []

    def add_ip(self, ip_list:list):
        for ip in ip_list:
            if ip.valid and ip not in self.ip_pool and ip not in self.assigned:
                self.ip_pool.append(ip.ip)

    def assign(self, ip):
        if ip in self.ip_pool and ip not in self.assigned:
            self.assigned.append(ip)
            self.ip_pool.remove(ip)
        else:  
            raise InvalidIP("Invalid IP address")
        

    def liberate(self, ip):
        if ip in self.assigned:
            self.assigned.remove(ip)
            self.ip_pool.append(ip)
        else:  
            raise InvalidIP("Invalid IP address")
        

    def __str__(self):
        return self.ip_pool

    def availible_ip(self):
        print('\n----availible ip----')
        for ip in self.ip_pool:
            print(ip)
        print('-------------------')

    def assigned_ip(self):
        print('\n----assigned ip----')
        for ip in self.assigned:
            print(ip)
        print('-------------------')

    def info(self):
        return super().info()
    
    def function(self):
        return super().function()






ip = IPV4("100.178.44.111")
print(ip.get_class())
print(ip.id_reseau())
print(ip.id_host())
print(ip.host_num())



"""dns = DNS()
dns.add("www.google.com", IPV4("244.178.44.111"))
dns.add("www.facebook.com", IPV4("244.178.44.111"))
dns.add("www.instagram.com", IPV4("244.178.44.111"))
dns.add("www.twitter.com", IPV4("244.178.44.111"))
dns.add("www.github.com", IPV4("244.178.44.111"))

dns.show_cache()
dns.show_register()
dns.clear_cache()
dns.add("www.youtube.com", IPV4("244.178.44.111"))
dns.show_cache()
dns.show_register()


dhcp = DHCP()
dhcp.add_ip([IPV4('1.1.1.1'), IPV4('2.2.2.2'), IPV4('3.3.3.3'), IPV4('4.4.4.4'), IPV4('5.5.5.5'), IPV4('6.6.6.6')])
dhcp.assign("1.1.1.1")
dhcp.assign('3.3.3.3')

dhcp.availible_ip()
dhcp.assigned_ip()
dhcp.liberate('1.1.1.1')
dhcp.availible_ip()
dhcp.assigned_ip()
            
        """