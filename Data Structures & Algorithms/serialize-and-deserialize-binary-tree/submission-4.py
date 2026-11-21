# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        inorder = []
        preorder = []

        def dfs(node):
            nonlocal preorder
            if not node:
                return 

            preorder.append(node.val)
            dfs(node.left)
            dfs(node.right)

        def inorderdfs(node):
            nonlocal inorder
            if not node:
                return 

            inorderdfs(node.left)
            inorder.append(node.val)
            inorderdfs(node.right)
            
            
        dfs(root)
        inorderdfs(root)
        
        txt = ""
        for element in preorder:
            txt += str(element) + " "
        
        txt += ";"

        for element in inorder:
            txt += str(element) + " "

        return txt

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        inorder_str, preorder_str = data.split(";")
        inorder = inorder_str.split()
        preorder = preorder_str.split()
        inorder = [int(x) for x in inorder]
        preorder = [int(x) for x in preorder]

        def dfs(preorder, inorder):
            if not inorder or not preorder:
                return 

            val = preorder[0]
            mid = inorder.index(val)
            node = TreeNode(val)

            node.left = dfs(preorder[1:mid+1], inorder[:mid])
            node.right = dfs(preorder[mid+1:], inorder[mid+1:])

            return node
        root = dfs(inorder, preorder)
        return root