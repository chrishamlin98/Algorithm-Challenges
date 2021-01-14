# Write a function that takes in a non-empty string and returns its run-length encoding.
# Basically, take a run of data and compress it "AAAAAAA" = "7A"
# Any string length longer than 9 must be split - ie
# "AAAAAAAAAAAAA" = "9A4A"

# Coded in notebook - complete another day

def runLengthEncoding(string):
    characters = []
    length = 1

    for i in range(1, len(string)):
        current = string[i]
        prev = string[i-1]

        if current != prev or length == 9:
            characters.append(str(length))
            characters.append(prev)
            length = 0

        length += 1

    characters.append(str(length))
    characters.append(string[len(string) - 1])

    return "".join(characters)
    pass
