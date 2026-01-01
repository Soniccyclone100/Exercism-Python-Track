# Step 1: Implement Equilateral Function, This function checks if all sides are equal and greater than zero.
def equilateral(sides):
    a, b, c = sides
    if a == b == c and a > 0:
        return True
    return False

# Step 2: Implement Isosceles Function, This function checks if at least two sides are equal, while also ensuring the triangle is valid (sides > 0 and the triangle inequality holds).
def isosceles(sides):
    a, b, c = sides
    # Check validity and if at least two sides are equal
    if a > 0 and b > 0 and c > 0 and \
       (a + b >= c and a + c >= b and b + c >= a) and \
       (a == b or b == c or a == c):
        return True
    return False

#Step 3: Implement Scalene Function, This function checks if all sides are different and the triangle is valid.
def scalene(sides):
    a, b, c = sides
    # Check validity and if all sides are different
    if a > 0 and b > 0 and c > 0 and \
       (a + b >= c and a + c >= b and b + c >= a) and \
       (a != b and b != c and a != c):
        return True
    return False


