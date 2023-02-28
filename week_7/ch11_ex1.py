# Exercise 1

# Suppose you have a dictionary of survey responses:
# •keys are student names
# •values are favourite ice cream flavours (one of
# "chocolate", "vanilla", "strawberry")
# Write a function that takes a dictionary of survey responses
# and returns a new dictionary where:
# •keys are ice cream flavours
# •values are number of students with that favourite flavour

survey = {"Christopher": "vanilla",
          "Ty": "vanilla",
          "Muhammed": "chocolate",
          "Ani": "vanilla",
          "Gang": "chocolate"}

# def icecream_survey(survey):
#     result = {}  # key, flavour, value votes
#     for name in survey:
#         flavour = survey[name]
#         if flavour in result:
#             result[flavour] += 1
#         else:
#             result[flavour] = 1
#     return result

# def icecream_survey(survey):
#     result = {}  # key, flavour, value votes
#     for name in survey:
#         flavour = survey[name]
#         if flavour not in result:
#             result[flavour] = 0  # initialize flavour record
#         result[flavour] += 1
#     return result

def icecream_survey(survey):
    result = {}  # key, flavour, value votes
    for flavour in survey.values():
        if flavour not in result:
            result[flavour] = 0  # initialize flavour record
        result[flavour] += 1
    return result

count_summary =  icecream_survey(survey)

print(count_summary)