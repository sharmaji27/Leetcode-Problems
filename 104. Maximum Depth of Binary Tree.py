'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
mx = 0
def find_max(root,level):
    global mx
    if root==None:return
    mx = max(mx,level)
    find_max(root.left,level+1)
    find_max(root.right,level+1)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        global mx
        mx = 0
        find_max(root,1)
        return mx