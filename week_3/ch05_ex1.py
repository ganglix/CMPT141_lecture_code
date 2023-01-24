# Given variables:
nation = "Canada !!!"
nation_motto = "From Sea to Sea"

# Write expressions to:
# (a) Determine if nation has only alphabetic letters and digits
print(nation.isalnum())

# (b) Remove "!" characters and whitespace from nation
print(nation.replace("!", "").replace(" ", ""))

# (c) Find the location of the first "Sea" substring in nation_motto
print(nation_motto.find("Sea"))

