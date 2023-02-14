# List msgs contains sublists of the form [msg,days old]:
# msgs = [ ["Forgot the recipe again! #nofood",3],
# ["such a gluten #food #fivestar",10] ]
# Use list comprehensions to:
# (a) create list food_msgs of messages containing "#food"
# (b) create a new copy of food_msgs where messages are
# appended with "#yawn"

# Topic : List Comprehensions
# DEMO
# list of social media messages as sublists ( message , days since posted )


msgs = [["Forgot the recipe again! #nofood", 3],
        ["such a gluten #food #fivestar", 10],
        ["International #Food day! Hooray!", 1],
        ["Apple pie is bestest food", 5],
        ["lunchtime? #food #craving hits again", 9]]

# (a) create list food_msgs of messages containing "#food"

# for loop style:
food_msgs = []
for this_msg in msgs:
    if "#food" in this_msg[0]:
        food_msgs.append(this_msg)

print(food_msgs)

# list comprehension



# (b) create a new copy of food_msgs where messages are
# appended with "#yawn"
food_msgs_new = food_msgs.copy()
for m in food_msgs_new:
    m.append("#yawn")


# take a look at this list comprehension
# food_msgs_new = food_msgs.copy()
# returned = [m.append("#yawn") for m in food_msgs_new]

# print(food_msgs_new)
# print(returned)
