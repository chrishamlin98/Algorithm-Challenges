# Easy to run solution - not optimal

def isPalindrome(string):
    reverse = string[::-1]
    if reverse == string:
        return True
    else:
        return False

# optimal solution

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1

    while leftIdx < leftIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx +=1
        rightIdx -=1
    return True
pass