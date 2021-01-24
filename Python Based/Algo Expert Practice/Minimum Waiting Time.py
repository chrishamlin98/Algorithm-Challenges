# A query's waiting time is defined as the amount of time it must
# wait before its execution starts.  If a query is executed third, then
# its waiting time is the sum of the durations of the first two queries.
# [1, 2, 2, 3, 6]  - First thing to do is sort the array
# The sum order would them be 0 + (1) + (1+2) + (1+2+2) + (1+2+2+3)

# We can use enumerate and multiplication to calculate the values that
# will end up being repeated (all at once)

# Time O(n log n) (Through the use of sorting)  Space = O(1) (All in place)

def minimumWaitingTime(queries):
    queries.sort()

    totalWaitingTime = 0

    for idx, value in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += value * queriesLeft

    return totalWaitingTime
