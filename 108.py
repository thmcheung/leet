# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        def create_tree(nums):
            mid = len(nums) // 2
            root = TreeNode(nums[mid], None, None)
            if mid > 0:
                left_tree = create_tree(nums[:mid])
                root.left = left_tree
            if mid < len(nums) - 1:
                right_tree = create_tree(nums[mid+1:])
                root.right = right_tree
            return root
        root = create_tree(nums)
        return root