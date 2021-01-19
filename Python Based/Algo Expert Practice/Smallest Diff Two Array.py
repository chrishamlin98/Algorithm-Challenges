# My solution did not work, the recommended solution
# is using while loops.  I'm not sure why

# def smallestDifference(arrayOne, arrayTwo):
# 	arrayOne.sort()
# 	arrayTwo.sort()
# 	idxOne = 0
# 	idxTwo = 0
# 	smallest = float("inf")
# 	currentDif = float("inf")
# 	smallestPair = []
# 	for idxOne in len(arrayOne):
# 		for idxTwo in len(arrayTwo):
# 			if arrayOne[idxOne] < arrayTwo[idxTwo]:
# 				currenDif = arrayTwo[idxTwo] - arrayOne[idxOne]
# 				idxOne += 1
# 			elif arrayOne[idxOne] > arrayTwo[idxTwo]:
# 				currentDif = arrayOne[idxOne] - arrayTwo[idxTwo]
# 				idxTwo += 1
# 			else:
# 				return[arrayOne[idxOne], arrayTwo[idxTwo]]
# 			if smallest > currentdif:
# 				smallest = currentdif
# 				smallestPair = [arrayOne[idxOne], arrayTwo[idxTwo]]
# 			return smallestPair
# 	pass

# ALgoExpert solution that works

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while i < len(arrayOne) and j < len(arrayTwo):
        firstNum = arrayOne[i]
        secondNum = arrayTwo[j]
        if firstNum < secondNum:
            current = secondNum - firstNum
            i += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            j += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


pass
