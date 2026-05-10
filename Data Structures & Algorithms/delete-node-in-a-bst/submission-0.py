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
                r = r.left
            return r
        # search for the right node
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # If node has one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                # if node has two or more children
                # find smallest node on right branch to keep a valid BST
                mnode = min_node(root.right)
                mnode_val = mnode.val

                root.val = mnode_val
                root.right = self.deleteNode(root.right, mnode_val)
        return root



