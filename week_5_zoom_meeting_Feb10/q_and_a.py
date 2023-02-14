# from new_file import my_print, message
# my_print()
# print(message)

def my_division(a, b):
    """
    It returns the quotient a/b
    :param a: a number, dividend
    :param b: a number, divisor
    :return:
    """
    return a + b

# codelab question:
# you are asked to make a function all with a test case \
# that you think will reveal the error

# corrct answer: almost ANY test cases
# my_division(1,1)


def my_new_division(a, b):
    """
    It returns the quotient a/b
    :param a: a number, dividend
    :param b: a number, divisor
    :return:
    """
    return a // b

# codelab question:
# you are asked to make a function all with a test case \
# that you think will reveal the error

# corrct answer:
# my_new_division(1, 2)

def my_next_division(a, b):
    """
    It returns the quotient a/b
    :param a: a number, dividend
    :param b: a number, divisor
    :return:
    """
    return a / b

# codelab question:
# you are asked to make a function all with a test case \
# that you think will reveal the error

# corrct answer:
# my_next_division(1, 0)




def my_newest_division(a, b):
    """
    It returns the quotient a/b, and print a message when b = 0
    :param a: a number, dividend
    :param b: a number, divisor
    :return:
    """
    if b == 0:
        print("can not be divided by zero!")
    else:
        return a / b

# codelab question:
# you are asked to make a function all with a test case \
# that you think will reveal the error

# corrct answer:
# how about my_newest_division(1, 0)
# no test case would reveal an error,
# because there is no error, and the function did its job, correctly.