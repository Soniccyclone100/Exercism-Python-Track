def is_isogram(string):
    # Filter for letters only and normalize to lowercase
    chars = [c.lower() for c in string if c.isalpha()]
    return len(set(chars)) == len(chars)