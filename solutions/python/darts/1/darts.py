import math

def score(x, y):
    distance = math.sqrt(x**2 + y**2)
    if distance > 10:   # Outside the target
        return 0
    elif distance > 5:  # Outer circle (radius 10)
        return 1
    elif distance > 1:  # Middle circle (radius 5)
        return 5
    else:               # Inner circle (radius 1)
        return 10