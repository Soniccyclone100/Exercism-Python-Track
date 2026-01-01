def translate(text):
    # Rule helper for individual words
    def translate_word(word):
        vowels = ('a', 'e', 'i', 'o', 'u')
        
        # Rule 1: starts with vowel OR "xr", "yt"
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"
        
        # Rule 3: starts with consonant followed by "qu"
        # Check this BEFORE general consonants
        if not word.startswith(vowels) and word[1:3] == "qu":
            return word[3:] + word[0:3] + "ay"
        
        # Rule 3 (part 2): starts with "qu"
        if word.startswith("qu"):
            return word[2:] + "quay"
        
        # Rule 2 & 4: Move consonant cluster (up to first vowel or 'y' after first letter)
        for i, char in enumerate(word):
            if i > 0 and char in vowels + ('y',):
                return word[i:] + word[:i] + "ay"
        
        return word + "ay"

    # Step 1: Split the sentence into individual words
    words = text.split() 
    # Step 2: Translate each word separately
    translated = [translate_word(w) for w in words]
    # Step 3: Join them back into a sentence
    return " ".join(translated)

# Testing the example
print(translate("Supersatanson")) 
# Output: "ickquay astfay unray"
