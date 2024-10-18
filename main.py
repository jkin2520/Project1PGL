import sys
import re

# Roman numeral lookup table
roman_to_int_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

int_to_roman_map = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
    (1, 'I')
]

# Convert a Roman numeral to an integer
def roman_to_int(roman):
    result = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_to_int_map[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

# Convert an integer to a Roman numeral
def int_to_roman(number):
    if number <= 0:
        raise ValueError("0 does not exist in Roman numerals.")
    if number > 3999:
        raise ValueError("You're going to need a bigger calculator.")
    
    result = ""
    for value, numeral in int_to_roman_map:
        while number >= value:
            result += numeral
            number -= value
    return result

# Perform arithmetic operations
def evaluate_expression(expression):
    try:
        result = eval(expression)
        if result <= 0:
            raise ValueError("Negative numbers can't be represented in Roman numerals.")
        return result
    except ZeroDivisionError:
        raise ValueError("There is no concept of a fractional number in Roman numerals.")
    except SyntaxError:
        raise ValueError("I don't know how to read this.")
    except Exception as e:
        raise ValueError(str(e))

# Replace Roman numerals with their integer equivalents
def replace_roman_with_int(expression):
    return re.sub(r'[IVXLCDM]+', lambda x: str(roman_to_int(x.group())), expression)

# Process command line input
def process_input(input_str):
    input_str = input_str.replace(" ", "")  # Remove spaces
    try:
        # Handle single Roman numeral input
        if re.match(r'^[IVXLCDM]+$', input_str):
            return str(roman_to_int(input_str))
        
        # Replace Roman numerals in the expression with integers
        integer_expression = replace_roman_with_int(input_str)
        
        # Evaluate the mathematical expression
        result = evaluate_expression(integer_expression)
        
        # Convert the result back to a Roman numeral
        return int_to_roman(int(result))
    except ValueError as e:
        return str(e)

# Main entry point
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = ''.join(sys.argv[1:])
        print(process_input(input_str))
    else:
        print("Please provide a Roman numeral expression.")
