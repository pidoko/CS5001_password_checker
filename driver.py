"""
Final Project: Password generator and checker    
=======================
Course:   CS 5001
Semester: Fall 2023
Student:  Peter Idoko

Functions that calculate password entropy and brute-force crack time.
Main function that utilizes the functions in the generator.py file to run the password generator
"""

# Runs the password generator
import sys, random, math
from string import digits, ascii_letters, punctuation
from generator import check_length, check_value

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
    # Estimate at how long it takes to crack the password using a PC with a 3.5GHz rate of attempts
    answer = round(((len(ALL_LETTERS_DIGITS) ** len(output)) / (3.154 * (10 ** 8) * (10 ** 9))), 0)  # years to crack based on 1billion passwords per second
    return answer

def main():
    print("Welcome to the Password Generator.")
    selection = input("Press 1 to create your password and any other key for a computer generated password")
    if selection == '1':
        user_input = input("Create a password of minimum 12 characters combining lowercase, uppercase, digits and symbols")
        if check_length(user_input) == 1:
            output = type_password(user_input)
        else:
            print("Password length must be longer than 11.")
    else:
        user_input = int(input("How long do you want your password to be? minimum 12: "))
        if check_value(user_input) == 1:
            output = create_password(user_input)
            entropy_value = entropy(ALL_LETTERS_DIGITS, output)
            time_value = time(ALL_LETTERS_DIGITS, output)
            answer = "Your password is "+output+"\nIt has an entropy of "+str(entropy_value)+".\nIt will take about "+str(time_value)+" years to crack using brute-force."
            print(answer)
            return 1
        else:
            print("Password length must be longer than 11.")
            return 0

    return 0

if __name__ == "__main__":
    main()
