class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return []
        ar1 = [root]
        ar2 = []
        temp = [] #for each level
        while True:
            if ar1:
                node = ar1.pop(0)
                if node.left:
                    ar2.append(node.left)
                if node.right:
                    ar2.append(node.right)
                temp.append(node.val)
            if not ar1:
                ans.append(temp)
                temp = []
                if not ar2:
                    return ans[::-1]
                while ar2:
                    ar1.append(ar2.pop(0))