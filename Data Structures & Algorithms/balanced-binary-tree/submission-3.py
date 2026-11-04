# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return [True, 0]

            left_res = dfs(node.left)
            right_res = dfs(node.right)

            balanced = (left_res[0] and right_res[0] and 
                        (abs(left_res[1] - right_res[1]) <= 1))

            return [balanced, 1 + (max(left_res[1], right_res[1]))]

        return dfs(root)[0]