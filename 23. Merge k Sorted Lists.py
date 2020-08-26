'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

from heapq import heappush,heapify,heappop
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        h=[]
        heapify(h)
        for node in A:
            while node:
                heappush(h,node.val)
                node = node.next
        
        res = head = ListNode(0)
        
        while h:
            res.next=ListNode(heappop(h))
            res=res.next
        res.next=None
        return head.next