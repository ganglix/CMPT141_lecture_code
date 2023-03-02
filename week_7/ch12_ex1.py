# Topic(s): Reading Files
# read file and create a list of dictionaries to store data
# looks like this:
# scientists = [{"name": "Isaac Newton",
#                "birth_year": 1643,
#                "death_year": 1727},
#               {"name": "Albert Einstein",
#                "birth_year": 1879,
#                "death_year": 1955}]

# ~~~~~~~~~~~~open~~~~~~~read~~~~~~close~~~~routine~~~~~~~~

# open file for reading

# read in all scientist data and put in a list of records

# done reading , close file


































# ~~~~~~~ use with statement~~~~~~~~~~~~~~~~~

# # open file for reading
# with open("./subfolder/scientists_data.txt", "r") as f:
#     # read in all scientist data as list of records
#     # create scientist record
#     scientist = []
#     for line in f:
#         # removing trailing newline & parse data as list
#         line = line.rstrip().split(",")
#         # add scientist record to scientists listing
#         scientist.append({"name": line[0],
#                           "birth_year": line[1],
#                           "death_year": line[2]})
