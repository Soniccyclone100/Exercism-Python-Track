def classify(number):
    """ A perfect number equals the sum of its positive divisors. """
    
    # 1. Validation must be first and indented once (4 spaces)
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # 2. Calculation is also indented once
    # Use sum() with a generator to find all divisors from 1 up to number-1
    aliquot_sum = sum(i for i in range(1, number) if number % i == 0)

    # 3. Final classification logic
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
