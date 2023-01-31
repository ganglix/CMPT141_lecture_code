# Write a Python function which accepts integer parameter
# grade and prints to the console:
# • "A+" if grade is between 100 and 95
# • "A" if grade is between 94 and 85
# • "B" if grade is between 84 and 75
# • "C" if grade is between 74 and 65
# • "D" if grade is between 64 and 50
# • "F" otherwise

# def letter_grade(grade):
#     """
#     Print the letter grade of a number grade
#     :param grade: int, numeric grade
#     :return: None
#     """
#     if grade <= 100 and grade >= 95:
#         print("A+")
#     elif grade <= 94 and grade >= 85:
#     # if grade <= 94 and grade >= 85:
#         print("A")
#     elif grade <= 84 and grade >= 75:
#         print("B")
#     elif grade <= 74 and grade >= 65:
#         print("C")
#     elif grade <= 64 and grade >= 50:
#         print("D")
#     else:
#         print("F")


# mention if-if else-if if-else,

# discussion: room to improve?

def letter_grade(grade):
    """
    Print the letter grade of a number grade
    :param grade: int, numeric grade
    :return: None
    """
    from math import ceil
    grade = ceil(grade)

    if grade <= 100 and grade >= 95:
        print("A+")
    elif grade <= 94 and grade >= 85:
    # if grade <= 94 and grade >= 85:
        print("A")
    elif grade <= 84 and grade >= 75:
        print("B")
    elif grade <= 74 and grade >= 65:
        print("C")
    elif grade <= 64 and grade >= 50:
        print("D")
    else:
        print("F")

letter_grade(94.1)
