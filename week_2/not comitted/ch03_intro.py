# What Python function displays text on the console? (how about the return value?)
# print("hello")
# print( print("hello") )  #print() has no return value


# What Python function retrieves user input from the
# console (keyboard)?

# number = input("type an integer: ")
# print("the number you just typed in is: ", number)

# example
# sad_story = input("Tell me something that makes you sad: ")
# print("Then, let's make it something positive")
# print("|", sad_story ,"|")
# print("|", sad_story ,"|", sep="")
# print(f"|{sad_story}|")  # super cool f-string, only available after python 3.6


# another example
number_1 = int(input("type an integer number: "))
number_2 = int(input("type another number: "))
print("the sum is: ", number_1 + number_2)
