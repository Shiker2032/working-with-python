# tree
from map import Map
import time
import os

TICK_SLEEP = 0.1
TREE_UPDATE = 50
FIRE_UPDATE = 40
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.generateForest(3, 10)
field.generateRiver(10)
field.generateRiver(10)
field.printMap()


tick = 1

while True:
    os.system("cls") #clear for linux
    print("TICK", tick)
    field.printMap()
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generateTree()
    if (tick % FIRE_UPDATE == 0):
        field.updateFires()
