'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traversal(root):
    global l,prev,max_count,current_count,result
    if root==None:return 
    traversal(root.left)
    
    current_count=1 if root.val!=prev else current_count + 1
    if current_count == max_count:
        result.append(root.val)
    elif current_count>max_count:
        result = [root.val]
        max_count = current_count
    prev = root.val
    
    traversal(root.right)
    
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        global l,prev,max_count,current_count,result
        l = []
        prev = None
        max_count = 0
        current_count = 0 
        result = []
        traversal(root)
        return result