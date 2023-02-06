# Write Python code which asks a user to input a string from
# the console until it is identical to pre-defined string passcode.
# When this occurs, print the number of attempts made to
# enter the correct string. e.g. "3 attempt(s) made."

# passcode = "cmpt141"
# code = input("input the passcode: ")
#
# # if code == passcode: let's not do this
# #
# n_attempts = 1
# while code != passcode:
#     code = input("input the passcode: ")
#     n_attempts += 1
#
# print(f"{n_attempts} attempt(s) made.")
#
# passcode = "cmpt141"
# # initial a wrong code
# code = "absolutely_wrong_!@#$"
# n_attempts = 0
# while code != passcode:
#     code = input("input the passcode: ")
#     n_attempts += 1
#
# print(f"{n_attempts} attempt(s) made.")


# Bonous: another option to stop a while loop [not covered in the textbook]
passcode = "cmpt141"
n_attempts = 0
while True:
    code = input("input the passcode: ")
    n_attempts += 1
    if code == passcode:
        break   # it will stop the loop right here without checking while
        print("this message will show up the break failed")

print(f"{n_attempts} attempt(s) made.")


