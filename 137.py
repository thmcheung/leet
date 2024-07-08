class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ar = set(nums)
        k = set([])
        dic = {}
        for i in nums:
            try:
                dic[i] += 1
                k.add(i)
            except:
                dic[i] = 1
        return (ar - k).pop()