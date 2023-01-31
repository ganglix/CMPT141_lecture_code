# Write a Python function that accepts string parameter s and
# prints whether s has an even or odd amount of characters.
# Sample function console output:
# "Dog" has an odd number of characters.

def check_char(s):
    if len(s) % 2 == 0:
        print(f"{s} has an even number of chars")
    # if len(s) % 2 != 0:
    else:
        print(f"{s} has an odd number of chars")

check_char("cmpt 141")


# things to mention  character vs non-white-space-char


def check_char_no_space(s):
    s = s.replace(" ", "")
    if len(s) % 2 == 0:
        print(f"{s} has an even number of chars")
    # if len(s) % 2 != 0:
    else:
        print(f"{s} has an odd number of chars")

check_char_no_space("cmpt 141")


# if condition:
#     # do something
# else:
#     if another condition:
#         # do another thing
#     else:
#         # do something else
#
# if:
# elif:
# else:
