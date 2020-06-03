# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.seen = set()

        def dfs(node,v):
            if node:
                node.val = v 
                self.seen.add(v)
                dfs(node.left,2*v+1)
                dfs(node.right,2*v+2)        
        dfs(root,0)
    
    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)