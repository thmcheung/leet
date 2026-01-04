class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2
        global dp
        dp = [[0 for i in range(target + 1)] for i in range(len(nums))]
        dp[0][0] = 1
        for i in range(len(nums)):
            for j in range(target + 1):
                if j >= nums[i]:
                    if dp[i - 1][j - nums[i]] == 1:
                        dp[i][j] = 1
                if dp[i - 1][j] == 1:
                    dp[i][j] = 1
        return dp[len(nums) - 1][target] == 1