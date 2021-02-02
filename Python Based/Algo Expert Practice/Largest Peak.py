# I think we need to separate the left and right peakcheckers in order to keep them increasing or decreasing

def longestPeak(array):
    peakChecker = 1
    currentPeak = 0
    largestPeak = 0

    for peakChecker in array:
        while array[peakChecker] - 1 < array[peakChecker]:
            peakChecker += 1
            currentPeak += 1
        while array[peakChecker] < array[peakChecker] + 1:
            peakChecker += 1
            currentPeak += 1


pass
