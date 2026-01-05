import string

# Adding ='encrypt' makes this argument optional for the tests
def rotate(text, key, mode='encrypt'):
    # Standard English alphabet has 26 letters
    key %= 26
    
    if mode == 'decrypt':
        key = -key

    # Setup alphabets
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    
    shifted_lower = lower_alphabet[key:] + lower_alphabet[:key]
    shifted_upper = upper_alphabet[key:] + upper_alphabet[:key]
    
    # Create the map
    translation_table = str.maketrans(lower_alphabet + upper_alphabet, 
                                      shifted_lower + shifted_upper)

    # RETURN THE RESULT (don't call the function again here)
    return text.translate(translation_table)

    original_text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    return rotate(original_text, 13, "encrypt")