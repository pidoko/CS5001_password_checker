"""
Final Project: Password generator and checker    
=======================
Course:   CS 5001
Semester: Fall 2023
Student:  Peter Idoko

Functions that generate random passwords greater than 12 in length, 
and allows users to create passwords that meet uppercase,
 lowercase, number, and special character requirements.
"""

# program to generate passwords
import sys, random, math
from string import digits, ascii_letters, punctuation

# original alphanumeric string with punctuations
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation

# text file with one million common passwords
PASSWORD_FILE = 'password_list.txt'

def check_value(user_input: int) -> int:
    ''' Checks if value of password length is greater than 11.
        If it is, it outputs 1, otherwise 0.

        Examples:
            >>> check_value(10)
            '0'
            >>> check_value(15)
            '1' 

        Args:
            user_input (int): length of password to be created

        Returns:
            int: 1 or 0
    '''

    try: 
        if user_input > 11:  # No upper password limit   
            return 1
        else:  # Ensures a minimum number of password permutations or entropy
            return 0
    except: # if int cannot cast string or any other errors.
        return 0

def check_length(user_input: str) -> int:
    ''' Checks if password length is greater than 12.
        If it is, it outputs 1, otherwise 0.

        Examples:
            >>> check_length("@#faf")
            '0'
            >>> check_length("@#*(G_h'J-wdf")
            '1' 

        Args:
            user_input (str): user-generated password

        Returns:
            int: 1 or 0
    '''

    if len(user_input) < 12:  # Ensures a minimum number of password permutations or entropy
        return 0
    else:  # No upper password limit
        return 1

def create_password(user_input: int) -> str:
    """  Creates a random password of user-specified length.

    Examples:
        >>> create_password(15)
        '09"Ea<~t&\\iLu?m'  # different password each time
        >>> create_password(5)
        '~viLu'  

    Args:
        user_input (int): password length

    Returns:
        answer (str): the password
    """

    # random password generation
    answer = ''.join(random.choices(ALL_LETTERS_DIGITS, k = user_input))
    return answer

def clean_word(word: str) -> str:
    """
    Recursively removes punctuation from a word, and reduces it to lower case.

    Examples:
        >>> clean_word('Hello!')
        'hello'
        >>> clean_word('World...')
        'world'
        >>> clean_word(' main@msn.com ')
        'mainmsncom'

    See:
        https://docs.python.org/3/library/stdtypes.html#str.isalnum


    Args:
        word (str): the word to remove punctuation from

    Returns:
        str: the word without punctuation
    """

    punctuation_set = "!#$%&'()*+,-./:;<=>?@][^_`{|}~ .— " + '"'
    if len(word) == 0:
        return ""
    if word[0] in punctuation_set:
        return clean_word(word[1:]).casefold()  # skip word if in set
    return (word[0].casefold() + clean_word(word[1:])).casefold()  # recursively add desirable character

def common_password(PASSWORD_FILE: str, user_input: str) -> int:
    '''  Check password in lowercase without punctuations
         
        Examples:
        >>> common_password(PASSWORD_FILE, "Yankees12345!")
        1
        >>> common_password(PASSWORD_FILE, "Denyak1234!!!")
        1

        Args:
            PASSWORD_FILE (str), user_input (str)
        
        Returns:
            0 or 1
    '''
    with open('password_list.txt') as password_list:
        
        if clean_word(user_input) in password_list.read():
            return 0
        else:
            return 1

def common_password_num(PASSWORD_FILE: str, user_input: str) -> int:
    '''  Check password in lowercase without punctuations and numbers
         
        Examples:
        >>> common_password_num(PASSWORD_FILE, "Yankees12345!")
        0
        >>> common_password_num(PASSWORD_FILE, "denyak")
        1
        
        Args:
            PASSWORD_FILE (str), user_input (str)
        
        Returns:
            0 or 1
    '''
    with open('password_list.txt') as password_list:
        # check password in lowercase without punctuations and without numbers
        if (''.join(filter(lambda x: not x.isdigit(), clean_word(user_input)))) in password_list.read():
            return 0
        else:
            return 1


def type_password(user_input: str) -> str:
    """  Takes in user generated password, checks the passwords against various rules,
        prints error messages notifying client of issue if the inputted entry is invalid,
        ,runs until an appropriate password is entered, and returns a string 
        (EXPLAIN WHY IN README FILE)

    Examples:
        >>> type_password('Denyak123!!!')
        'Denyak123!!!'
        >>> type_password('Denyak123!')
        'Please create a password longer than 11 characters.'

    Args:
        user_input (str): user-generated password

    Returns:
        str: user-generated password
    """
    # minimum 12 characters to increase password entropy
    if check_length(user_input) == 0:
        return "Please create a password longer than 11 characters."
    elif user_input.islower():
        return "Please combine uppercase letters with your password."
    elif user_input.isupper():
        return "Please combine lowercase letters with your password."
    elif user_input.isalpha():
        return "Please include a number in your password"
    elif user_input.isalnum():
        return "Please include a special character in your password"
    else:
        # check if password too similar to top 1,000,000 password list
        if common_password(PASSWORD_FILE, user_input) == 0:
            return "This password is found in a list of commonly used passwords."
        else:
            if common_password_num(PASSWORD_FILE, user_input) == 0:
                return "This password is found in a list of commonly used passwords."
            else:
                return user_input

def entropy(ALL_LETTERS_DIGITS: str, output: str) -> float:
    # Measure of how hard it is to use brute-force to guess the password.
    answer = round(math.log2(len(ALL_LETTERS_DIGITS) ** len(output)), 2)
    return answer

def time(ALL_LETTERS_DIGITS: str, output: str) -> float:
    # Estimate at how long it takes to crack the password using a PC with a 3.5GHz rate of attempts
    answer = round(((len(ALL_LETTERS_DIGITS) ** len(output)) / (3.154 * (10 ** 8) * (10 ** 9))), 0)  # years to crack based on 1billion passwords per second
    return answer