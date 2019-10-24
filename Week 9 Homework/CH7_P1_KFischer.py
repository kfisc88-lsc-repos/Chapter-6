"""
Kelley Fischer
CIS 1415 - Intro to Programming
October 23, 2019
"""

from turtle import Turtle
from math import pi


def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x, y)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * pi * (radius / 120.0))


def main():
    t = Turtle()

    drawCircle(t, 50, 50, 100)


if __name__ == '__main__':
    main()
