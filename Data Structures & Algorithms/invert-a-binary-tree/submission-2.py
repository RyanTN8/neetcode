# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node: Optional[TreeNode]) -> None:
            if node:
                if node.left and not node.right:
                    node.right = node.left
                    node.left = None
                    helper(node.right)
                elif node.right and not node.left:
                    node.left = node.right
                    node.right = None
                    helper(node.left)
                else:
                    node.left, node.right = node.right, node.left
                    helper(node.left)
                    helper(node.right)
        helper(root)
        return root


                