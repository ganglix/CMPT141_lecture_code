# Write a Python function that accepts string parameter s and
# prints whether s has an even or odd amount of characters.
# Sample function console output:
# "Dog" has an odd number of characters.

def check_char(s):
    if len(s) % 2 != 0:
        print(s, "has an odd number of characters")
    # if len(s) % 2 == 0:
    else:
        print(s, "has an even number of characters")

# check_char("cmpt 141")
# things to mention  character vs non-space character

def check_char_no_space(s):
    s = s.replace(" ", "")
    if len(s) % 2 != 0:
        print(s, "has an odd number of characters")
    # if len(s) % 2 == 0:
    else:
        print(s, "has an even number of characters")

check_char("cmpt 141")
check_char_no_space("cmpt 141")






