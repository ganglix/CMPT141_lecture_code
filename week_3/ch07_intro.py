# Indexing and Slicing of !Sequences!
# "hello"
# [1, 2, 4, 'doesnt matter']
# (1, 2, 3)


# •What is indexing used for?
# •What does a positive index mean?
# •What does a negative index mean?
#    ________
#    87654321
#    01234567
s = "CMPT 141"
# print(s[2])
# print(s[-1])
# print(s[len(s)-1])

# •What is slicing used for?
# •What are the meanings of the First, second, and third
# numbers in a slicing operation?
#    ________
#    87654321
#    01234567
s = "CMPT 141"
# s[start: stop(exclusive): step]
# print(s[0: 3: 1])
# print(s[0: 3: 2])

# print(s[7: 0: -1])
# print(s[7: None: -1])
# print(s[7: : -1])
# print(s[: : -1])
# print(s[: : 1])
# print(s[:])

#     [         ]
#    ________
#    87654321
#    01234567
s = "CMPT 141"

print(s[2: 10])
print(s[0: 5: 3])
# I want to mention omitted value
