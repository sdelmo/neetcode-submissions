# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
         
        # edge case: no valid tree to begin with
        if not root:
            return False

        """
        Approach:
        We need to DFS all the way to the leaf such that the sum of all nodes in path
        equals targetSum. Any solution is fine

        Ideally, we'd like to avoid branches where currsum exceeds targetsum
        """

        def dfs(node: TreeNode, running: int) -> bool:
            if not node:
                return False
            
            running += node.val
            
            if not node.left and not node.right and running == targetSum:
                return True
            # Check left and right branches, return whichever evals to true    
            return dfs(node.left, running) or dfs(node.right, running)
        
        return dfs(root, 0)
        

        
            

            

