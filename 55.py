class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        index = 0
        target = len(nums) - 1
        ans = 1
        while True:
            power = nums[index]
            if power == 0:
                return False
            if index + power >= target:
                break
            maximum = 0
            for i in range(index + 1, index + power + 1):
                if nums[i] + i > maximum:
                    maximum = nums[i] + i
                    temp = i
            index = temp
            ans += 1
        return True