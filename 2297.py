from typing import List

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            flag = 0 #1: k < i; 2: k >= i
            for j in range(i + 1, n):
                if j - i == 1:
                    if dp[j] > costs[j] + dp[i]:
                        dp[j] = costs[j] + dp[i]
                    if nums[i] > nums[j]:
                        flag = 1
                    else:
                        flag = 2
                if (nums[i] <= nums[j] and flag == 1) or (nums[i] > nums[j] and flag == 2):
                    if dp[j] > costs[j] + dp[i]:
                        dp[j] = costs[j] + dp[i]
                    break
        return dp[n-1]