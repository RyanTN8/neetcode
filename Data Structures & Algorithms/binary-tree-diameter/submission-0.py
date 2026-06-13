# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> (int, int):
            #returns maxDepth, maxDiameter
            if not root.left and not root.right:
                return (1,1)

            if not root.right:
                l, m = helper(root.left)
                return (l + 1, max(l + 1, m))
            if not root.left:
                r, m = helper(root.right)
                return (r + 1, max(r + 1, m))
            else:
                l, m1 = helper(root.left)
                r, m2 = helper(root.right)
                diameter = l + r + 1
                return (max(l, r) + 1, max(diameter, m1, m2))
        return helper(root)[1] - 1
            
