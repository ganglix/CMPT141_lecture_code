# List music contains sublists of songs. Song sublists have the
# format [title, rating, genre]:
# e.g. [ ["One",4,"Metal"], ["Happy",3,"Pop"], ... ]
# Use list comprehensions to create list best_playlist for
# songs where:
# • rating is either 4 or 5; AND...
# • genre is either "Metal" or "Hard Rock"


# Topic : List Comprehensions ( Selection )
# list of sublists of a user ’s songs containing [title , rating , genre ]
library = [["Pokemon!", 5, "Metal"],
           ["The Pokerap", 4, "Rap"],
           ["On the Road to Viridian City", 4, "Hard Rock"],
           ["Ghost Love Score", 1, "Metal"],
           ["So Cold", 1, "Hard Rock"]]

# -----------------------------------------
# the brackets work across multiple lines, so the one-liner list comprehension can be written in many lines
best_playlist = [song for song in library     # song is the sublist in library
                 if (song[1] == 4 or song[1] ==5) and (song[2] == "Metal" or "Hard Rock")] # paranthesis needed here

# remember NAO? order of precedence not > and > or. If unsure, use paranthesis to ensure order of execution


print(best_playlist)