# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        level = 0    

        def getLevel(node):
            if not node:
                return 0

            return [getLevel(node.left), getLevel(node.right)]

        self.levelOrder(root.left)
        selflevelOrder(root.right)    
        
