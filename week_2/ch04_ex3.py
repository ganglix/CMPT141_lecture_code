# Generalization of functions (or algorithms)
# is the process of modifying a function/algorithm that
# solves a specific problem so that it can solve a wider range of problems, or a larger number of
# instances of the same problem

# How can we generalize each function for reusability?
# (a) This function computes the most number of cards in a 52 card deck that can be dealt equally amongst
# four people

def cards_per_player(number_of_cards, number_of_players):
    return number_of_cards // number_of_players


# (b) This function computes the number of hours required to watch a 26 episode television show consisting
# of 22 minute episodes

def total_watch_time(n_episode, minute_per_episode):
    """

    :param n_episode:
    :param minute_per_episode:
    :return: total hours
    """
    minutes_per_hour = 60
    return n_episode * minute_per_episode / minutes_per_hour