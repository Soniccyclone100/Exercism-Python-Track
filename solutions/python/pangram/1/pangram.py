import string

def is_pangram(sentence):
    # 1. Standardize input to lowercase
    sentence = sentence.lower()
    
    # 2. Define the set of all 26 lowercase letters
    alphabet = set(string.ascii_lowercase)
    
    # 3. Create a set of only the letters found in the sentence
    # We filter out spaces, numbers, and punctuation
    letters_in_sentence = set(char for char in sentence if char.isalpha())
    
    # 4. RETURN True if the sentence set contains all 26 letters
    return alphabet.issubset(letters_in_sentence)
