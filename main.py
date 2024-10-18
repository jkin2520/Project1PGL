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

def roman_to_int(roman):
    """
    Convert a Roman numeral to an integer.
    
    Args:
        roman (str): Roman numeral string to be converted.
    
    Returns:
        int: The integer representation of the Roman numeral.
    
    Raises:
        ValueError: If the Roman numeral is invalid.
    """
    result = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_to_int_map.get(char)
        if not value:
            raise ValueError("Invalid Roman numeral.")
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

def int_to_roman(number):
    """
    Convert an integer to a Roman numeral.
    
    Args:
        number (int): The integer to convert to Roman numerals.
    
    Returns:
        str: Roman numeral representation of the integer.
    
    Raises:
        ValueError: If the number is zero, negative, or greater than 3,999.
    """
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

def evaluate_expression(expression):
    """
    Evaluate an arithmetic expression with integers.
    
    Args:
        expression (str): The mathematical expression to evaluate.
    
    Returns:
        int: The result of the evaluated expression.
    
    Raises:
        ValueError: If division by zero occurs or if the expression contains invalid syntax.
    """
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

def replace_roman_with_int(expression):
    """
    Replace Roman numerals in an expression with their integer equivalents.
    
    Args:
        expression (str): The expression containing Roman numerals.
    
    Returns:
        str: The expression with Roman numerals replaced by integers.
    """
    return re.sub(r'[IVXLCDM]+', lambda x: str(roman_to_int(x.group())), expression)

def process_input(input_str):
    """
    Process the input string, perform arithmetic operations, and convert the result back to Roman numerals.
    
    Args:
        input_str (str): The input Roman numeral expression.
    
    Returns:
        str: The result of the evaluation in Roman numerals or an error message.
    """
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

# Main entry point with interactive input
if __name__ == "__main__":
    while True:
        input_str = input("Enter a Roman numeral expression (or type 'exit' to quit): ")
        if input_str.lower() == 'exit':
            break
        print(process_input(input_str))
