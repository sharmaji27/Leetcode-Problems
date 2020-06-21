'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 
Example 1:


Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 

Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
'''
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = [root]
        mx = root.val
        ml = 1
        level = 1
        while q:
            q_temp = []
            c_s = 0
            while q:
                if q[0].left:q_temp.append(q[0].left)
                if q[0].right:q_temp.append(q[0].right)
                x = q.pop(0)
                c_s+=x.val
            if c_s>mx:
                mx = c_s
                ml = level
            q = q_temp
            level+=1
        return ml