class Bot:
    def __init__(self, name, age, energy, sheild):
        self.name = name
        self.age = age
        self.energy = energy
        self.sheild = sheild

    def display_name(self):
        print("",len(self.name) * "#" ) 
        print("#"+self.name+"#")
        print("",len(self.name) * "#")

    def display_age(self):
        print("Age:",self.age)
    
    def display_energy(self):
        print("Energy level:", "#" * self.energy)
        
    def display_sheild(self):
        print("Sheild level:", "#" * self.sheild)
        
    def display_summary(self):
        self.display_name()
        self.display_age()
        self.display_energy()
        self.display_sheild()
    
    def __str__(self):
        return self.name, self.age, self.energy, self.sheild

bot1 = Bot("bot" , 35, 10, 10)

bot1.display_name()
bot1.display_age()
bot1.display_energy()
bot1.display_sheild()
bot1.display_summary()
print(bot1.__str__())

