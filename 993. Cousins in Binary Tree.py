'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(root,parent,level,x,y):
    global p1,p2,l1,l2
    
    if root==None:return
    if root.val == x:
        l1 = level
        p1 = parent.val if parent else None
    if root.val == y:
        l2 = level
        p2 = parent.val if parent else None
        
    traverse(root.left,root,level+1,x,y)
    traverse(root.right,root,level+1,x,y)
    

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        global p1,p2,l1,l2
        l1 = 0
        l2 = 0
        p1 = None
        p2 = None
        traverse(root,None,1,x,y)
        return p1!=p2 and l1==l2