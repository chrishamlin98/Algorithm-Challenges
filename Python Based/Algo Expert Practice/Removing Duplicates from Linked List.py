# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # set the current node = to the linked list because we are starting at the beginning and
    # iterating through every node use the temp and next functions

    currentNode = linkedList

    while currentNode is not None:
        temp = currentNode.next
        while temp is not None and temp.value == currentNode.value:
            temp = temp.next

        currentNode.next = temp
        currentNode = temp

    return linkedList
