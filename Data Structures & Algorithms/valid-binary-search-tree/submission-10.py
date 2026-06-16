# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode, minimum: int, maximum: int) -> bool:
            if not root.left and not root.right:
                return minimum < root.val < maximum
            if not root.right:
                return minimum < root.val < maximum and dfs(root.left, minimum, min(maximum, root.val))
            if not root.left:
                return minimum < root.val < maximum and dfs(root.right, max(minimum, root.val), maximum)
            return minimum < root.val < maximum and dfs(root.left, minimum, min(maximum, root.val)) and dfs(root.right, max(minimum, root.val), maximum)
        if not root:
            return True
        return dfs(root, -1001, 1001)