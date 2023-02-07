# Control Flow: Repetition
# what is a computer good at?
# repeat till what? when?


# while loop starts and stops according to a condition
## things I want to mention: condition boolean, while/if, keep checking(eg.)

# counting example
count = 0
# if count < 10:
#     count = count + 1
#     # keep doing this
#     print(f"count={count}")
#
# if count < 10:
#     count = count + 1
#     # keep doing this
#     print(f"count={count}")

while count < 10:
    print(f"count={count}")
    count = count + 1
print(f"after the loop is done: count={count}")

count = 0
condition = True
while condition:
    print(f"count={count}")
    count = count + 1
    if count == 10:
        condition = False



# for : repeat over a sequence
## mention types of sequence: string, range, list, dict

# for item in "cmpt141":
#     print(item)

# for i in range(1, 4, 1): # 1 2 3
#     print(i)

# range(3) # range(0,3,1), range(0,3)
# for i in range(5, 1, -1):
#     print(i)

print(type(range(3)))
# repeat for 20 times

for count in range(20):
    # do something
    print(count)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# make the Codeflow
# while loop
i = 1
while i < 10:
    i = i * 2
print(i)

"""
i = 1
while 1 < 10
i = 1 * 2
while 2 < 10
i = 2 * 2
while 4 < 10
i = 4 * 2
while 8 < 10
i = 8 * 2
while 16 < 10
print(16)
"""


# for loop
for c in "PIKA":
    print(c)
print("hooray!")

"""
for c in "PIKA"
c = "P"
print("P")
c = "I"
print("I")
c = "K"
print("K")
c = "A"
print("A")
print("hooray!")
"""

# word = "PIKA"
# end_index = len(word) - 1
# current_index = 0
# while current_index <= end_index:
#     print(word[current_index])
#     current_index += 1
