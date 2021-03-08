# given an array, return the squared values

def sortedSquaredArray(array):
    for i, x in enumerate(array):
        array[i] = x*x
    return sorted(array)
