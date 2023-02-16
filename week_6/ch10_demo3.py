# Up until now, only immutable data types have been passed
# as arguments to functions. What happens when we pass
# mutable data?
# Let us observe the effect on an input variable before,
# during, and after a function call that changes the value.


def update_grades(grades):
    grades[0] = grades[0] + 2

classgrades = [48, 53, 95, 72]
#
# new_grades = update_grades(classgrades)
#
# print(classgrades)
# print(new_grades)

# -----------------------------------------

def update_grades_for_all(grades):
    grades = [g+2 for g in grades]

new_grades = update_grades_for_all(classgrades)

print(classgrades)
print(new_grades)


# -----------------------------------------
# # does this operation create a new list?
#
a = [1, 2, 3]
b = a
# do some operation about a
a[0] += 10
print(a)
print(b)

a = [1, 2, 3]
b = [item for item in a]  # same as a.copy()
#
# # do some operation about a
a[0] += 10
print(a)
print(b)
#

