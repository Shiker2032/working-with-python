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
# task 1

class CashRegister (object):
    def __init__ (self, cash = 0):
        self.cash = cash
    def topUp (self, x):
        self.cash += x
    def takeAway (self, x):        
        if (self.cash - x <= 0):            
            raise Exception ("Not enough money in the cash register")
        self.cash -= x
    def countThousands (self):
        return self.cash // 1000

cashReg = CashRegister(100)
try:
    cashReg.takeAway(500)
except Exception as e:print(e)

# task 2

class Turtle (object):
    def __init__(self, x = 0, y = 0, s = 2):
        self.x = x
        self.y = y
        self.s = s
    def goUp (self):
        self.y += self.s

    def goDown (self):
        self.y -= self.s

    def goLeft (self):
        self.x -= self.s

    def goRight (self):
        self.x += self.s

    def printInfo (self):
        print(f"x:{self.x}, y:{self.y}, s: {self.s}")

    def evolve (self):
        self.s += 1

    def degrade (self):
        if (self.s - 1 <= 0):
            raise Exception ("The movement of squares cannot be less than 1")
        self.s -= 1

    def countMoves (self, x2, y2):
        if (x2 % self.s !=0) or (y2 % self.s !=0):
            raise Exception ("Impossible to reach the destination with the current square movement")
        steps = 0
        while (self.x != x2):
            if (self.x < x2):
                self.x += self.s
            else:
                self.x -= self.s
            steps += 1        
        while (self.y != y2):
            if (self.y < y2):
                self.y += self.s
            else:
                self.y -= self.s
            steps += 1
        print("total moves:", steps)
        
            

turtle = Turtle (0, 0, 2)
try:
    turtle.goUp()
    turtle.goRight()
    turtle.printInfo()

    turtle.goDown()
    turtle.goLeft()
    turtle.printInfo()

    turtle.evolve()
    turtle.printInfo()

    turtle.degrade()
    turtle.printInfo()

    turtle.countMoves(3, 1)

        
except Exception as e: print(e)

