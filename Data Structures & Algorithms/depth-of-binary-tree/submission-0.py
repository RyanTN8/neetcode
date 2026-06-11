# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode]) -> int:
            if not node.left and not node.right:
                return 1
            elif not node.right:
                return 1 + helper(node.left)
            elif not node.left:
                return 1 + helper(node.right)
            return 1 + max(helper(node.left), helper(node.right))
        if not root:
            return 0
        return helper(root)
