import numpy as np
import math

def convert_to_decimal(quinary_number) -> int: # what does -> int do? JD
    return int(str(quinary_number), 5)

def convert_to_quinary(decimal_number) -> int:
    return int(np.base_repr(decimal_number, 5)) # use numpy to one-line

def add(quinary_1, quinary_2) -> int:
    return convert_to_quinary(convert_to_decimal(quinary_1) + convert_to_decimal(quinary_2))

def subtract(quinary_1, quinary_2) -> int:
    return convert_to_quinary(convert_to_decimal(quinary_1) - convert_to_decimal(quinary_2))

def multiply(quinary_1, quinary_2) -> int:
    return convert_to_quinary(convert_to_decimal(quinary_1) * convert_to_decimal(quinary_2))

def divide(quinary_1, quinary_2) -> int:
    if quinary_2 == 0:
        return "Cannot divide by zero"
    return convert_to_quinary(convert_to_decimal(quinary_1) // convert_to_decimal(quinary_2))

def sqrt(quinary) -> int:
    if quinary < 0:
        return "No root"
    return convert_to_quinary(math.floor(math.sqrt(convert_to_decimal(quinary))))

def square(quinary) -> int:
    return convert_to_quinary(convert_to_decimal(quinary)**2)
