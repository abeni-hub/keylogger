# Controlling your mouse
# COntrolling to your keyboard
#Listening to your mouse and keyboard
from pynput.mouse import Controller
from pynput.keyboard import Controller


def controlMouse():
    mouse = Controller()
    mouse.position = (400,400)

controlMouse()

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("I am freaking awesome!")

controlKeyboard()