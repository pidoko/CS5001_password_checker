# program to generate passwords

import sys, random, math
from string import digits, ascii_letters, punctuation

# original alphanumeric string with punctuations
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation

def create_password() -> str:
    '''
    Password generator that checks that password length is greater than 9,
    prints error messages and runs until an accurate number is entered.
    '''
    try:
        user_input = int(input("How long do you want your password to be? minimum 12: "))
        # minimum 12 characters to increase password entropy
        while user_input < 12 :  # NIST SP 800-132 standard
            print("Password length too short.")
            user_input = int(input("How long do you want your password to be? minimum 12: "))
        else:
            if user_input > 1000:
                print("Password length too long.")
            else:
                # random password generation
                answer = ''.join(random.choices(ALL_LETTERS_DIGITS, k = user_input))
                return answer
    except ValueError:  # if int cannot cast string
        print("Enter a number (e.g. 17).")
    except:  # catch all other errors
        print("Something went wrong")
    create_password()


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


def type_password() -> str:
    # minimum 12 characters to increase password entropy
    user_input = input("Create a password of minimum 12 characters combining lowercase, uppercase, digits and symbols")
    if len(user_input) < 3:
        print("Please create a password longer than 11 characters.")
        return type_password()
    elif user_input.islower():
        print("Please combine uppercase letters with your password.")
        return type_password()
    elif user_input.isupper():
        print("Please combine lowercase letters with your password.")
        return type_password()
    else:
        # check if password too similar to top 1,000,000 password list
        with open('password_list.txt') as password_list:
            if clean_word(user_input) in password_list.read():
                print("The password is too weak.")
                return type_password()
            else:
                return user_input


def main():
    print("Welcome to the Password Generator.")
    main_answer = input("Press 1 to create your password and any other key for a computer generated password")
    if main_answer == '1':
        output = type_password()
    else:
        output = create_password()
    entropy = round(math.log2(len(ALL_LETTERS_DIGITS) ** len(output)), 2)
    time = round(((len(ALL_LETTERS_DIGITS) ** len(output)) / (3500000000 * 6.308 * (10 ** 7))), 0)
    return print(f"Your password is {output}\nIt has an entropy of {entropy}.\nIt will take about {time} years to crack.")

if __name__ == "__main__":
    main()