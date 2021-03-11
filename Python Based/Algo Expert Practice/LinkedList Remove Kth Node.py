# Singly linked list remove kth node from end

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    counter = 1
    tempOne = head
    tempTwo = head

    while counter <= k:
        tempTwo = tempTwo.next
        counter += 1

    if tempTwo is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while tempTwo.next is not None:
        tempOne = tempOne.next
        tempTwo = tempTwo.next

    tempOne.next = tempOne.next.next


pass
