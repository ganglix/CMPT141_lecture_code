# how to define a function
# creating functions: parameter, arguments, return
## things I want to mention: indentation, position, scope, function calling function

def add_func(par1, par2):
    # do something what takes 1000 lines of code
    res = par1 + par2
    print(f"par1 is {par1}")
    return res

# value = add_func(10, 20)
# print(value)
# under the hood (inside the function)
# par1 = 10
# par2 = 20
# res = 10 + 20
# above the hood (outside the function, global scope)
# value = 30

# print(par1)

def add_calculator():
    par1 = float(input("input a number: "))
    par2 = float(input("input a number: "))
    return par1 + par2

def another_func():
    ans = add_calculator()
    return ans

print(another_func())