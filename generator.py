# program to generate passwords

import sys, random
from string import digits, ascii_letters, punctuation

# original alphanumeric string with punctuations
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation

def create_password() -> str:
    '''
    Checks that password length is greater than 9
    Prints error messages and runs until an accurate number is entered
    '''
    try:
        user_input = int(input("Enter a password length greater than or equal to 10: "))
        while user_input < 10 :  # NIST SP 800-132 standard
            print("Password length too short.")
            user_input = int(input("Enter a password length greater than or equal to 10: "))
        else:
            # random password generation
            answer = ''.join(random.choices(ALL_LETTERS_DIGITS, k = user_input))
            return answer
    except ValueError:  # if int cannot cast string
        print("Enter a number between 10 and 20")
    except:  # catch all other errors
        print("Something went wrong")
    create_password()
    
def main():
    print("Welcome to the Password Generator.")
    return create_password()

if __name__ == "__main__":
    main()