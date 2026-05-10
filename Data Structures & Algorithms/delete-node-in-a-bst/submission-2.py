# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def smallest_node(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Edge case
        if not root:
            return
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # found node in question
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                # find smallest node on right branch to keep tree balanced
                minnode = self.smallest_node(root.right)
                mval = minnode.val

                # replace node to delete with mval
                root.val = mval
                # delete duplicate node on right branch
                root.right = self.deleteNode(root.right, mval)
        return root
    
        
