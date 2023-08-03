#0 - Field
#1 - Tree
#2 - River
#3 - Hospital
#4 - Upgrade shop
#5 - Fire

from utils import randbool, randcell, randcell2

CELL_TYPES = "🟩🌳🌊🏥🛒🔥🚁"
TREE_BONUS = 100
UPGRADE_COST = 300
LIFE_COST = 500

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generateForest(3, 10)
        self.generateRiver(10)
        self.generateRiver(10)
        self.generateUpgradeShop()
        self.generateHospital()

    def checkBounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
    
    def printMap(self, helico):
        print("⬛" * (self.w + 2))
        for ri in range(self.h):
            print("⬛", end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (helico.x == ri and helico.y == ci):
                    print("🚁", end="")
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("⬛")
        print("⬛" * (self.w + 2))

    def generateRiver(self, l):
        rc = randcell(self.w, self.h)
        rx = rc[0]
        ry = rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.checkBounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generateTree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1


    def generateUpgradeShop(self):
      c = randcell(self.w, self.h)
      cx, cy = c[0], c[1]
      self.cells[cx][cy] = 4

    def generateHospital(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else: self.generateHospital()

    def generateForest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w) :
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1                    



    def addFire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def updateFires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (cell == 5):
                    self.cells[ri][ci] = 0
        for i in range(7):
            self.addFire()

    def processHelicopter(self, helico):
        c = self.cells[helico.x][helico.y]
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if (c == 4 and helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST

        if (c == 3 and helico.score >= LIFE_COST):
            helico.lives += 1
            helico.score -= LIFE_COST
        

    
        