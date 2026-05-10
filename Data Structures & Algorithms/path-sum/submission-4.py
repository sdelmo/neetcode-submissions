# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(r, running):
            if not r:
                return False
            
            running += r.val

            if not r.left and not r.right:
                return running == targetSum
            
            return dfs(r.left, running) or dfs(r.right, running)
        
        return dfs(root, 0)