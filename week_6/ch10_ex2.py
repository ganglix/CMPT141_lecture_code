# Daily variance of flu tests can be high. We often calculate the
# 7-day average instead: for each day, take the AVERAGE of
# the preceding 7 days (including itself)
# Using the flu_data list, create a new list where the values
# are the 7-day average for each day. Start from day 7
# Then, plot the data in the new list
# Hint: Slicing might be useful

flu_case = [13, 14, 9, 16, 10, 18, 22, 19, 16, 22,
             24, 48, 34, 25, 17, 29, 33, 35, 28, 43,
             59, 44, 55, 63, 61, 48, 68, 61, 70, 76,
             78, 74, 87, 101, 120, 128, 105, 109, 120, 124,
             111, 128, 120, 133, 134, 139, 127, 130, 141, 147,
             439, 236, 218, 209, 213, 244, 329, 197, 351, 325]

"""
index   0   1   2   3   4   5   6   7   ... len(flu_case)-1
day     1   2   3   4   5   6   7   8   ... len(flu_case)
"""

days = range(1, len(flu_case)+1)
days_7d = range(7, len(flu_case)+1)
window_size = 7
# # first 7 days average
# case_7d_avg = sum(flu_case[0:7]) / window_size
#
# # move window by 1 place
# case_7d_avg = sum(flu_case[0+1:7+1]) / window_size

# move window by "nubmer of day" place
flu_case_7d = []
for day in days_7d:
    case_7d_avg = sum(flu_case[day-7 : day]) / window_size
    flu_case_7d.append(case_7d_avg)

import matplotlib.pyplot as plt

plt.plot(days, flu_case, color='C0', marker="o", label = "daily")
plt.plot(days_7d, flu_case_7d, color='C1', linestyle="-", linewidth = 3, label = "7-day average")
plt.xlabel("day")
plt.ylabel("cases")
plt.legend()
plt.show()



