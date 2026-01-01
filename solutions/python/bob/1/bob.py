def response(hey_bob):
    # .strip() removes whitespace around the text
    # This ensures " " is treated as silence and "How are you? " is a question
    phrase = hey_bob.strip()

    # 1. Check for silence first
    if not phrase:
        return "Fine. Be that way!"

    # 2. Check for yelled question (Highest priority)
    # isupper() only returns True if there are letters and they are all caps
    if phrase.isupper() and phrase.endswith("?"):
        return "Calm down, I know what I'm doing!"

    # 3. Check for yelling (All Caps)
    if phrase.isupper():
        return "Whoa, chill out!"

    # 4. Check for regular question (Ends with ?)
    if phrase.endswith("?"):
        return "Sure."

    # 5. Anything else
    return "Whatever."
