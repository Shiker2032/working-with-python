from map import Map
from pynput import keyboard
from hellicopter import Hellicopter
import time
import os


TICK_SLEEP = 0.2
TREE_UPDATE = 50
FIRE_UPDATE = 40
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)



helico = Hellicopter(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1,0), 'a': (0, -1)}

def process_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
        
listener = keyboard.Listener(
    on_release=process_key)
listener.start()

tick = 1

while True:
    os.system("cls") #clear for linux
    field.processHelicopter(helico)
    helico.printStats()
    field.printMap(helico)
    print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generateTree()
    if (tick % FIRE_UPDATE == 0):
        field.updateFires(helico)
