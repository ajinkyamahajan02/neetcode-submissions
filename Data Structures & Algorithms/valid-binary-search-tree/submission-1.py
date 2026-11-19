# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = True

        def dfs(node, left, right):
            nonlocal flag
            if not node:
                return True 

            if not left and not right:
                return True
            
            if not left:
                if node.val > left.val:
                    return True
                else:
                    flag = False
                    return False
            
            if not right:
                if node.val < right.val:
                    return True 
                else:
                    flag = False
                    return False

            elif left.val < node.val < right.val:
                return True 
            
            else: return False

            dfs(node, node.right, node.left)
        
        dfs(root)
        return flag
            
        