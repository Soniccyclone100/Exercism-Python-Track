# Source - https://stackoverflow.com/a
# Posted by Forge, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-15, License - CC BY-SA 3.0

def is_armstrong_number(number):
    result = 0
    snumber = str(number)
    l = len(snumber)
    for digit in snumber:
        result += int(digit)**l
        if result > number:
            return False
    if result != number:
        return False
    return True
