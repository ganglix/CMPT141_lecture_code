def is_valid_password(password):
    """
    determines if password meets these constraints:
    - 9-18 characters long
    - no Underscores or minus _,-
    password: string to check validity of
    return: True if password satisfies constraints
    """
    is_valid = True

    if len(password) < 9 or len(password) > 18:
        is_valid = False
    if "_" in password:
        is_valid = False
    if "-" in password:
        is_valid = False

    return is_valid

# Testing - white box
# white box reasoning: cover important lines of code
# branching if-else, loop(case: no run, run once, run max times)


reason = "trigger line 11, if statement"
inputs = "a" * 8
outputs = False
result = is_valid_password(inputs)
if result != outputs:
    print("fault found!")
    print("test case input: ", inputs)
    print("expected output: ", outputs)
    print("got: ", result)
    print("test reason: ", reason)


reason = "trigger line 11, if statement"
inputs = "a" * 19
outputs = False
result = is_valid_password(inputs)

if result != outputs:
    print("fault found!")
    print("test case input: ", inputs)
    print("expected output: ", outputs)
    print("got: ", result)
    print("test reason: ", reason)

reason = "trigger line 13, if statement"
inputs = "_"
outputs = False
result = is_valid_password(inputs)
if result != outputs:
    print("fault found!")
    print("test case input: ", inputs)
    print("expected output: ", outputs)
    print("got: ", result)
    print("test reason: ", reason)

reason = "trigger line 15, if statement"
inputs = "-"
outputs = False
result = is_valid_password(inputs)
if result != outputs:
    print("fault found!")
    print("test case input: ", inputs)
    print("expected output: ", outputs)
    print("got: ", result)
    print("test reason: ", reason)




# an fancy way to organize your test cases using list of dictionaries (revisit this after we cover list and dict)
test_suite =[
    {"input": "a"*8,
    "output": False,
    "reason": "trigger line 11, length of the password is less than 9"
     },

    {"input": "a" * 19,
     "output": False,
     "reason": "trigger line 11"
     },

    {"input": "12_",
     "output": False,
     "reason": "trigger line 13 if statement"
    }
]

test_pass = True
for test_case in test_suite:
    res = is_valid_password( test_case["input"] )
    if res != test_case["output"]:
        print("fault found!", test_case['reason'])
        print("    expected: ", test_case["output"])
        print("    returned: ", res)
        print()
        test_pass = False

if test_pass:
    print("All test passed!")
