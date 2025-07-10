import re
class FormatInvalid(Exception):
    pass
class DomainNonExistant(Exception):
    pass
class DomainAlreadyExists(Exception):
    pass

class dns:
    def __init__(self):
        self.register = {}
        self.domains = []
        self.journal = []
        
    
    def add(self, name, ip):
        if not re.match(r'^(www\.)?[a-zA-Z0-9\-]+\.[a-z]{2,3}$', name):
            raise FormatInvalid("Invalid name")
        
        ip_list = ip.split(".")
        if len(ip_list) != 4:
            raise FormatInvalid("Invalid IP address")
        for i in ip_list:
            if not 0 <= int(i) <= 255:
                raise FormatInvalid("Invalid IP address")
            
        for i in self.register.keys():
            if i == name:
                raise DomainAlreadyExists("Name already exists")
        
        self.register = {'name': name, 'ip': ip}
        self.Domains.append(self.register)
        print(f"\nAdded {name} with IP {ip}\n")
        self.journal.append(f"Added {name} with IP {ip}")

    def search(self, name):
        for i in self.Domains:
            if i['name'] == name:
                print(f"\nName: {name}    IP: {i['name']}\n")
                return self.Domains.index(i)
        raise DomainNonExistant("Name does not exist")
            
    def update_ip(self, name, ip):
        if self.search(name) == None:
            raise DomainNonExistant("Name does not exist")
        else:
            self.Domains[self.search(name)]['ip'] = ip
            self.journal.append(f"Updated {name} with IP {ip}")

    def delete(self, name):
        if self.search(name) == None:
            raise DomainNonExistant("Name does not exist")
        else:
            self.Domains.pop(self.search(name))
            self.journal.append(f"Deleted {name}")

    def show_Domains(self):
        print('')
        return self.Domains
        
    
    def run(self):
        while True:
            print('********************************')
            print("1. Add domain")
            print("2. Search domain")
            print("3. Update domain IP")
            print("4. Delete domain")
            print("5. Show Domains")
            print("6. Show Journal")
            print("7. Clear Journal")
            print("8. Exit")
            print('********************************')
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter name: ")
                ip = input("Enter IP: ")
                self.add(name, ip)
            elif choice == 2:
                name = input("Enter name: ")
                self.search(name)
            elif choice == 3:
                name = input("Enter name: ")
                ip = input("Enter IP: ")
                self.update_ip(name, ip)
            elif choice == 4:
                name = input("Enter name: ")
                self.delete(name)
            elif choice == 5:
                print(self.show_Domains())
            elif choice == 6:
                print(self.journal)
            elif choice == 7:
                self.journal = []
            elif choice == 8:
                break

DNS1 = dns()
DNS1.add("www.google.com", "244.178.44.111")
DNS1.add("www.facebook.com", "244.178.44.111")
DNS1.add("www.instagram.com", "244.178.44.111")
DNS1.add("www.twitter.com", "244.178.44.111")
DNS1.add("www.github.com", "244.178.44.111")
DNS1.add("www.youtube.com", "244.178.44.111")

DNS1.run()