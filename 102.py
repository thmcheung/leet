# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ar = []
        stack = [root]
        temp = []
        nodes = []
        while stack:
            node = stack.pop()
            temp.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if not stack:
                ar.append(temp)
                while nodes:
                    stack.append(nodes.pop())
                temp = []
                nodes = []
        return ar