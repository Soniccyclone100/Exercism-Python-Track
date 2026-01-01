def leap_year(year):
    # The most crucial fix: Check divisibility by 400 *before* divisibility by 100 or 4.

    # 1. If divisible by 400, it is a leap year (e.g., 2000, 2400)
    if year % 400 == 0:
        return True
    # 2. If divisible by 100 but not 400, it is not a leap year (e.g., 1900, 2100)
    elif year % 100 == 0:
        return False
    # 3. If divisible by 4 but not 100, it is a leap year (e.g., 2024, 2028)
    elif year % 4 == 0:
        return True
    # 4. Otherwise, it is not a leap year (e.g., 2015, 2023)
    else:
        return False

# You can test the function by calling it outside of its definition:
print(leap_year(2015))
print(leap_year(1900))
print(leap_year(2000))
