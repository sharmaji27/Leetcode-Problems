
'''
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        if head.next == None:
            return head
        f = head
        s = head.next
        head = head.next
        p = f
        temp = s.next
        s.next = f
        f.next = temp
        f = f.next
        try:
            s = s.next.next.next
        except:
            return head
        
        while(f and s):
            temp = s.next
            s.next = f
            f.next = temp
            p.next = s
            f = f.next
            try:
                s = s.next.next.next
            except:
                break
            p = p.next.next
        return head