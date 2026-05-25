# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSubset(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            return ((node1.val == node2.val) and 
            isSubset(node1.right, node2.right) and 
            isSubset(node1.left, node2.left))

        if not root:
            return False
        
        if not subRoot:
            return True 
        
        if isSubset(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.right, subRoot) or 
            self.isSubtree(root.left, subRoot))
        