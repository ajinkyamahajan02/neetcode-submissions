# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        max_element = root.val
        res = 0

        def dfs(node, max_element):
            nonlocal res
            if not node:
                return 0

            if node.val >= max_element:
                res += 1
                max_element = node.val
            
            dfs(node.right, max_element)
            dfs(node.left, max_element)

        dfs(root, max_element)
        print(res)
        return res