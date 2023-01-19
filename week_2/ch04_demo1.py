# Write a docstring for the following function definition (abs()
# returns the absolute value of a number):

def print_smaller_absolute(num1, num2):
    """
    This function takes two numbers and return the absolute value of the
    smaller number. It also prints out the message showing that value.
    :param num1: a number, first number to compare
    :param num2: a number, second number to compare
    :return: a number, absolute value of the smaller number
    """
    small_abs = abs(min(num1, num2))
    print("Absolute value of smaller number: ", small_abs)
    return small_abs


answer = print_smaller_absolute(-20, 2)
print(answer)
# things not to do.
# afraid to lose marks
# example in an engineering software program?
# style




# help(max)
# print(max.__doc__)
# print(print_smaller_absolute.__doc__)









#~~~~~~~~~~~~~~~~~~~~~~~~things I want to mention~~~~~~~~~~~~~~~~~~
# sphinx, __doc__, help, hover, pen and paper




