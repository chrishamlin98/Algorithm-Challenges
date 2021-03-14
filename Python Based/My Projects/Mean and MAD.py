# This file will find the mean of a list of values as well as the mean absolute deviation

arrayOfValues = input()
input = list(map(int, arrayOfValues.split(' ')))

mean = sum(input) / len(input)

absoluteDeviation = []
for eachValue in input:
    absoluteDeviation.append(abs(eachValue - mean))
    eachValue += 1

mad = sum(absoluteDeviation) / len(absoluteDeviation)

print(mad)
print(mean)
