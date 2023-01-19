# codeflows with function
# scope

status = "Healthy"
# print(f"before poisoned: {status}")
# def set_status(s):
#     # global status   # dont do it! very evil!!!!
#     status = s

# def set_status(s):
#     # status = s
#     return s
#
# status = set_status("Poisoned")
# print(f"after poisoned: {status}")
# print("after poisoned:", status)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(reminder: scope, return, dangerous thing to do, inplace)



# # inplace update with class/object  (advanced, not covered in cmpt141)

# class Pokemon:
#     def __init__(self, status):
#         self.status = status
#
#     def set_status(self, new_status):
#         self.status = new_status
#
# pikachu = Pokemon("healthy")
# print(f"before poisoned: {pikachu.status}")
#
# pikachu.set_status("poisoned")
# print("after poisoned:", pikachu.status)


text = "cmpt141"
print(type(text))

print(text.find("z"))

