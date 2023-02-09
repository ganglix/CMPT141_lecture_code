# while vs. for
# In this demonstration, we’ll see a situation where using a
# while-loop is preferable to using a for-loop.

# password example

# initiate param
passcode = "cmpt141"
max_attempt = 3
code = input("input the passcode: ")
n_attempt = 1

# ask user to input passcode
while code != passcode and n_attempt <= (max_attempt-1):
    code = input("input the passcode: ")
    n_attempt += 1

# print message to user
if code == passcode:
    print(f"passcode is correct. {n_attempt} attempt(s) made")
else:
    print(f"maximum {n_attempt}/{max_attempt} attempts reached, your are locked out")



# bonus example testing-debugging SDLC

# write code
# testing
# if is_passed = False:
#     while not is_passed:
#         dubug
#         testing
#         if testing passed:
#             is_passed = True
# else:
#     done
