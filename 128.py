class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        length = 1
        
        for num in nums:
            if num - 1 not in nums:
                cur = num
                length = 1
                while cur + 1 in nums:
                    cur += 1
                    length += 1
            ans = max(ans, length)
        
        return ans