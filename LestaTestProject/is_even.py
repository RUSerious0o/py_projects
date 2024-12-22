def isEven(value):
    return value % 2 == 0


def is_even(value: int) -> bool:
    return not value & 1
