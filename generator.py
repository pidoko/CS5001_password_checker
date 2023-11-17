# program to generate passwords

import sys, random
from string import digits, ascii_letters, punctuation

# original alphanumeric string with punctuations
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation

def main():
    answer = ''.join(random.choices(ALL_LETTERS_DIGITS, k = 10))
    return (answer)

if __name__ == "__main__":
    main()