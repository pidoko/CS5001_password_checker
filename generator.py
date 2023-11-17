# program to generate passwords

import sys, random
from string import digits, ascii_letters, punctuation

# original alphanumeric string with punctuations
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation

def get_input() -> int:
    '''
    Checks that user input is between 10 and 20 inclusive
    Prints error messages and runs until an accurate number is entered
    '''
    try:
        user_input = int(input("Enter password length between 10 to 20: "))
        while user_input < 10 :
            if user_input < 10:
                print("Enter a value greater than 10.")
            else:
                print("Enter an integer between 10 and 20.")
            user_input = int(input("Length of password to be created (10 - 20): "))
        else:
            # random password generation
            answer = ''.join(random.choices(ALL_LETTERS_DIGITS, k = user_input))
            print(answer)
            return answer
    except ValueError:  # if int cannot cast string
        print("Enter a number between 10 and 20")
    except:  # catch all other errors
        print("Something went wrong")
    get_input()
    
def main():
    print("Welcome to the Password Generator.")
    return get_input()

if __name__ == "__main__":
    main()