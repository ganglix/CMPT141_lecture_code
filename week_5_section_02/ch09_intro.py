# Control Flow: Repetition
# what is a computer good at?
# repeat till what? when?


# while - use a condition to make it start and stop
## things I want to mention: condition boolean, while/if, keep checking(eg.)
# counting example
# count = 0
# while count < 10:
#     print("count = ", count)
#     count = count + 1
#
# print(f"after the loop is done, count = {count}")

count = 0
condition = True
while condition:
    print("count = ", count)
    count = count + 1
    if count == 10:
        condition = False

print(f"after the loop is done, count = {count}")

# while True: # inf loop
#     # do something



# for  loop stops when it finishes a sequence
## mention types of sequence: string, range, list, dict

# for letter in "hello":
#     print(letter)

# for i in range(10, 50, 3): # 10,13,16...
#     print(i)

# for i in range(10+1): # 0-10 included
#     print(i)

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
# for c in "PIKA":
#     print(c)
# print("hooray!")
