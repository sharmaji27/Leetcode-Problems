'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.

'''

'''
 Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0) 
        l3 = head
        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0 
            d2 = l2.val if l2 else 0
            s = d1 + d2 + carry
            carry = s//10
            r = s%10
            l3.next = Listnode(r)
            l3 = l3.next
            if l1:l1=l1.next
            if l2:l2=l2.next
        
        return head.next    