# Name: Shuling Lin
# CSE 160
# Homework 4

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

###
#  Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

# Test shape of practice graph
assert set(practice_graph.neighbors("A")) == set(["B", "C"])
assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
assert set(practice_graph.neighbors("E")) == set(["D"])
assert set(practice_graph.neighbors("F")) == set(["C", "D"])


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_practice_graph(practice_graph)


###
#  Problem 1b
###

rj = nx.Graph()
# (Your code for Problem 1b goes here.)

rj.add_edge("Nurse", "Juliet")
rj.add_edge("Juliet", "Tybalt")
rj.add_edge("Juliet", "Friar Laurence")
rj.add_edge("Juliet", "Capulet")
rj.add_edge("Juliet", "Romeo")
rj.add_edge("Tybalt", "Capulet")
rj.add_edge("Capulet", "Escalus")
rj.add_edge("Capulet", "Paris")
rj.add_edge("Friar Laurence", "Romeo")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Romeo", "Mercutio")
rj.add_edge("Benvolio", "Montague")
rj.add_edge("Montague", "Escalus")
rj.add_edge("Escalus", "Mercutio")
rj.add_edge("Escalus", "Paris")
rj.add_edge("Mercutio", "Paris")

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

# Test shape of Romeo-and-Juliet graph
assert set(rj.neighbors("Nurse")) == set(["Juliet"])
assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet", "Mercutio"])
assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo", "Benvolio"])
assert set(rj.neighbors("Capulet")) == \
    set(["Juliet", "Tybalt", "Paris", "Escalus"])
assert set(rj.neighbors("Escalus")) == \
    set(["Paris", "Mercutio", "Montague", "Capulet"])
assert set(rj.neighbors("Juliet")) == \
    set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
assert set(rj.neighbors("Romeo")) == \
    set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
# draw_rj(rj)


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


assert friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given
    graph. The result does not include the given user nor any of that user's
    friends.
    """
    # store a bunch of friends to a set
    friends_set = friends(graph, user)
    # declare a friends_of_friends set
    friends_of_friends_set = set()
    # iterate over friends_set and get a set of friends_of_friends
    # using difference and union to exclude user and user's friends
    for every_friend in friends_set:
        friends_of_every_friend = set(graph.neighbors(every_friend))
        new2 = friends_of_every_friend - friends_set - {user}
        friends_of_friends_set |= new2

    return friends_of_friends_set


assert friends_of_friends(rj, "Mercutio") == \
    set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])
assert friends_of_friends(rj, "Nurse") == \
    set(['Capulet', 'Tybalt', 'Romeo', 'Friar Laurence'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common.
    """
    # use & to find the common elements of two sets and store it in
    # common_friends_set
    common_friends_set = set(graph.neighbors(user1)) & \
        set(graph.neighbors(user2))

    return common_friends_set


