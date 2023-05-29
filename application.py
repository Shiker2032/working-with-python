import math

#task 1
n = int(input("input n"))
if ((n >= 1) and (n <= 100000)):
    tmp = []
    for i in range (n):
        tmp.append(input("input a number"))
    tmp.reverse()
    print(*tmp)
else:
    print("range should start from 1 and be less than 100 000")

# task 2 
n2 = int(input("input n "))
tmp2 = []
if (n2 < 0) or (n2 > 100000):
    print("range should start from 1 and be less than 100 000")
else:
    tmp2 = list(map(int, input().split()))    
    tmp2.insert(0,tmp2[-1])
    tmp2.pop()  
    print(tmp2)

# task 3
maxBoatMass = int(input("Input max boat mass capacity "))
fishersCount = int(input("Input fishers amount "))
boatsRequired = 1
currentBoatMass = 0
totalMass = 0
fishers = []

class Fisher:
    def __init__(self, mass):
        self.mass = int(mass)

for i in range (fishersCount):
    fishers.append(Fisher(input("input fisher mass ")))

for i, fisher in enumerate(fishers):
    if (fisher.mass <= maxBoatMass):    
        totalMass += fisher.mass
    else:
        print('fisher {0} will have to wait for bigger boat'.format(int(i + 1)))
boatsRequired = math.ceil(totalMass / maxBoatMass)
print(boatsRequired)