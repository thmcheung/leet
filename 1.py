class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ar = nums + []
        ar.sort()
        low = 0
        high = len(ar) - 1
        while high > low:
            if ar[high] + ar[low] > target:
                high -= 1
            elif ar[high] + ar[low] < target:
                low += 1
            else:
                break
        i1 = None
        i2 = None
        if ar[high] == ar[low]:
            ans = []
            for i in range(len(ar)):
                if nums[i] == ar[high]:
                    ans.append(i)
            return ans[:2]
        else:
            for i in range(len(ar)):
                if nums[i] == ar[high]:
                    i1 = i
                elif nums[i] == ar[low]:
                    i2 = i
            return [i1, i2]