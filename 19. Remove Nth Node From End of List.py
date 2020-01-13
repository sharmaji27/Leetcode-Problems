# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp1 = head
        temp2 = head
        for _ in range(n):
            if temp2:temp2 = temp2.next
            else : return None
        if temp2 is None:
            return head.next
        while temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next
        temp1.next = temp1.next.next
        return head