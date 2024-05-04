"""
File: PotholeFilling.py
Name: 邦宇2
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is at the(2,1)
    post-condition:Karel is at the(2,7)
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()

def go_in():
    """
    pre_condition:Karel is at the upper left,facing east
    post_condition:Karel is in the pothole,facing south
    """
    move()
    turn_right()
    move()


def put_99_beepers():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()

def go_out():
    """
    pre_condition:Karel is in the pothole,facing south
    post_condition:Karel is at the upper left,facing east
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_right():
    """
    Karel will turn right
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Karel will turn around
    """
    for i in range(2):
        turn_left()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
