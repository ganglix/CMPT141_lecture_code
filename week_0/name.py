import random

name_lis = []
with open("namelist.csv") as f:
    for line in f:
        name_lis.append(line)

emoji_lis = ["\U0001F600", "\U0001F602", "\U0001F605", "\U0001F609", "\U0001F914", "\U0001F60E"]
name = random.choice(name_lis)
emoji = random.choice(emoji_lis)

print(emoji, name)
