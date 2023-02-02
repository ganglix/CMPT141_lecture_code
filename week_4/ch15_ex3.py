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
# white box reasoning : cover all lines of code (leave no stone unturned)
# important code line: if-else branching, loop ( zero run, one run, max number run)

# reason = "trigger line 11, if statement, make the condition True, password length is 8"
# inputs = "a" * 8
# outputs_expected = False
#
# reason = "trigger line 11, if statement, make the condition True, password length is 19"
# inputs = "a" * 19
# outputs_expected = False
#
# # not necessary, no else statement
# # reason = "trigger line 11, if statement, make the condition False, password length is 19, no - no _"
# # inputs = "a" * 13
# # outputs_expected = True
#
# reason = "trigger line 13, if statement, make the condition True, password contains _"
# inputs = "a_"
# outputs_expected = False
#
#
# reason = "trigger line 15, if statement, make the condition True, password contains -"
# inputs = "a-"
# outputs_expected = False



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
all_passed = True
for test_case in test_suite:
    res = is_valid_password( test_case["input"] )
    if res != test_case["output"]:
        print("fault found!", test_case['reason'])
        print("    expected: ", test_case["output"])
        print("    returned: ", res)
        print()
        all_passed = False

if all_passed:
    print("all tests passed!")

