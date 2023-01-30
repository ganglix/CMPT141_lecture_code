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
# white box reasoning

























# # an fancy way to organize your test cases using list of dictionaries (revisit this after we cover list and dict)
# test_suite =[
#     {"input": "a"*8,
#     "output": False,
#     "reason": "trigger line 11, length of the password is less than 9"
#      },
#
#     {"input": "a" * 19,
#      "output": False,
#      "reason": "trigger line 11"
#      },
#
#     {"input": "12_",
#      "output": False,
#      "reason": "trigger line 13 if statement"
#     }
# ]
# for test_case in test_suite:
#     res = is_valid_password( test_case["input"] )
#     if res == test_case["output"]:
#         print("fault found!", test_case['reason'])
#         print("    expected: ", test_case["output"])
#         print("    returned: ", res)
#         print()
#     else:
#         print("all tests passed!")
