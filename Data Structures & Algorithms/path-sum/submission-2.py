# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def dfs(r, csum):
            if not r:
                return False
            
            csum += r.val

            # See if possible from left
            if not r.left and not r.right and csum == targetSum:
                return True
            if dfs(r.left,csum):
                return True
            if dfs(r.right, csum):
                return True
            # Backtrack value
            csum -= r.val
            return False

        return dfs(root, 0)