# tree
from map import Map
import time
import os

tmp = Map(20, 10)
tmp.generateForest(3, 10)
tmp.generateRiver(10)
tmp.generateRiver(10)
tmp.printMap()


tick = 1
TICK_SLEEP = 0.23
while True:
    os.system("cls")
    print("TICK", tick)
    tmp.printMap()
    tick += 1
    time.sleep(TICK_SLEEP)
