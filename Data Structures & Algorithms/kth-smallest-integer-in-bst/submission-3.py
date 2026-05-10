# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        ino = []
        curr_node = root
        steps = 0

        while curr_node or stack:
            # explore entire right branch
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            # pop last e added to stack
            curr_node = stack.pop()
            ino.append(curr_node.val)
            steps += 1
            if steps == k:
                return ino[-1]
            # process right branch
            curr_node = curr_node.right
    