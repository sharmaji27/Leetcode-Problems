'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    global isBal
    if not root: return 0
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh-rh)>1:isBal= False
    return 1+max(lh,rh)
    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        global isBal
        isBal = True
        height(root)
        return isBal