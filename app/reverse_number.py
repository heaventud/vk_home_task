class UnsupportedInput(Exception):
    pass


def reverse_number(number: int) -> int:
    """
    The method accepts a natural number and returns
    another natural number that represents input’s reverse.
    """
    if not isinstance(number, int):
        raise UnsupportedInput(f'Expected integer, but {type(number)} given')
    if number <= 0:
        raise UnsupportedInput('Only natural numbers are supported')
    result = 0
    while True:
        if number >= 1:
            digit = number % 10
            number = number // 10
            result = result * 10 + digit
        else:
            break
    return result
