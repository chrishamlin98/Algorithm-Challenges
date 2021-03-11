# This is incomplete = does not work yet

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    combinedLL = LinkedList(0)
    linkedListPointerOne = linkedListOne()
    linkedListPointerTwo = linkedListTwo()
    carry = 0
    currentValue = 0

    while linkedListPointerOne is not None or linkedListPointerTwo is not None:
        currentValue = linkedListPointerOne + linkedListPointerTwo
        combinedLL.value = currentValue % 10
        carry = currentValue // 10
        combinedLL.next = carry + combinedLL.next.value

    while linkedListPointerOne is None:
        currentValue = linkedListPointerTwo.next + carry
        linkedListPointerTwo = currentValue

    while linkedListPointerTwo is None:
        currentValue = linkedListPointerOne.next + carry
        linkedListPointerOne = currentValue

    return combinedLL.next
