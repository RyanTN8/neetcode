# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = ""
        def helper(root: Optional[TreeNode]) -> None:
            nonlocal result
            if not root:
                result += "N,"
                return
            result += str(root.val) + ","
            helper(root.left)
            helper(root.right)
        helper(root)
        return result

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        result = iter(data.split(","))
        def helper() -> Optional[TreeNode]:
            val = next(result)
            if val == 'N':
                return None
            else:
                return TreeNode(val, helper(), helper())
        return helper()
