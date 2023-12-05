# Runs the password generator
import sys, random, math
from string import digits, ascii_letters, punctuation

# original alphanumeric string with punctuations
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation

from generator import (
    create_password,
    type_password,
)

def entropy(ALL_LETTERS_DIGITS: str, output: str) -> float:
    # Measure of how hard it is to use brute-force to guess the password.
    answer = round(math.log2(len(ALL_LETTERS_DIGITS) ** len(output)), 2)
    return answer

def time(ALL_LETTERS_DIGITS: str, output: str) -> float:
    # Estimate at how long it takes to crack the password using a PC with a 3.5GHz processor
    answer = round(((len(ALL_LETTERS_DIGITS) ** len(output)) / (3.154 * (10 ** 8) * (10 ** 9))), 0)  # years to crack based on 1billion passwords per second
    return answer

def main():
    print("Welcome to the Password Generator.")

    selection = input("Press 1 to create your password and any other key for a computer generated password")
    if selection == '1':
        user_input = input("Create a password of minimum 12, max 20 characters combining lowercase, uppercase, digits and symbols")
        output = type_password(user_input)
    else:
        user_input = int(input("How long do you want your password to be? minimum 12, max 20: "))
        output = create_password(user_input)
    
    entropy = entropy(ALL_LETTERS_DIGITS, output)
    time = time(ALL_LETTERS_DIGITS, output)

    return print(f"Your password is {output}\nIt has an entropy of {entropy}.\nIt will take about {time} years to crack using brute-force.")

if __name__ == "__main__":
    main()
