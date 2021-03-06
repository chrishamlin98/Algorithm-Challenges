# I think we need to separate the left and right peakcheckers in order to keep them increasing or decreasing
# After 2nd day of reviewing, it seems we will be traversing the array and finding peaks then
# moving left and right to find the length and store that value.  Then, find another and compare
def longestPeak(array):
    longestPeak = 0
    i = 1
    while i < len(array) - 1:
        peak = array[i - 1] < array[i] > array[i + 1]
        if not peak:
            i += 1
            continue

        leftIdx = i - 2
        rightIdx = i + 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longestPeak = max(longestPeak, currentPeakLength)
        i = rightIdx

    return longestPeak


pass
