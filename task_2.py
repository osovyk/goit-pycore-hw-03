import random

"""
1. The requirements should be changed for example to 'start' and 'stop',
since 'max' and 'min' are Shadows built-in names in Python.

2. The requirements are not clear:
quantity=53, min=50, max=56 what function should return?
"""


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Returns a list with the specified number of integers from the specified range

    Requirement:
    1. min, max, quantity should be integer
    2. min >= 1
    3. max <= 1000
    4. max - min >= quantity - 1

    :param min: Required. An integer specifying at which position to start.
    :param max: Required. An integer specifying at which position to end.
    :param quantity: Required. An integer specifying the number to generate
    :return: Returns a list of integers
    """
    result = []
    try:
        if min >= 1 and max <= 1000 and max - min >= quantity - 1:
            while len(result) < quantity:
                new_number = random.randint(min, max)
                if new_number not in result:
                    result.append(new_number)
            result.sort()
    except Exception:
        return result

    return result
