# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {}
        for i, val in enumerate(inorder):
            hashMap[val] = i
        
        def dfs(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder:
                return None
            value = preorder[0]
            index = hashMap[value]

            leftpreorder = []
            rightpreorder = []
            leftinorder = inorder[:index]
            rightinorder = inorder[index + 1:]

            for num in preorder[1:]:
                if hashMap[num] < index:
                    leftpreorder.append(num)
                else:
                    rightpreorder.append(num)
            
            node = TreeNode(value, dfs(leftpreorder, leftinorder), dfs(rightpreorder, rightinorder))
            return node
        return dfs(preorder, inorder)

        
