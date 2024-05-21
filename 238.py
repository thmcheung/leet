class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        for i in range(1, length):
            ans[i] = ans[i-1] * nums[i-1]
        temp = [1] * length
        for i in range(1, length):
            j = length - 1 - i
            temp[j] = temp[j+1] * nums[j+1]
        for i in range(length):
            ans[i] = temp[i] * ans[i]
        return ans