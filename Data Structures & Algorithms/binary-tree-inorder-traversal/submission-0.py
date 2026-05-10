# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ino = []

        def dfs(r):
            if not r:
                return

            dfs(r.left)
            ino.append(r.val)
            dfs(r.right)
        
        dfs(root)
        return ino
        
        