'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

############################### ITERATIVE ######################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root]
        while q:
            values = [i.val if i else None for i in q]
            if values!=values[::-1]:return False
            q = [child for i in q if i for child in (i.left,i.right)]
        return True

############################### RECURSIVE ######################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def lr_check(L,R):
    if not L and not R : return True
    if not L or not R : return False
    
    if L.val!=R.val:return False

    a = lr_check(L.left,R.right)
    b = lr_check(L.right,R.left)
    return a and b

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root : return True
        return lr_check(root.left,root.right)