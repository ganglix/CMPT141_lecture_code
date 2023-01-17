# Define Python functions for the following scenarios:
# (a) Function say_hello() that prints "Bonjour" to the screen
def say_hello():
    print("Bonjour")
say_hello()

# (b) Function named copycat() that takes a phrase
# parameter and prints its value to the screen five times (hint newbie,*)
def copycat(phrase):
    phrase_new = phrase + " "
    print(phrase_new * 5)

# copycat("meow")

# (c) Function named high_score() that takes three integer
# parameters and returns the highest value
def high_score(p1, p2, p3):
    highest_value = max(p1, p2, p3)
    return highest_value

print( high_score(2, 1, 3) )