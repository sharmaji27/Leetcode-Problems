'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None:return []
        stack = [[root,'']]
        res = []
        while stack:
            curr,path = stack.pop()
            if curr.left:stack.append([curr.left,path+str(curr.val)+'->'])
            if curr.right:stack.append([curr.right,path+str(curr.val)+'->'])
            if not curr.left and not curr.right:
                res.append(path+str(curr.val))
        
        return(res)