#0 - Field
#1 - Tree
#2 - River
#3 - Hospital
#4 - Upgrade shop
#5 - Fire

from utils import randbool, randcell, randcell2

CELL_TYPES = "🟩🌳🌊🏥🛒🔥"

class Map:
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

    def generateForest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w) :
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1                    


    def printMap(self):
        print("⬛" * (self.w + 2))
        for row in self.cells:
            print("⬛", end="")
            for cell in row:
                if (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("⬛")
        print("⬛" * (self.w + 2))

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
        for i in range(5):
            self.addFire()

    def checkBounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        