class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        big = max(nums)
        small = min(nums)
        for i in range(len(nums)):
            if nums[i] == small:
                start = i
                break
        for i in range(len(nums)):
            if nums[i] == big:
                end = i
        ans = start + len(nums) - 1 - end
        if start > end:
            ans -= 1
        return ans