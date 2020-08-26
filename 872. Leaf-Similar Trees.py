'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Constraints:

Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def make_list(self,root,l):
        if root == None:
            return 
        self.make_list(root.left,l)
        if root.left==None and root.right==None:
            l.append(root.val)
        self.make_list(root.right,l)
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        l1 = []
        l2 = []
        self.make_list(root1,l1)
        self.make_list(root2,l2)

        return l1==l2