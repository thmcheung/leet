class Solution:
    def perm(self, length):
        ar = [i for i in range(length)]
        ans = []
        for i in range(length):
            for j in range(i+1, length):
                ans.append([i, j])
        return ans
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lst = []
        length = len(nums)
        ar = self.perm(length)
        nums.sort()
        for comb in ar:
            a, b = comb[0], comb[1]
            front, back = 0, length - 1
            while front != back:
                k = nums[a] + nums[b] + nums[front] + nums[back]
                if k > target:
                    back -= 1
                elif k < target:
                    front += 1
                else:
                    if front != a and back != a and front != b and back != b:
                        temp = [nums[a], nums[b], nums[front], nums[back]]
                        temp.sort()
                        if temp not in lst:
                            lst.append(temp)
                        front += 1
                    else:
                        front += 1
        return lst
                