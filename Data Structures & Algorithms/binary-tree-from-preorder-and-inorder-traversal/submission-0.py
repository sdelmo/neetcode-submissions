# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder and not inorder:
            return None
        
        # Root is the first element in preorder
        # as it traverses root left right
        root = TreeNode(preorder[0])
        # We find the index of the root in inorder to see how many elements in right/left trees
        idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return root
        
