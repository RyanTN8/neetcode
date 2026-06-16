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
        result = []
        def inOrder(node: TreeNode, result: []):
            if not node:
                return
            
            inOrder(node.left, result)
            result.append(node.val)
            inOrder(node.right, result)
        inOrder(root, result)
        return result[k - 1]