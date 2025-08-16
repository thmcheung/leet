# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        fake = TreeNode()
        self.inOrder(root, fake)
        return fake.right
        
    
    def inOrder(self, root, cur):
        if root.left:
            cur = self.inOrder(root.left, cur)
        cur.right = TreeNode(root.val)
        cur = cur.right
        if root.right:
            cur = self.inOrder(root.right, cur)
        return cur