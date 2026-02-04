def is_paired(input_string):
    # First, clean the string: keep ONLY brackets
    # (Because "a(b)c" is harder to shrink than "( )")
    code = "".join(char for char in input_string if char in "()[]{}")

    # Keep shrinking as long as there are pairs to shrink
    while "()" in code or "[]" in code or "{}" in code:
        code = code.replace("()", "")
        code = code.replace("[]", "")
        code = code.replace("{}", "")

    # If the string is empty, everyone found a partner!
    return code == ""

