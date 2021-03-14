# This file will take an input of values and find the median of the values without being in order
# This code runs and correctly calculates the Q1, Q3, and IQR
from scipy.stats import iqr
from numpy import quantile

arrayOfValues = input("What are your numbers? ")


def main():
    input = list(map(int, arrayOfValues.split(' ')))

    input.sort()
    dataset_IQR = iqr(input, interpolation='nearest')
    q1 = quantile(input, 0.25, interpolation='nearest')
    q3 = quantile(input, 0.75, interpolation='nearest')

    print("The first quartile is: " + str(q1))
    print("The third quartile is: " + str(q3))
    print("The IQR is : " + str(dataset_IQR))


main()

"""

    if len(input) % 2 == 0:
        medianValue = (input[len(input) // 2] + input[len(input) // 2 - 1]) / 2
        q1 = input[len(input) // 4]
        q3 = input[len(input) // 4]
    else:
        medianValue = input[len(input) // 2]
        q1 = (input[len(input) // 4] + input[len(input) // 4 - 1]) / 2

    iqr = q3 - q1

    print("Median is: " + str(medianValue))
    print(q1)
    print(q3)
    print("Interquartile Range is: " + str(iqr))


main()
# print(q1)


# These are the algorithms I have been working with

arrayOfValues = input()
input = list(map(int,arrayOfValues.split(' ')))

input.sort()

while len(input) %2 == 0:
  medianValue = (input[len(input)//2] + input[len(input)//2 - 1])/2
  break

while len(input) %2 != 0:
  medianValue = input[len(input)//2]
  q1 = medianValue(medianValue)
  # iqr = ((input[len(input)//2] + input[len(input)//2 - 1])/2) - ((input[len(input)//3] + input[len(input)//3 - 1])/2)
  break

print(medianValue)
print(q1)

"""
