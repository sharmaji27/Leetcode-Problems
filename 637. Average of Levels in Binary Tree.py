'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root==None:return[]
        q = [root]
        res = []
        while q:
            q_temp = []
            s = 0
            count = 0
            while q:
                x = q.pop(0)
                s+=x.val
                count+=1
                if x.left:q_temp.append(x.left)
                if x.right:q_temp.append(x.right)
            q = q_temp
            res.append(s/count)
        return res