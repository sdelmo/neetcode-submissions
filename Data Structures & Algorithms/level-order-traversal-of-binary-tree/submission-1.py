# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque

        queue = deque()
        subtrees = []

        # Ensure that we do have a root

        if root:
            queue.append(root)

        while queue:
            subtrees.append([x.val for x in queue])

            for i in range(len(queue)):

                # Process parent node
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)

        return subtrees



