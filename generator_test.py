"""
Final Project: Password generator and checker test file    
=======================
Course:   CS 5001
Semester: Fall 2023
Student:  Peter Idoko

Functions that test the functions in the generator file to ensure edge cases are accounted for.
"""
from generator import check_value, check_length, create_password, clean_word, common_password, common_password_num, type_password

# text file with one million common passwords
PASSWORD_FILE = 'password_list.txt'

def check_string(actual: str, expected: str) -> int:
    """checks for error, returns 1 if error exists, 0 if it doesn't

    Args:
        actual (str): actual value
        expected (str): expected value
    """
    if actual != expected:
        print(f"Actual: {actual} does not equal Expected: {expected}")
        return 1
    return 0


def check_bool(actual: bool, expected: bool) -> int:
    """checks for error, returns 1 if error exists, 0 if it doesn't

    Args:
        actual (bool): actual value
        expected (bool): expected value
    """
    if actual != expected:
        print(f"Actual: {actual} does not equal Expected: {expected}")
        return 1
    return 0


def check_int(actual: int, expected: int) -> int:
    """checks for error, returns 1 if error exists, 0 if it doesn't

    Args:
        actual (int): actual value
        expected (int): expected value
    """
    if actual != expected:
        print(f"Actual: {actual} does not equal Expected: {expected}")
        return 1
    return 0


def test_check_value() -> int:
    """
    tests generator.check_value

    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    fail += check_int(check_value(10), 0)
    fail += check_int(check_value(15), 1)
    fail += check_int(check_value(-1), 0)
    
    return fail


def test_check_length() -> int:
    """
    tests generator.check_length

    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    fail += check_int(check_length("@#faf"), 0)
    fail += check_int(check_length("@#*(G_h'J-wdf"), 1)
    fail += check_int(check_length("1234567891011"), 1)
    
    return fail


def test_create_password() -> int:
    """
    tests generator.create_password

    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    if create_password(15) == len(create_password(15)):
        fail += 0
    else:
        fail += 1
    
    return fail

def test_clean_word() -> str:
    """
    tests generator.clean_word

    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    fail += check_string(clean_word('Hello!'), "hello")
    fail += check_string(clean_word('World...'), "world")
    fail += check_string(clean_word(' main@msn.com '), "mainmsncom")
    
    return fail

def test_common_password() -> int:
    """
    tests generator.common_password

    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    fail += check_int(common_password(PASSWORD_FILE, "Yankees12345!"), 1)
    fail += check_int(common_password(PASSWORD_FILE, "Denyak1234!!!"), 1)
    
    return fail

def test_common_password_num() -> int:
    """
    tests generator.common_password_num

    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    fail += check_int(common_password_num(PASSWORD_FILE, "Yankees12345!"), 0)
    fail += check_int(common_password_num(PASSWORD_FILE, "denyak"), 1)
    
    return fail

def type_password() -> str:
    """
    tests generator.type_password

    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    fail += check_string(type_password('Denyak123!!!'), 'Denyak123!!!')
    fail += check_string(type_password('Denyak123!'), "Please create a password longer than 11 characters.")
    fail += check_string(type_password('denyak123!!!'), "Please combine uppercase letters with your password.")
    fail += check_string(type_password('KHOTSI627!!!'), "Please combine lowercase letters with your password.")
    fail += check_string(type_password('Eaglespannerheal'), "Please include a number in your password")
    fail += check_string(type_password('Eaglespannerheal1'), "Please include a special character in your password")
    fail += check_string(type_password('Shadow1987!!!'), "This password is found in a list of commonly used passwords.")
    
    return fail

def main() -> None:
    fail = 0
    fail += test_clean_word()
    fail += test_is_palindrome()
    fail += test_count_vowels()

    print(f"Failed {fail} tests.")


if __name__ == "__main__":
    main()
