'''
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
 

Constraints:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
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
        l.append(root.val)
        self.make_list(root.right,l)
        
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = []
        self.make_list(root,l)
        ans = TreeNode(0)
        curr = ans
        
        for i in l:
            curr.left = None
            curr.right = TreeNode(i)
            curr = curr.right
        
        return ans.right