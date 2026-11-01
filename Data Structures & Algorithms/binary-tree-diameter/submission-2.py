# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(node):

            if not node: 
                return 0

            return 1 + max(maxDiameter, max(self.dfs(node.left), self.dfs(node.right)))

        dfs(root)