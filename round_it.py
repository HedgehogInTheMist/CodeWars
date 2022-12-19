from math import ceil, floor


def round_it(n: float) -> int:
    general_part = len(str(n)) - 1
    integer_part = len(str(int(n)))
    mantissa = general_part - integer_part

    if integer_part < mantissa:
        return ceil(n)
    elif integer_part > mantissa:
        return floor(n)
    else:
        integer_part == mantissa
        return round(n)
