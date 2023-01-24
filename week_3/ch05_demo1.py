# This demonstration shows you how to call methods on string objects.

# Let's do this in the interactive mode in console

# initialize some variables to play with
url = "www.engineering.usask.ca"

# # find the location of the first period in the url
# def find(s):
#     search for "."
#     return the location of the search result
print(url.find('.'))
print(url.find('ing'))

# count the number of periods in the url
print(url.count('.'))

# remove white space
print(" computer science ".strip())
print(" computer science ".rstrip())
print(" computer science ".lstrip())

# count the number of characters in the url after removing "www."
# (!gotta be careful - don’t just assume a function does what you think!)
print("use rstrip: ", url.lstrip("w."))


# print(len(url.replace("www.", "")))
#
# print(len(" computer science ".replace(" ", "")))
#
# # # more methods:
# # .upper()
# print('aa'.upper().lower())
# # .lower()
# # when are they useful
# # immutable, they create a copy
# print(url)
# new_url = url.replace("www", "funny")
# print(url)
# print(new_url)
#
#
# # how do I know what kind of methods are out there? How do I know the syntax/usage?
#
# from pprint import pprint
# pprint(dir(url))
# print(help(url.find))
# print(url.find.__doc__)