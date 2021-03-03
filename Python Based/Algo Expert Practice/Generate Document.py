## Given a string of characters and a document with a string of characters
## Can the document be made with the string of characters?
## If string is "aabbcc" and doc is "aabbccc" then doc cannot be made
## because we are missing 1 "c".

def generateDocument(characters, document):
    charCounts = {}

    for char in characters:
        if char not in charCounts:
            charCounts[char] = 0

        charCounts[char] += 1

    for char in document:
        if char not in charCounts or charCounts[char] == 0:
            return False

        charCounts[char] -= 1

    return True
