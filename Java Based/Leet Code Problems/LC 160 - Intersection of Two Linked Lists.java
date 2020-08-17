/**
Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }



 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {


ListNode p1 = headA, p2 = headB;
    int len1 = 0, len2 = 0;
    while (p1 != null) {
        p1 = p1.next;
        len1++;
    }
    while (p2 != null) {
        p2 = p2.next;
        len2++;
    }
    p1 = headA;
    p2 = headB;
    if (len1 > len2) {
        for (int i = 0;i < len1 - len2; i++) {
            p1 = p1.next;
        }
    } else {
        for (int i = 0;i < len2 - len1; i++) {
            p2 = p2.next;
        }
    }
    while (p1 != p2) {
        p1 = p1.next;
        p2 = p2.next;
    }
    return p1;
}
