import os
import sys
import keyboard
import numpy as np


def player():
    player_SH='''
    ^-^
    | |
    '''
    return player_SH

class P:
   def __init__(self, standing_on):
       self.standing_on = standing_on
       self.row, self.column = 14, 14

   def __str__(self):
       car = '''
        ^-^
        | |
        '''
       return '@'

class Player:
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column

    # This method is a string representation of the player. 
    # It's called when you try to print an instance of the player class.
    def __str__(self):
        return "P"

# Create a player instance at position (5,5)
p = Player(5, 5)
# game_map = np.full((25, 25), ".")

class G:
    walkable = True

    def __str__(self):
        return "█"


class W:
    walkable = False

    def __str__(self):
        return "|"

rows, columns = os.popen('stty size', 'r').read().split()
rowX = int(rows)
columnX = int(columns)

p = P(G())
game_map = np.full((rowX, columnX), G())
game_map[:, 0] = W()
game_map[0, :] = W()
game_map[:, -1] = W()
game_map[-1, :] = W()
#game_map[p.row][p.column] = str(p)

def print_map(game_map):
    game_map[p.column][p.row] = p
    lenC, lenR = game_map.shape  # If game_map is a numpy array, this gets its dimensions
    for column in range(lenC):
        for row in range(lenR):
            print(game_map[column][row], end="")
        print()

def move_up():
    temp = p.row - 1
    if game_map[temp][p.column].walkable:
        game_map[p.column][p.row] = p.standing_on
        p.column -= 1
        p.standing_on = game_map[p.column][p.row]
        game_map[p.row][p.column] = p

def move_down():
    temp = p.row + 1
    if game_map[temp][p.column].walkable:
        game_map[p.column][p.row] = p.standing_on
        p.column += 1
        p.standing_on = game_map[p.column][p.row]
        game_map[p.row][p.column] = p

def move_left():
    temp = p.column - 1
    if game_map[p.row][temp].walkable:
        game_map[p.column][p.row] = p.standing_on
        p.row -= 1
        p.standing_on = game_map[p.column][p.row]
        game_map[p.column][p.row] = p

def move_right():
    temp = p.column + 1
    if game_map[p.row][temp].walkable:
        game_map[p.column][p.row] = p.standing_on
        p.row += 1
        p.standing_on = game_map[p.column][p.row]
        game_map[p.column][p.row] = p

while True:  # Loop to capture keys continuously
    event = keyboard.read_event()  # Capture a keyboard event

    if event.name == 'esc' and event.event_type == 'down':
        print("[ ESC ] key was pressed.")
        break
    # elif event.event_type == 'down':
       # print(f"{event.name} key was pressed")
    elif event.name == 'up' and event.event_type == 'down':
        print(f"{event.name} key was pressed")
        os.system('clear')
        print_map(game_map)
        print(p.row, p.column, "\n")
        move_up()
        os.system('clear')
        print_map(game_map)
        print(p.row, p.column, "\n")
    elif event.name == 'down' and event.event_type == 'down':
        print(f"{event.name} key was pressed")
        os.system('clear')
        print_map(game_map)
        print(p.row, p.column, "\n")
        move_down()
        os.system('clear')
        print_map(game_map)
        print(p.row, p.column, "\n")
    elif event.name == 'left' and event.event_type == 'down':
        print(f"{event.name} key was pressed")
        os.system('clear')
        print_map(game_map)
        print(p.row, p.column, "\n")
        move_left()
        os.system('clear')
        print_map(game_map)
        print(p.row, p.column, "\n")
    elif event.name == 'right' and event.event_type == 'down':
        print(f"{event.name} key was pressed")
        os.system('clear')
        print_map(game_map)
        print(p.row, p.column, "\n")
        move_right()
        os.system('clear')
        print_map(game_map)
        print(p.row, p.column, "\n")
