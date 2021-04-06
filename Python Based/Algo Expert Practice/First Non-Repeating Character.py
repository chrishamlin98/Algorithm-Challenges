# Idea 1 -  Brute force - use 2 pointers and traverse the string until match is found
# Once found, move both pointers forward one until a match is not found
# Return the index of the first pointer

# Idea 2 - Sort the string, for character, if char == char, continue
# else if character != character, return string[characters]

# Idea 3 - store key as characters and values as counts and return first with count == 1

# O(n) time because we do two linear traversals
# O(1) because there are only lowercase English letters, and the
# dictionary will have at most 26 entries. It doesn't grow as string grows
def firstNonRepeatingCharacter(string):
    characterFrequencies = {}

    for character in string:
        # key is going to be equal to the value where the value is going to be get (character, 0) + 1
        # This will check the dictionary and add to character with a value of 0 if not present
        # else it will add 1 to the character value
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1

    # We are doing an index traversal because we are returning the index
    for index in range(len(string)):
        character = string[index]
        if characterFrequencies[character] == 1:
            return index

    return -1
