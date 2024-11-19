# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if root:
            self.dfs(root, targetSum, 0, [], ans)
        return ans


    def dfs(self, root, targetSum, cur, path, ans):
        cur += root.val
        ar = path.copy()
        ar.append(root.val)
        if (not root.left) and (not root.right):
            if cur == targetSum:
                print(path)
                ans.append(ar)
                return
            else:
                return
        if root.left:
            self.dfs(root.left, targetSum, cur, ar, ans)
        if root.right:
            self.dfs(root.right, targetSum, cur, ar, ans)
                
