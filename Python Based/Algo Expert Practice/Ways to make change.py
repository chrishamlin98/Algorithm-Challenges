def numberOfWaysToMakeChange(n, denominations):
    output = [0 for amount in range(n + 1)]
    output[0] = 1

    for number in denominations:
        for amount in range(1, n + 1):
            if number <= amount:
                output[amount] += output[amount - number]

    return output[-1]
