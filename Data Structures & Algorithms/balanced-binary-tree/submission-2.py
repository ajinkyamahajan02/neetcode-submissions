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

            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            balanced = (left_len[0] and right_len[0] and 
                        abs(left_len[1] - right_len[1]) <= 1)
            
            return [balanced, 1 + max(left_len[1], right_len[1])]

        return dfs(root)[0]        