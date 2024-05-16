#Binary Tree Zigzag Level Order Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        flag = 0
        ar = []
        this_layer = [root]
        next_layer = []
        values = 0
        while True:
            for node in this_layer:
                ar.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if flag == 0:
                ans.append(ar)
                flag = 1
            elif flag == 1:
                ans.append(ar[::-1])
                flag = 0
            ar = []
            this_layer = []
            if len(next_layer) == 0:
                break
            else:
                this_layer = next_layer
                next_layer = []
        return ans