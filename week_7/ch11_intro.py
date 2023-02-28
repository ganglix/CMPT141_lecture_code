# dictionary : hash map in python

# Store and look up data
phone_list = ['306123456', '3068888888']
name_list = ['Mark', 'Gang']

# for idx in range(len(name_list)):
#     if name_list[idx] == "Mark":
#         print(phone_list[idx])
#
# print(phone_list[name_list.index("Mark")])

phone_book = { 'Mark': '306123456',
               'Gang': '3068888888'}

# print( phone_book['Mark'] )
phone_book['Adam'] = '911'
print(phone_book)


# KEYS  # use consistent key
# any immutable data type: int, float, string, tuple,
print({1 : "data point"})


# VALUES
# any data type
contact_book = { 'Mark': {'number':'306123456', 'email':'mark@usask.ca'},
               'Gang': '3068888888'}

print(contact_book['Mark']['email'])

# dictionary methods
print(contact_book.values())

# No key found?
# use unique keys
# d = {'mark': 98, 'mark':99}
# print(d['mark'])


# things I want to mention: mutable, no order, key is the key