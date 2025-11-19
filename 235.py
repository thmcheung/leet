# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(root):
            cnt = 0
            if root == p or root == q:
                cnt += 1
            if root.left:
                a = func(root.left)
                if type(a) is int:
                    cnt += a
                else:
                    return a
            if root.right:
                b = func(root.right)
                if type(b) is int:
                    cnt += b
                else:
                    return b
            if cnt == 2:
                return root
            return cnt
        return func(root)