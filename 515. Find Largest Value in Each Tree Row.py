'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9] 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root==None:
            return
        q=[]
        ans = []
        q.append(root)
        
        while len(q)!=0:
            row = []
            temp = []
            while len(q)!=0:
                row.append(q[0].val)
                if q[0].left:temp.append(q[0].left)
                if q[0].right:temp.append(q[0].right)
                q.pop(0)
            q = temp
            ans.append(max(row))
        
        return ans