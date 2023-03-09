# CMPT 141 - Arrays
# Topic(s): 1D Arrays


import numpy as np

# distances from current location to all coffee shop chain locations in city
coffee_shops = [5.5, 2.6, 12.5, 22.2, 0.45, 1.32, 3.3, 8.3, 6.2, 9.1]


# Part (a) Create a 1D array of the data items from coffee_shops in
# ascending order
distances = np.array(sorted(coffee_shops))
# distances = np.array(coffee_shops)
# distances.sort()


# Part (b) Print the number of coffee shops
print("Number of coffee shops in the city:", distances.size)

# Part (c) Print the distance to the farthest shop
print("The furthest coffee shop is",distances.max(),"km away.")

# Part (d) Print the distances to the five closest shops
print(distances[0:5])

