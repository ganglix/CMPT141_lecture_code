# lists and tuples

# create a list

lis = ["a", "b", "c"]  # the element in a list can be anything

# print(type( [] ))
# print(lis)
# print(range(3))
# print(list(range(3)))


# indexing and slicing
# print(
# "computer"[0],
#     lis[0:2],
#     lis[-1],
#     lis[:100],
#     sep="\n"
# )


# add an item: .append(), +, .extend()
# new_thing = lis.append("d")
# print(f"new_thing: {new_thing}" )
#
# lis.append("d")   # in-place change, does not return a new list
# print(lis)
# print(lis + ['e', 'f'])
# # lis.extend('gee')
# lis.extend(["gee","eich"])
# print(lis)
#
#
#
# # remove an item: .remove(), del, .pop()
# lis.remove('eich')
# lis.append('a')
# print(lis)
# lis.remove('a')
# print(lis)
#
# del lis[0]
# print(lis)
#
# being_removed = lis.pop()  # remove and return the last item
# print(lis)
# print(being_removed)
#
# being_removed = lis.pop(1)  # remove and return the  item with index 1
# print(lis)
# print(being_removed)


# # locating an item: index()
# c_idx = lis.index('c')
# print(c_idx)


# sorting: .sort()
# lis = ["c", "a", "b"]
# lis.sort()
# print(lis)
# lis.sort(reverse= True)
# print(lis)

# lis.append(10)
# lis.sort()
# print(lis)

# new_lis = sorted(lis)
# print(new_lis)

# list is mutable !


# function with list


# codeflow
# L = [1, 2, 3, 4, 5, 6]
# for value in L:        # do not do it! do not iterate over a changing list
#     L.remove(value)
# print(L)


# # doomed?
# L = [1, 2, 3, 4, 5, 6]
# another_L = L   # this will NOT create a new list
# L.remove(1)
# print(another_L)
#
# L = [1, 2, 3, 4, 5, 6]
# # another_L = L[:]   # this will create a new list clone
# another_L = L.copy()   # this will also create a new list clone
#
# for value in another_L:
#     L.remove(value)
# print(L)
#
#
# tu = ("a", "b", "c")


lis = [1, 1, 2, 3]
lis_copy = lis[:]
for item in lis:
    lis_copy.remove(item)
    if item in lis_copy:
        print("duplicate: ", item)