assert common_friends(practice_graph, "A", "B") == set(['C'])
assert common_friends(practice_graph, "A", "D") == set(['B', 'C'])
assert common_friends(practice_graph, "A", "E") == set([])
assert common_friends(practice_graph, "A", "F") == set(['C'])
assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }
    """
    # declare a dictionary
    dict = {}
    # store the return values of function friends_of_friends into a set
    friends_of_friends_set = friends_of_friends(graph, user)
    # map the number of common_friends as values and person that has common
    # friends as keys to a dictionary-dict
    for every_friend in friends_of_friends_set:
        number_of_friends = len(common_friends(graph, user, every_friend))
        dict[every_friend] = number_of_friends
    return dict


assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}
assert number_of_common_friends_map(rj, "Mercutio") == \
    {'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1,
     'Juliet': 1, 'Montague': 2}


def number_map_to_sorted_list(map_with_number_vals):
    """Given map_with_number_vals, a dictionary whose values are numbers,
    return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.
    """
    # turn keys and values of a dictionary into a list
    list_of_mapping_values = map_with_number_vals.items()
    # sort on most important element last: sort score from highest to lowest
    # and if there is a tie, sort by name alphebetically
    # (from least to greatest)
    sort_by_name = sorted(list_of_mapping_values, key=itemgetter(0))
    sort_by_score = sorted(sort_by_name, key=itemgetter(1), reverse=True)
    # declare a new list
    sorted_key = []
    # store the sorted keys into a new list
    for every_pair in sort_by_score:
        sorted_key.append(every_pair[0])
    return sorted_key


assert number_map_to_sorted_list({"a": 5, "b": 2, "c": 7, "d": 5, "e": 5}) == \
    ['c', 'a', 'd', 'e', 'b']
assert number_map_to_sorted_list({"a": 3, "b": 3, "c": 3, "d": 5, "e": 5}) == \
    ['d', 'e', 'a', 'b', 'c']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    # declare a dictionary
    new_dict = {}
    # store the mapping of number of common friends and people
    # that have friends in common into a dictionary
    new_dict = number_of_common_friends_map(graph, user)
    # given the dictionary and return a list of sorted keys
    return number_map_to_sorted_list(new_dict)


assert recommend_by_number_of_common_friends(practice_graph, "A") == ['D', 'F']
assert recommend_by_number_of_common_friends(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    # declare a dictionary
    influence_dict = {}
    # declare an int variable to store influence score
    influence_score = 0
    # store the return values of friends_of_friends function into a set
    friends_of_friends_set = friends_of_friends(graph, user)
    # iterate over friends_of_friends set
    for every_friend in friends_of_friends_set:
        # store the return values of common_friends into a set
        common_friends_set = common_friends(graph, user, every_friend)
        # iterate over every common friend and calculate its influence score
        # by calling the friends function and map the values to a dictionary
        for every_common_friend in common_friends_set:
            influence_score += (1 / len(friends(graph, every_common_friend)))
        influence_dict[every_friend] = influence_score
        influence_score = 0
    return influence_dict


assert influence_map(rj, "Mercutio") == \
    {'Benvolio': 0.2, 'Capulet': 0.5833333333333333,
     'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45}


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    # store a bunch of sorted friend recommendations to a list
    influence_list = number_map_to_sorted_list(influence_map(graph, user))
    return influence_list


assert recommend_by_influence(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
#  Problem 4
###

print("Problem 4:")
print()

# declare two lists for storing the results for print statements
same_result_list = []
different_result_list = []
# iterate over the graph
for every_node in rj.nodes():
    # If the results of two functions are the same, add the node
    # to same_result_list
    if recommend_by_number_of_common_friends(rj, every_node) == \
            recommend_by_influence(rj, every_node):
        same_result_list.append(every_node)
    # If not, add the node to different_result_list
    else:
        different_result_list.append(every_node)
print("Unchanged Recommendations:", same_result_list)
print("Changed Recommendations:", different_result_list)

###
#  Problem 5
###

# declare a facebook graph
facebook = nx.Graph()
# open the facebook-links.txt file
myfile = open("facebook-links.txt")
# declare a list
two_identifiers = []
# read lines in myfile one by one
for line_of_text in myfile:
    # split the line into several strings
    read_users = line_of_text.split()
    # iterate over the first two strings in a list
    for every_user in read_users[0:2]:
        # turn the variable type to int
        user_num = int(every_user)
        # store two integers into a list
        two_identifiers.append(user_num)
    # create nodes and edges of facebook graph
    facebook.add_node(two_identifiers[0])
    facebook.add_node(two_identifiers[1])
    facebook.add_edge(two_identifiers[0], two_identifiers[1])
    # clear the list so it can take in new values and
    # add nodes and edges when one iteration is done
    two_identifiers = []
# close the file when all lines are read
myfile.close()


assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090


###
#  Problem 6
###
print()
print("Problem 6:")
print()

# declare a set
user_set = set()
# iterate over the graph
for user in facebook.nodes():
    # take in every user whose ID is a multiple of 1000
    if (user % 1000 == 0):
        # add every user that matches the expression
        user_set.add(user)
# iterate over the sorted user_set
for user in sorted(user_set):
    # store a bunch of recommended friends into a list
    recommend_friends_list = \
        recommend_by_number_of_common_friends(facebook, user)
    # if the list has more than 10 friends, then print the first ten
    if len(recommend_friends_list) > 10:
        print(user, "(by number_of_common_friends):",
              recommend_friends_list[0:10])
    # If less than ten, print the entire list
    else:
        print(user, "(by number_of_common_friends):",
              recommend_friends_list)


###
#  Problem 7
###
print()
print("Problem 7:")
print()

# declare a new set
user_set = set()
# iterate over the facebook graph
for user in facebook.nodes():
    # take in every user whose ID is a multiple of 1000
    if (user % 1000 == 0):
        # add every qualified user to user_set
        user_set.add(user)
# iterate over the sorted user_set
for user in sorted(user_set):
    # store a bunch of recommended friends into a list
    recommend_friends_list = \
        recommend_by_influence(facebook, user)
    # if the list has more than 10 friends, then print the first ten
    if len(recommend_friends_list) > 10:
        print(user, "(by influence):",
              recommend_friends_list[0:10])
    # If less than ten, print the entire list
    else:
        print(user, "(by influence):",
              recommend_friends_list)

###
#  Problem 8
###
print()
print("Problem 8:")
print()

# declare two new lists
same_results_list = []
different_results_list = []
# iterate over facebook graph
for every_user in facebook.nodes():
    # take in every user whose ID is a multiple of 1000
    if (every_user % 1000 == 0):
        # if the results of two functions all equal, add the user to
        # same_results_list
        if recommend_by_number_of_common_friends(facebook, every_user) == \
           recommend_by_influence(facebook, every_user):
            same_results_list.append(every_user)
        # If not, add the user to different_results_list
        else:
            different_results_list.append(every_user)
print("Same:", len(same_results_list))
print("Different:", len(different_results_list))

###
#  Collaboration
###

# None
