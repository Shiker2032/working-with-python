# task 1
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
            return f"Capacity of one bus {self.name}  {capacity} passengers"
    def info (self):
        return f"{self.name} Speed: {self.max_speed} Mileage: {self.mileage}"

autobus = Transport ("Renault Logan", 180, 12)
print(autobus.info())

# task 2
class Autobus (Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    def seating_capacity(self, capacity = 50):
        return f"Capacity of one bus {self.name}  {capacity} passengers"
    
renault2 = Autobus ("renault Logan", 120, 12)
print(renault2.seating_capacity())
