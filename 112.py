# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def dfs(node, targetSum, cur):
            cur += node.val
            if node.left is None and node.right is None:
                if cur == targetSum:
                    return True
            if node.left:
                if dfs(node.left, targetSum, cur):
                    return True
            if node.right:
                if dfs(node.right, targetSum, cur):
                    return True
            return False

        return dfs(root, targetSum, 0)