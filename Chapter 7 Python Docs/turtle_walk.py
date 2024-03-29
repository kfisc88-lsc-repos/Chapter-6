import random

def randomWalk(t, turns, distance=20):
    """Turns a random number of degrees and moves a given distance for a fixed number of turns"""
    for x in range(turns):
        if x % 2 == 0:
            t.left(random.randint(0, 270))
        else:
            t.right(random.randint(0, 270))
        t.forward(distance)