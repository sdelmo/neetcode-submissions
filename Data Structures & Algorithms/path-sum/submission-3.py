# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(r, currsum):
            if not r:
                return False

            # add curr value of node
            currsum += r.val

            # check that we have reached a leaf and target
            if not r.left and not r.right and currsum == targetSum:
                return True
            
            return dfs(r.left, currsum) or dfs(r.right, currsum)

        return dfs(root,0)

