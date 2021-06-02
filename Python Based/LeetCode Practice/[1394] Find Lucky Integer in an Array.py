class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        maxVal = -1

        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in arr:
            if freq[i] == i:
                maxVal = max(maxVal, freq[i])

        return maxVal

# create a dictionary that stores the key, value pair where the key is a new number and the value how many of the
# number there is.  Each time a key is identified, increase the value

#      count = 0
#    === THIS DOES NOT WORK BECAUSE YOU NEED MULTIPLE COUNTS ===
#        for pointerOne in range(0, len(arr) - 1):
#            positionOne = pointerOne[0]
#            for pointerTwo in range(1, len(arr)):
#               positionTwo = pointerTwo[1]

#                if positionOne == positionTwo:
#                    count += 1
#  for key, value in range(len(arr)):
