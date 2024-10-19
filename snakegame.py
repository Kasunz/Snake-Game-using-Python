""" Snake Game Using Python """

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,255,0)):
        pass
    
    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes=False):
        pass
    

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass
    
    def reset(self):
        pass
    
    def addCube(self):
        pass
    
def drawGrid(w, rows, surface):
    pass

def redrawWindow(surface):
    pass

def randomSnack(rows, items):
    pass

def massage_box(subject, content):
    pass


def main():
    width = 600
    height = 600
    rows = 30
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10)) # Snake color -->  Red , position --> 10, 10 
    flag = True
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50) # ms milliseconds
        clock.tick(10)
        redrawWindow(win)
        
rows = None
w = None
h = None

cube.rows = rows
cube.w = w

main()
