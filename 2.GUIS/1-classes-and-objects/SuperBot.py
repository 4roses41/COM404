from bot import Bot

class SuperBot:
    def __init__(self, name, age, energy, shield, super_power):
        self.name = name
        self.age = age
        self.energy = energy
        self.sheild = shield
        self.super_power = super_power
    def display_super_power(self):
        print(self.super_power)

