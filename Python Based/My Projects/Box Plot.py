import matplotlib.pyplot as plt

arrayOfValues = input("What are your numbers? ")


def main():
    data = list(map(int, arrayOfValues.split(' ')))

    data.sort()

    fig1, ax1 = plt.subplots()

    ax1.boxplot(data)

    plt.show()


main()
