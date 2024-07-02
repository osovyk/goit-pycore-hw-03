import re

"""
The requirements are not clear:
2. Перевірте, чи номер починається з '+', і виправте префікс згідно з вказівками.
3. Видаліть всі символи, крім цифр та '+', з номера телефону.

What should be the result if the number "38050+111+22+22"
"""


def remove_all_symbols(number: str) -> str:
    """
    Remove all symbols from a number except for 0-9 numbers

    :param number: Required. Any data in string format
    :return: String that contains only numbers
    """
    return re.sub("[^0-9]", "", number)


def add_region_code(number: str) -> str:
    """
    Add a region code to a phone number and return it

    :param number: Required. Any data in string format
    :return: String containing a phone number with a region code
    """
    match len(number):
        case 10:
            return "+38" + number
        case 11:
            return "+3" + number
        case 12:
            return "+" + number


def normalize_phone(phone_number: str) -> str:
    try:
        result = remove_all_symbols(phone_number)
        result = add_region_code(result)
    except Exception:
        raise Exception("Here should be some error message")
    else:
        return result
