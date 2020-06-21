'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
'''
def insert(l,r,n,x):
    z=n.next
    l.next=n
    n.next=r
    x.next=z


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None:return
        left = head
        right = head.next
        jumps=1
        while 1:
            x = right
            y = jumps-1
            while y:
                x = x.next
                y-=1
            if x==None or x.next==None:break
            insert(left,right,x.next,x)
            if right.next==None or right.next.next==None:break
            jumps+=1
            left = left.next
        return head