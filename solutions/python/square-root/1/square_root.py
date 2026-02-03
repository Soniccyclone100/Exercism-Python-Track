def square_root(number):
    
    if number < 0:
        return "Unable to find The Sq Root"
    
    guess = number // 1 
    while abs(guess * guess - number) > 0.1:
        guess = (guess + (number / guess)) // 2
        
    return guess