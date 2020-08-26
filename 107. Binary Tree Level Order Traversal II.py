'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:return[]
        q = [root]
        res = []
        while q:
            q_temp = []
            re = []
            while q:
                x = q.pop(0)
                re.append(x.val)
                if x.left:q_temp.append(x.left)
                if x.right:q_temp.append(x.right)
            q = q_temp
            res.insert(0,re)
        return res