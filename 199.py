# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        temp = [root]
        if not root:
            return []
        while True:
            if len(temp) == 0:
                break
            n = len(temp)
            for i in range(n):
                a = temp.pop(0)
                if a.left:
                    temp.append(a.left)
                if a.right:
                    temp.append(a.right)
                if i == n - 1:
                    ans.append(a.val)
        return ans