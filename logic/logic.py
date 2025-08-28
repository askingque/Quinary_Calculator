def convert_to_decimal(quinary_number) -> int:
    decimal_num = 0
    
    # move from left to right in the string
    # multiply the current total by 5
    # add the parsed digit to the total
    if quinary_number is str:
        for ch in quinary_number:
            decimal_num = 5 * decimal_num
            parsed = int(ch)
            decimal_num += parsed
            
    #adds the next digit space (think of a string of numbers) multiplied by the value of its respective space
    else:
        i = 0
        while quinary_number > 0:
            decimal_num = decimal_num + (quinary_number % 10) * (5 ** i)
            quinary_number //= 10
            i += 1
        

    return decimal_num

def convert_to_quinary(decimal_number) -> int:
    quinary_num = 0
    
        # convert if string!
    if decimal_number is str:
        decimal_parsed = int(decimal_number)
    else:
        decimal_parsed = decimal_number
        
    #adds the next digit space (think of a string of numbers) multiplied by the value of its respective space
    i = 0
    while decimal_parsed > 0:
        quinary_num = quinary_num + (decimal_parsed % 5) * (10 ** i)
        decimal_parsed //= 5
        i += 1
    return quinary_num


def add(quinary_1, quinary_2) -> int:
    decimal_1 = convert_to_decimal(quinary_1)
    decimal_2 = convert_to_decimal(quinary_2)
    return decimal_1 + decimal_2

def subtract(quinary_1, quinary_2) -> int:
    decimal_1 = convert_to_decimal(quinary_1)
    decimal_2 = convert_to_decimal(quinary_2)
    return decimal_1 - decimal_2

def multiply(quinary_1, quinary_2) -> int:
    decimal_1 = convert_to_decimal(quinary_1)
    decimal_2 = convert_to_decimal(quinary_2)
    return decimal_1 * decimal_2

def divide(quinary_1, quinary_2) -> int:
    decimal_1 = convert_to_decimal(quinary_1)
    decimal_2 = convert_to_decimal(quinary_2)
    if decimal_2 == 0:
        raise ValueError("Division by zero is not allowed")
        return None
    return decimal_1 // decimal_2

def sqrt(quinary) -> int:
    decimal = convert_to_decimal(quinary)
    return int(decimal ** 0.5)

def square(quinary) -> int:
    decimal = convert_to_decimal(quinary)
    return decimal ** 2
