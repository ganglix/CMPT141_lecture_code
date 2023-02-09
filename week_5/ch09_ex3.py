# Write a Python function that uses a for-loop to print the
# number of times each lowercase vowel (a,e,i,o,u) occurs in a
# string s. e.g. "piece" prints "a:0 e:2 i:1 o:0 u:0".

s = "piece"
# show solution for letter "e"
# not using for-loop
# print("e:", s.count("e"), sep="")
# print(f"e:{s.count('e')}")


# using a for-loop
# a_count = 0
# e_count = 0
# for letter in s:
#     if letter == "e":
#         e_count += 1
#     if letter == "a":
#         a_count += 1
#
# print(f"e:{e_count}")
# print(f"a:{a_count}")






# # code flow nested for-loop
total = 0
for i in range(2):  # 0, 1
    for j in range(2): # 0, 1
        total = total + 1
print(total)

# """
# total = 0
# for i in range(2)
#     i = 0
#     for j in range(2)
#         j = 0
#         total = 0 + 1
#         j = 1
#         total = 1 + 1
#     i = 1
#     for j in range(2)
#         j = 0
#         total = 2 + 1
#         j = 1
#         total = 3 + 1
# print(4)
# """
"""
total = 0
for i in range(2)
i = 0
for j in range(2)
j = 0
total = 0 + 1
j = 1
total = 1 + 1
i = 1
for j in range(2)
j = 0
total = 2 + 1
j = 1
total = 3 + 1
print(4)
"""

# mention debugger