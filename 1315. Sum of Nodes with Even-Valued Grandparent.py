'''
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ans = 0

def get_sum(root,parent,grandparent):
    global ans
    if root==None:
        return 
    if grandparent and (grandparent.val%2)==0:
        ans+=root.val
        
    get_sum(root.left,root,parent)
    get_sum(root.right,root,parent)
    
    
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        global ans
        ans = 0
        get_sum(root,None,None)
        return ans