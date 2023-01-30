def is_valid_username(username):
    """
    determines if username meets these constraints:
    - 1-18 characters long
    - can be letters and/or numbers
    - underscore is allowed if it’s not the first character
    username: string to check validity of
    return: True if username satisfies constraints
    """

# Testing - black box
# black box reasoning

#     - 1-18 characters long
"""
input: "a"
output(expected): True
reason: string contains one char

input: "a" * 18
output: True
reason: string contains 18 chars

input: ""
output: False
resaon: empty string is not valid

input: "a"*19
output: False
reason: 19 chars out of range
"""


#- underscore is allowed if it’s not the first character
"""
input: "_"
output: False
reason: string starts with _, and length is one.

input: "a_a"
output: True
reason: string has a _ in the middle

input: "a_"
output: True
reason: string has a _ at the end

"""

# test driver example

inputs = "a" * 18
output_expected = True
reason = "string contains 18 chars"

result = is_valid_username(inputs)
if result != output_expected:
    print("fault found!",
          "test case input: ", inputs,
          "expected: ", output_expected,
          "got: ", result)

# Jan 30 test drive finished.
























# ~~~~~~~~~~~~~~~~after dictionary~~~~~~~~~~~~~~~~~~~~


# dictionary of test case suite to feed into test driver loop
test_suite = [
    # call for length -zero username (empty string)
    {"inputs": [""],
     "outputs": False,
     "reason": "length must be be 1-18 characters"},

    # call for length -one username of invalid character
    {"inputs": ["+"],
     "outputs": False,
     "reason": "username can only contain letters , numbers , underscores"},

    # call for length -one username of a letter
    {"inputs": ["a"],
     "outputs": True,
     "reason": "username is allowed to have letters"},

    # call for length -18 username of numbers only with trailing underscore
    {"inputs": ["0" * 17 + "_"],
     "outputs": True,
     "reason": "username is allowed to have numbers and trailing underscore"},

    # call for length -three username with letter , number , underscore
    {"inputs": ["a_0"],
     "outputs": True,
     "reason": "username is allowed to have letters , numbers , underscore"},

    # call for length -three username with letter , number , starting underscore
    {"inputs": ["_a0"],
     "outputs": False,
     "reason": "can’t start with underscore"},

    # call for length -18+ username of letters and numbers
    {"inputs": ["a0" * 18],
     "outputs": False,
     "reason": "can’t have more than 18 characters"}
]
# a generic loop for test drivers
# the inputs are in a list , so it has to be modified
for test in test_suite:
    inputs = test["inputs"]
    result = is_valid_username(inputs[0])

    if result != test["outputs"]:
        print(f"Testing fault: is_valid_username () returned {result} on inputs {inputs}"
              f"\ntest reason: {test['reason']})\n")
