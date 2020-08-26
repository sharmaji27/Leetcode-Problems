'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        q = []
        q.append(root)
        level = 1
        ans = []
        
        while len(q)!=0:
            tempq = []
            data = []
            while len(q)!=0:
                data.append(q[0].val)
                if q[0].left!=None:tempq.append(q[0].left)
                if q[0].right!=None:tempq.append(q[0].right)
                q.pop(0)
            if level%2==0:
                ans.append(data[::-1])
            else:
                ans.append(data)
            q = tempq
            level+=1
        return ans