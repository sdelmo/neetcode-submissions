# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def search(root, running):
            if not root:
                return False
            running += root.val
            if not root.left and not root.right and running == targetSum:
                return True
            return search(root.left, running) or search(root.right, running)

        return search(root, 0)
