# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        ar.append(root)
        self.inorder(root.right)
    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        global ar
        ar = []
        self.inorder(root)
        for i in range(len(ar)-1):
            if ar[i] == p:
                return ar[i+1]
        return None