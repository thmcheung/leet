class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        high = 1
        low = 1
        ans = 0
        flag = 0
        for i in nums:
            if i == 0:
                high = 1
                low = 1
            else:
                temp_high = high
                high = max(high * i, i, low * i)
                low = min(temp_high * i, i, low * i)
                
                if high >= ans:
                    ans = high
                    flag = 1
        if flag == 0:
            ans = max(nums)
        return ans
            