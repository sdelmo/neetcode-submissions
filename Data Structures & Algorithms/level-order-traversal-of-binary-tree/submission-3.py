# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []
        if not root:
            return levels
        from collections import deque
        frontier = deque([root])

        while frontier:
            level = []
            # process elements in queue
            for _ in range(len(frontier)):
                n = frontier.popleft()
                # add current node to level
                level.append(n.val)
                # enqueue left
                if n.left:
                    frontier.append(n.left)
                # same for right
                if n.right:
                    frontier.append(n.right)
            
            levels.append(level)
        
        return levels
