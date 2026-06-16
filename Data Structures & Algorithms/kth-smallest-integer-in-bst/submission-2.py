# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #do in-order traversal on tree until get kth value
        #decrement k each time
        count = k
        result = root.val

        def inOrder(node: TreeNode) -> None:
            nonlocal count, result
            if not node:
                return
            
            inOrder(node.left)
            count -= 1
            if count == 0:
                result = node.val
                return
            inOrder(node.right)
        inOrder(root)
        return result