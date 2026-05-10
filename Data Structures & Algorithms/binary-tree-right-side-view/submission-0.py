# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        
        frontier = deque([root])
        rhs = []
        while frontier:
            level = []
            for _ in range(len(frontier)):
                node = frontier.popleft()
                level.append(node.val)
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)
            rhs.append(level[-1])
        return rhs
