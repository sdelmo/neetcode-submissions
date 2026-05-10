# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        def min_node(r):
            while r.left:
                r=r.left
            return r
        
        # If node is greater than key, search left branch
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # If node is less than key, search right branch
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # Found the place to delete
        else:
            # One child at node
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Two or more children
            else:
                # Find smallest node on right branch to keep tree balanced
                mn = min_node(root.right)
                mval = mn.val
                # Reset value at node with smallest right branch node
                root.val = mval
                # Remove the node we used to fill the root with
                root.right = self.deleteNode(root.right, mval)
        return root



