# Monotonic array either increases or decreases through the array
# if empty array return True if array has len(1) return True, else return if it is monotonic

def isMonotonic(array):
    Increases = True
    Decreases = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            Decreases = False
        if array[i] > array[i - 1]:
            Increases = False

    return Increases or Decreases


pass
