# Merge two sorted linked lists and return it as a new sorted list. The new list
#  should be made by splicing together the nodes of the first two lists.
#
#
#  Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
#  Example 2:
#
#
# Input: l1 = [], l2 = []
# Output: []
#
#
#  Example 3:
#
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
#
#  Constraints:
#
#
#  The number of nodes in both lists is in the range [0, 50].
#  -100 <= Node.val <= 100
#  Both l1 and l2 are sorted in non-decreasing order.
#
#  Related Topics Linked List
#  👍 5531 👎 685


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = sort_list = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                sort_list.next = l1
                l1 = l1.next
                sort_list = sort_list.next

            elif l1.val >= l2.val:
                sort_list.next = l2
                l2 = l2.next
                sort_list = sort_list.next

        sort_list.next = l1 or l2
        return head.next

# leetcode submit region end(Prohibit modification and deletion)
