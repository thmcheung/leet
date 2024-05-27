class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate(1, n+1)

    def generate(self, low, high):
        ans = []
        for i in range(low, high):
            left = self.generate(low, i)
            right = self.generate(i+1, high)
            if len(left) == len(right) == 0:
                ans.append(TreeNode(i, None, None))
            elif len(left) == 0:
                for r in right:
                    root = TreeNode(i, None, r)
                    ans.append(root)
            elif len(right) == 0:
                for l in left:
                    root = TreeNode(i, l, None)
                    ans.append(root)
            else:
                for l in left:
                    for r in right:
                        root = TreeNode(i, l, r)
                        ans.append(root)
        return ans