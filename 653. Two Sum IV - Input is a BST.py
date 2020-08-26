'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root,l):
    if root==None:return
    inorder(root.left,l)
    l.append(root.val)
    inorder(root.right,l)

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        l = []
        inorder(root,l)
        i=0
        j=len(l)-1
        while i<j:
            if l[i]+l[j]==k:return True
            elif l[i]+l[j]<k:i+=1
            else:j-=1
        return False