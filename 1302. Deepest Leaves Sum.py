'''
Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

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
def height(root):
    if root == None:return 0
    return 1+max(height(root.left),height(root.right))
    
    
def dfs(root,curr_height,wanted_height):
    global ans
    if root==None:return
    if (1+curr_height)==wanted_height:
        ans+=root.val

    dfs(root.left,curr_height+1,wanted_height)
    dfs(root.right,curr_height+1,wanted_height)

ans = 0

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        global ans
        ans=0
        h = height(root)
        dfs(root,0,h)
        return ans