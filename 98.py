# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.bruh(float('inf'), -float('inf'), root)

    def bruh(self, maximum, minimum, node):
        
        if minimum >= node.val or maximum <= node.val:
            return False
        if node.right:
            if not self.bruh(maximum, max(minimum, node.val), node.right):
                return False
        if node.left:
            if not self.bruh(min(maximum, node.val), minimum, node.left):
                return False
        return True