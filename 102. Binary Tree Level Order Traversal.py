'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:return []
        q = [root]
        res = []
        while q:
            qtemp = []
            r = []
            while q:
                x = q.pop(0)
                r.append(x.val)
                if x.left:qtemp.append(x.left)
                if x.right:qtemp.append(x.right)
            res.append(r)
            q = qtemp
        return res