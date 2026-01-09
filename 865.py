# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        global dic
        dic = {}
        deepest = self.recursion(root, 0)
        a = self.answer(root, deepest)
        return a
        
    
    def recursion(self, root, cur):
        cur += 1
        depth = 0
        if not root.right and not root.left:
            dic[root] = cur
            return cur
        if root.right:
            depth = max(depth, self.recursion(root.right, cur))
        if root.left:
            depth = max(depth, self.recursion(root.left, cur))
        dic[root] = depth
        return depth
    
    def answer(self, root, deepest):
        if root.left and root.right:
            if dic[root.left] == deepest and dic[root.right] == deepest:
                return root
            if dic[root.left] == deepest:
                return self.answer(root.left, deepest)
            if dic[root.right] == deepest:
                return self.answer(root.right, deepest)
        if root.left:
            return self.answer(root.left, deepest)
        if root.right:
            return self.answer(root.right, deepest)
        return root