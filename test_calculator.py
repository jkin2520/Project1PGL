import pytest
from main import roman_to_int, int_to_roman, process_input

# Test cases for Roman to Integer conversion
def test_roman_to_int():
    assert roman_to_int('I') == 1
    assert roman_to_int('V') == 5
    assert roman_to_int('X') == 10
    assert roman_to_int('L') == 50
    assert roman_to_int('C') == 100
    assert roman_to_int('D') == 500
    assert roman_to_int('M') == 1000
    assert roman_to_int('IV') == 4
    assert roman_to_int('IX') == 9
    assert roman_to_int('CMXCIV') == 994
    
    with pytest.raises(ValueError):
        roman_to_int('A')  # Invalid Roman numeral

# Test cases for Integer to Roman conversion
def test_int_to_roman():
    assert int_to_roman(1) == 'I'
    assert int_to_roman(5) == 'V'
    assert int_to_roman(10) == 'X'
    assert int_to_roman(50) == 'L'
    assert int_to_roman(100) == 'C'
    assert int_to_roman(500) == 'D'
    assert int_to_roman(1000) == 'M'
    assert int_to_roman(3999) == 'MMMCMXCIX'
    
    with pytest.raises(ValueError):
        int_to_roman(0)  # Should raise error for zero
    with pytest.raises(ValueError):
        int_to_roman(4000)  # Should raise error for out-of-range number

# Test cases for full expression processing
def test_process_input():
    assert process_input('VI') == '6'
    assert process_input('I + I') == 'II'
    assert process_input('(VII + V) * II + I') == 'XXV'
    assert process_input('X / III') == "There is no concept of a fractional number in Roman numerals."
    assert process_input('III - III') == "0 does not exist in Roman numerals."
    assert process_input('M + M') == 'MM'
    
    with pytest.raises(ValueError):
        process_input('4000 + M')  # Should raise error for out-of-bounds result
    assert process_input('I - II') == "Negative numbers can't be represented in Roman numerals."

    assert process_input('invalid_input') == "I don't know how to read this."

# Run tests from the command line
if __name__ == "__main__":
    pytest.main()

