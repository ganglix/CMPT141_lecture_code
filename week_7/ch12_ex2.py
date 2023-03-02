# Topic(s): Writing Files
# store’s item inventory to write (no "stock" means not carried by store)

# expected output
# Healing Herb,Heals minor wounds,25,0.25,5
# Smoke Cloud,Creates distraction,65,1.15,

inventory = [
    {"name": "Healing Herb", "desc": "Heals minor wounds",
     "cost": 25, "weight": 0.25, "stock": 5},
    {"name": "Antidote Vial", "desc": "Cures poisonous wounds",
     "cost": 50, "weight": 1.25, "stock": 3},
    {"name": "Paralysis Herb", "desc": "Paralyzes enemy when thrown",
     "cost": 75, "weight": 0.35},
    {"name": "Smoke Cloud", "desc": "Creates distraction for escape",
     "cost": 65, "weight": 1.15},
    {"name": "Fairie Dust", "desc": "Casts light in the darkness",
     "cost": 100, "weight": 0.4, "stock": 3},
]

# open file for writing
f = open("store_inventory.txt", 'w')

# for every item in inventory , write out its details on its own line



# done writing , so close the file
f.close()





























# -------------------- alternative way ------------------------------------
# # open file for writing
# f = open("store_inventory.txt", 'w')
#
# # for every item in inventory , write out its details on its own line
# for item in inventory:
#     # every item has a name , desc , cost , weight to write
#     line_to_write = ','.join([item["name"], item["desc"], str(item["cost"]), str(item["weight"])])
#     f.write(line_to_write)
#     f.write(',')
#     # if store carries item , write its stock , otherwise leave blank column
#     if "stock" in item:
#         print(item)
#         f.write(str(item["stock"]))
#     f.write("\n")
# # done writing , so close the file
# f.close()



# #~~~~~~~~~~ advanced dictionary .get() method~~~~~~~~~~~~~
#
# for item in inventory:
#     line_to_write = ','.join([item.get("name"),
#                               item.get("desc"),
#                               str(item.get("cost")),
#                               str(item.get("weight")),
#                               str(item.get("stock",''))])
#     f.write(line_to_write)
#     f.write('\n')
