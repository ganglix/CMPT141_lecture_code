# Write a Python function that accepts string parameter s and
# prints whether s has an even or odd amount of characters.
# Sample function console output:
# "Dog" has an odd number of characters.

# def check_char(s):
#     if len(s) % 2 == 0:
#         print(f"{s} has an even number of characters")
#     if not len(s) % 2 == 0:
#         print(f"{s} has an odd number of characters")

# def check_char(s):
#     if len(s) % 2 == 0:
#         print(f"{s} has an even number of characters")
#     else:
#         print(f"{s} has an odd number of characters")

def check_char(s):
    s_clean = s.strip()
    if len(s_clean) % 2 == 0:
        print(f"{s} has an even number of characters")
    else:
        print(f"{s} has an odd number of characters")

check_char("star ")

# n = 5
# if n < 10:
#     print("n < 10")
# elif n < 6:
#     print("n < 6")
# else:
#     print("no conditions satisfied")
#
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# if n < 10:
#     print("n < 10")
# if n < 6:
#     print("n < 6")
# else:
#     print("no conditions satisfied")


















# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # alternative solution
# def char_check(s):
#     number = len(s.strip())
#     if number // 2 == 0:
#         message = "even"
#     else:
#         message = "odd"
#     print(f"{s.strip()} has as an {message} number of characters")
