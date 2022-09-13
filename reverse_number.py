class UnsupportedInput(Exception):
    pass


def reverse_number(number: int) -> int:
    """

    """
    if not isinstance(number, int):
        raise UnsupportedInput(f'Expected integer, but {type(number)} given')
    result = 0
    i = 1
    while True:
        if number >= 1:
            digit = number % 10
            number = number // 10
            result = result * 10 + digit
            i *= 10
            print(digit)
            print(number)
        else:
            break
    return result
