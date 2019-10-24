import random

# Shapes
triangle = 3
square = 4
pentagon = 5
hexagon = 6
heptagon = 7
octagon = 8
nonagon = 9
decagon = 10


def polygon(t, length, sides):
    """Draws a polygon with a given length and given number of sides."""
    for count in range(sides):
        t.forward(length)
        t.left(360 / sides)


def radialPattern(t, n, length, shape):
    """Draws a radial pattern of n shapes with a given length and given shape.
    Shapes Include:
    triangle
    square
    pentagon
    hexagon
    heptagon
    octagon
    nonagon
    decagon
    """
    for count in range(n):
        polygon(t, length, shape)
        t.left(360 / n)


def drawPattern(t, x, y, count, length, shape):
    """Draws a radial pattern with a random fill color at the given position."""
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    t.fillcolor(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    radialPattern(t, count, length, shape)
    t.end_fill()
