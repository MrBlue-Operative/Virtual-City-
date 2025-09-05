import sys # unused
import pygame as py
def EVENT(events):
    for event in events:
        if event.type == py.QUIT:
            py.quit()
            return False
    return True