# Use 2 pointers.  1 at the start 1 at the end.  Move 1st pointer forward to find target
# number and then swap with last pointer.  Then move last pointer left until they pass.

# Given an array and an integer, find all instances of integer and move to end

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
            j -= 1
        else:
            i += 1
    return array


pass
