class Bot:
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        print("",len(self.name) * "#" ) 
        print("#"+self.name+"#")
        print("",len(self.name) * "#")

    def display_age(self):
        print("Age:",self.age)
    
    def display_energy(self):
        print("Energy level:", "#" * self.energy)
        
    def display_shield(self):
        print("Sheild level:", "#" * self.shield)
        
    def display_summary(self):
        self.display_name()
        self.display_age()
        self.display_energy()
        self.display_shield()
    
    def __str__(self):
        return self.name, self.age, self.energy, self.shield



