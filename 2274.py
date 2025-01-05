class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = 0
        print(ans)
        ans = max(ans, special[0] - bottom)
        ans = max(ans, top - special[len(special)-1])
        for i in range(len(special) - 1):
            ans = max(ans, special[i+1] - special[i] - 1)
        return ans