# Define Python functions for the following scenarios:
# (a) Function say_hello() that prints "Bonjour" to the screen
def say_hello():
    """
    This function prints a message: "Bonjour"
    :return: no returned value
    """
    print("Bonjour")
say_hello()

def greeting(message):
    print("Bounjour", message)

# (b) Function named copycat() that takes a phrase
# parameter and prints its value to the screen five times (hint newbie,*)

def copycat(phrase):
    """
    It takes a phrase and prints it five times
    :param phrase: a string, phrase to print
    :return: None
    """
    phrase_new = phrase + " "
    print(phrase_new * 5)

# copycat("meow")

# (c) Function named high_score() that takes three integer
# parameters and returns the highest value
def high_score(p1, p2, p3):
    """
    It takes three numbers and returns the highest number
    :param p1: number, first number to compare
    :param p2:
    :param p3:
    :return: number, highest value of the three input numbers
    """
    highest_value = max(p1, p2, p3)
    return highest_value

print( high_score(2, 1, 3) )



# (c) Function named high_score() that takes three integer
# parameters and returns the highest value
