def convert(number):
    result = ""
    
    # Check each factor and add the sound if it fits
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    
    # If no factors matched, return the number as a string
    return result if result else str(number)

