class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = len(nums)
        ar = [0 for i in range (k + 1)]
        for i in nums:
            if 0 < i < k + 1:
                ar[i] = 1
        for i in range(1, k+1):
            if ar[i] == 0:
                return i
        return k + 1