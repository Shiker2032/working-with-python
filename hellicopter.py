from utils import randcell

class Hellicopter:
    def __init__(self, w, h):
        rc = randcell(w ,h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.mxtank = 1
        self.tank = 0
        self.score = 0

    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >=0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def printStats(self):
        print("💧 ", self.tank, "/", self.mxtank, sep="", end=" | ")
        print("🏆", self.score)
