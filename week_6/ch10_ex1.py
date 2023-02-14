# A given list called pkg_weights contains weights of parcels
# (in lbs) queued for shipping. Write Python code that:
# (a) Creates list light_pkgs of parcels that weigh less than 5
# lbs from pkg_weights
# (b) Removes parcels from pkg_weights that exceed 15 lbs
# (c) Print the:
# • contents of light_pkgs in ascending order
# • number of parcels in light_pkgs
# • number of parcels removed from pkg_weights

pkg_weights = [2, 6, 8, 34, 56, 67, 4, 2, 33]

# (a) Creates list light_pkgs of parcels that weigh less than 5
light_pkgs = []
for p in pkg_weights:
    if p < 5:
        light_pkgs.append(p)
print(light_pkgs)

# (b) Removes parcels from pkg_weights that exceed 15 lbs
# for p in pkg_weights:   # iterating over a changing list, BIG mistake!!!
#     if p > 15:
#         pkg_weights.remove(p)
# print(pkg_weights)

# # use a clone!!! (advanced!)
# pkg_weights_copy = pkg_weights[:]  # or use pkg_weights.copy()
# for p in pkg_weights_copy:
#     if p > 15:
#         pkg_weights.remove(p)
# print(pkg_weights)

# not use a clone
heavy_pkgs = []
for p in pkg_weights:
    if p > 15:
        heavy_pkgs.append(p)

for p in heavy_pkgs:
    pkg_weights.remove(p)
print(pkg_weights)


# (c) Print the:
# • contents of light_pkgs in ascending order
# • number of parcels in light_pkgs
# • number of parcels removed from pkg_weights


light_pkgs.sort()
print(light_pkgs)
print("number of light packages:", len(light_pkgs))

# print("number of heavy parcels removed ", count, "or", len(heavy_pkgs))












# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~things I want to mention
# Modifying list while iterating DO NOT DO IT
# dont change list if possible





