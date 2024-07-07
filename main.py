import os
import keyboard
import numpy as np

def two_d():
    A1 = [[1, 2], [3, 4]]
    matrix_arr = np.matrix(A1[0][1])
    return matrix_arr

def player():
    player_SH='''
    ^-^
    | |
    '''
    return player_SH

def enemy():
    enemy_SH='''
    ^-^
    |-|
    '''
    return enemy_SH

def obstacles():
    caltrop_SH='###'
    return caltrop_SH

def bullets():
    bullets_SH='!'
    return bullets_SH


while True:  # Loop to capture keys continuously
    event = keyboard.read_event()  # Capture a keyboard event

    if event.name == 'q' and event.event_type == 'down':
        print("Q key was pressed.")
        break
    elif event.event_type == 'down':
        print(f"{event.name} key was pressed")
        print(two_d())
        print(bullets())
        print(player())
        print(enemy())
        print(obstacles())
    elif event.event_type == 'up':
        print(f"{event.name} key was pressed")
        print(two_d())
        print(player())
