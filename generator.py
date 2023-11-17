# program to generate passwords

import sys
from string import digits, ascii_letters, punctuation
from random import sample

# original alphanumeric string
ALL_LETTERS_DIGITS = digits + ascii_letters + punctuation
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))