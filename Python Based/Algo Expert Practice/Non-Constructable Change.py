# Given an array of change values, write a function that returns
# the smallest amount that you cannot make

#  Brute force solution is too complicated because it would require
# multiple loops and complicated math

# Instead, we should sort the list and then use math understanding
# to come up with the solution

def nonConstructableChange(coins):
    coins.sort()
    change = 0

    for i in coins:
        if i > change + 1:
            return change + 1
        change += i

    return change + 1
