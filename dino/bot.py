
from PIL  import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Coordenadas():
    replay = (960,360)
    dino = (700,366)

def restartGame():
     pyautogui.click(Coordenadas.replay)

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.04)
    print("jump")
    pyautogui.keyUp('space')

def obstacle():
    box=(Coordenadas.dino[0]+40,Coordenadas.dino[1]-30,Coordenadas.dino[0]+100,Coordenadas.dino[1]+50)
    Image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(Image)
    a = array(grayImage.getcolors())
    return a.sum()
       


restartGame()
while True:    
    if obstacle() != 5130:
        jump()



