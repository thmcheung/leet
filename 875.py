import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = sum(piles) // h
        high = max(piles) + 1
        mid = (low + high) // 2
        ans = float('inf')
        while low < high:
            if self.check(piles, h, mid) == 0:
                ans = min(ans, mid)
                high = mid
            else:
                low = mid + 1
            mid = (high + low) // 2
        return ans
    
    def check(self, piles, h, k):
        if k == 0:
            return 2
        ans = 0
        for i in piles:
            if i % k == 0:
                ans += i // k
            else:
                ans += i // k + 1
        if ans <= h:
            return 0
        else:
            return 1