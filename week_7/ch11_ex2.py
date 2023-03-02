# Exercise 2

# Suppose we have dictionary availability:
# keys: friend’s name
# values: list of days they are available to play a game
# (a) Write a function that accepts an availability dictionary and returns a new dictionary mapping days to
# friends who can play that day.
# (b) Using the function from a):
# Find the day most friends can attend to play the game
# List who can and can not attend the session that day

availability = {"Neo": ["Monday"],
                "Morpheus": ["Sunday"],
                "Smith": ["Monday", "Tuesday"]}


def reverse_dict(avail_dict):
    schedule = {}  # day: friend
    for friend in avail_dict:
        days = avail_dict[friend]  # days is a list of day(s)
        for day in days:
            if day not in schedule:
                schedule[day] = []
            schedule[day].append(friend)  # append friend to list
    return schedule


week_schedule = reverse_dict(availability)

day_with_most_friends = ''
max_number_friend = 0

for day in week_schedule:
    if len(week_schedule[day]) > max_number_friend:
        max_number_friend = len(week_schedule[day])
        day_with_most_friends = day

print(f'max number {max_number_friend} of friends on {day_with_most_friends}')

attend = week_schedule[day_with_most_friends]
not_attend = [friend for friend in availability if friend not in attend]
print('not attend', not_attend)
