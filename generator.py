# program to generate passwords

import sys, random
from string import digits, ascii_letters, punctuation

# original alphanumeric string with punctuations
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation

def create_password() -> str:
    '''
    Password generator that checks that password length is greater than 9,
    prints error messages and runs until an accurate number is entered.
    '''
    try:
        user_input = int(input("How long do you want your password to be? minimum 10: "))
        while user_input < 10 :  # NIST SP 800-132 standard
            print("Password length too short.")
            user_input = int(input("How long do you want your password to be? minimum 10: "))
        else:
            if user_input > 1000:
                print("Password length too long.")
            else:
                # random password generation
                answer = ''.join(random.choices(ALL_LETTERS_DIGITS, k = user_input))
                print(answer)
                return answer
    except ValueError:  # if int cannot cast string
        print("Enter a number (e.g. 17).")
    except:  # catch all other errors
        print("Something went wrong")
    create_password()


def type_password():
    user_input = input("Create a password of minimum length 10 characters combining lowercase, uppercase, digits and symbols").strip 
    if len(user_input) < 10:
        print("Please create a password longer than 9 characters.")
        type_password()
    elif user_input.islower():
        print("Please combine uppercase letters with your password.")
        type_password()
    elif user_input.isupper():
        print("Please combine lowercase letters with your password.")
        type_password()
    
    # check if password too similar to top 1,000,000 password list
    with open('password_list.txt') as password_list:
        if user_input.lower in password_list.read():
            print("The password is too weak.")
            type_password()
        else:
            pass
        
    return user_input    
    
def main():
    print("Welcome to the Password Generator.")
    main_answer = input("Press 1 to create your password and any other key for a computer generated password")
    if main_answer == '1':
        output = type_password()
    else:
        output = create_password()
    return output

if __name__ == "__main__":
    main()