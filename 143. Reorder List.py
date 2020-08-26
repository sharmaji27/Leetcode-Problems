'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return []
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_list = slow.next
        slow.next = None

        prev = None
        curr = second_list

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second_list = prev
        first_list = head

        while second_list:
            temp1 = first_list.next
            temp2 = second_list.next
            second_list.next = None
            first_list.next = second_list
            second_list.next = temp1
            first_list = first_list.next.next
            second_list = temp2

        return head
 