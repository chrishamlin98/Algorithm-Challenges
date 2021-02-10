# Given a list of values whose values < len(array
# return the closest index of the 2nd value of the pair of matched integers

# This is a functional brute force method  O(N)2 time

def firstDuplicateValue(array):
    minimumSecondIndex = len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                minimumSecondIndex = min(minimumSecondIndex, j)

    if minimumSecondIndex == len(array):
        return -1
    return array[minimumSecondIndex]
