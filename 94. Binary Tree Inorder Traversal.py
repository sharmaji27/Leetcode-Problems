'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        inorder(root,l)
        return l