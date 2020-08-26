'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root==None:return 0
        stack = [[root,'']]
        s = 0
        
        while stack:
            curr,from_where = stack.pop()
            if not curr.left and not curr.right and from_where=='l':s+=int(curr.val)
            if curr.left: stack.append([curr.left,'l'])
            if curr.right: stack.append([curr.right,'r'])        
        
        return s