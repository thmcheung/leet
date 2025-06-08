from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        temp_sum = 0
        ar = [0] * len(nums)
        for i in range(len(nums)):
            temp_sum += nums[i]
            if nums[i] == 0:
                temp_sum -= 1
            ar[i] = temp_sum
        #find furthest apart same number begin with 0 at index -1
        big_dic = {}
        small_dic = {}
        ans = 0
        small_dic[0] = -1
        for i in range(len(ar)):
            if ar[i] not in small_dic:
                small_dic[ar[i]] = i
            else:
                ans = max(ans, i - small_dic[ar[i]])
        return ans