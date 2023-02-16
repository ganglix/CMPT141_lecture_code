# We have two separate lists, containing province names and
# their matching populations.
# provs = ["AB", "BC", ...]
# pops = [4200, 4700, ...]
# Take the data from these lists and construct a list of lists
# called prov_pops where each sublist has exactly 2 items: the
# province, followed by its population
# [ ["AB", 4200], ["BC", 4700], ... ]

provs = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]
pops = [4200, 4680, 1290, 750, 530, 40, 940, 40, 13790, 150, 8260, 1130, 40]

# # create a list first, and use for loop to append
# prov_pops = []
#
# for i in range(len(provs)):
#     sublist = [ provs[i], pops[i] ]
#     prov_pops.append(sublist)
# print(prov_pops)


# things I want to mention (pythonic). list comprehension later

prov_pops = []
for this_prov, this_pop in zip(provs, pops):
    prov_pops.append([this_prov, this_pop])
print(prov_pops)


