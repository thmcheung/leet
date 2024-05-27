class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        last = None
        for i in range(l):
            front = 0
            back = l - 1
            if last == nums[i]:
                pass
            else:
                while front != back:
                    if nums[front] + nums[back] + nums[i] < 0:
                        front += 1
                    elif nums[front] + nums[back] + nums[i] > 0:
                        back -= 1
                    else:
                        if i != back and i != front:
                            lst = [nums[front], nums[back], nums[i]]
                            lst.sort()
                            if lst not in ans:
                                ans.append(lst)
                            back -= 1
                        elif i == back:
                            back -= 1
                        elif i == front:
                            front += 1
                    last = nums[i]
        return ans