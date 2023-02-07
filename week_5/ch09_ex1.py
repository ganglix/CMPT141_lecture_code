# Write Python code which asks a user to input a string from
# the console until it is identical to pre-defined string passcode.
# When this occurs, print the number of attempts made to
# enter the correct string. e.g. "3 attempt(s) made."

# passcode = "cmpt141"
# code = input("input the passcode: ")
# n_attempts = 1
#
# while code != passcode:
#     code = input("input the passcode: ")
#     n_attempts += 1
# print(f"{n_attempts} attempt(s) made.")

passcode = "cmpt141"
n_attempts = 0

condition = True
while condition:
    code = input("input the passcode: ")
    n_attempts += 1
    if code == passcode:
        condition = False




# Bonous: another option to stop a while loop [not covered in the textbook]



