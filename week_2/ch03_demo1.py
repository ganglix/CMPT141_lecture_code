# In this demonstration we will show how to use the console
# input function to obtain answers to simple questions and
# convert the input to the desired data type.

# example 1
# sad_story = input("Tell me something that makes you sad: ")
# print("Then, let's make it something positive")
# print("|", sad_story ,"|")
# print("|", sad_story ,"|", sep="")
# print(f"|{sad_story}|")  # bonus: super cool f-string, only available after python 3.6 (out of scope of CMPT141)


# example 2
number_1 = int(input("type an integer number: "))
number_2 = int(input("type another number: "))
print("the sum is: ", number_1 + number_2)


# # example 3
#
# # title
# print("If I Were Super Wealthy Simulator")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print()
#
# # prompt user for their name
# name = input("What is your name?: ")
# print("Hello", name, "! We're going to gather some data on you and predict your life")
# print()
#
# # prompt user for some more data about themselves
# animal = input("What is your favourite animal?: ")
# number = int(input("What is your favourite number (please give an integer)?"))
# float_number = float(input("What is another number you like (this time, give a float number)?"))
# print()
#
# # print out the scenario
# print("Hello", name, ". If you were super wealthy, my guess is you would buy", number, animal)
# print("You would make sure that they live in", float_number, "degree celsius weather.")
# print("Should we be concerned? Possibly")