'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return 
        elif head.next==None:
            return head
        else:
            moving = head
            stable = head
            while moving.next!=None:
                if moving.next.val!=moving.val:
                    stable.next = moving.next
                    stable = moving.next
                moving = moving.next

            stable.next=None        
            return head