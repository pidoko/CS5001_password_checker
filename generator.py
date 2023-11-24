# program to generate passwords

import sys, random, math
from string import digits, ascii_letters, punctuation

# original alphanumeric string with punctuations
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation


def create_password(user_input: int) -> str:
    """
    Random password generator that checks that password length is greater than 11,
    prints error messages and runs until an appropriate length is entered.

    Examples:
        >>> create_password()
        'E~Bu1U%yBSsU'

    Args:
        user_input (int): password length

    Returns:
        str: the password
    """

    try:
        # minimum 12 characters to increase password entropy
        while user_input < 12 :  # NIST SP 800-132 standard
            print("Password length too short.")
            user_input = int(input("How long do you want your password to be? minimum 12, max 20: "))
        else:
            if user_input > 20:  # mastercard's limit
                print("Password length longer than 20.")
                user_input = int(input("How long do you want your password to be? minimum 12, max 20: "))
            else:
                # random password generation
                answer = ''.join(random.choices(ALL_LETTERS_DIGITS, k = user_input))
                return answer
    except ValueError:  # if int cannot cast string
        print("Enter a number (e.g. 17).")
    except:  # catch all other errors
        print("Something went wrong")
    create_password(user_input)


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


def type_password(user_input: str) -> str:
    """
    Takes in user generated password, checks the passwords against various rules,
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
    if len(user_input) < 12:
        print("Please create a password longer than 11 characters.")
    elif user_input.islower():
        print("Please combine uppercase letters with your password.")
    elif user_input.isupper():
        print("Please combine lowercase letters with your password.")
    elif user_input.isalpha():
        print("Please include a number in your password")
    elif user_input.isalnum():
        print("Please include a special character in your password")
    else:
        # check if password too similar to top 1,000,000 password list
        with open('password_list.txt') as password_list:
            # check password in lowercase without punctuations
            if clean_word(user_input) in password_list.read():
                print("This password is found in a list of commonly used passwords.")
            else:
                with open('password_list.txt') as password_list:
                    # check password in lowercase without punctuations and without numbers
                    if (''.join(filter(lambda x: not x.isdigit(), clean_word(user_input)))) in password_list.read():
                        print("The sequence of alphabets in your password is found in a list of commonly used passwords.")
                    else:
                        return user_input

    return type_password(input("Create a password of minimum 12 characters combining lowercase, uppercase, digits and symbols"))



