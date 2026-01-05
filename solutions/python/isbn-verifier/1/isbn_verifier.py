def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    
    total = 0
    weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    for i in range(10):
        character = isbn[i]
        
        # 1. Handle the 'X' (only allowed at the last index, which is 9)
        if character == 'X' and i == 9:
            number = 10
        # 2. Handle normal digits
        elif character.isdigit():
            number = int(character)
        # 3. If it's anything else (like 'A'), it's invalid!
        else:
            return False
            
        # 4. Add to the total
        total += number * weights[i]

    # 5. After the loop is totally done, check the math
    return total % 11 == 0
