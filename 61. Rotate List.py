'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head == None:
            return None
        if head.next == None:
            return head
        
        size = 0
        temp = head
        while temp:
            size+=1
            temp = temp.next
        
        k = k%size
        if k==0:
            return head
        
        fast = head
        slow = head
        
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        
        slow.next = None
        fast.next = head
        head = temp
        
        return head