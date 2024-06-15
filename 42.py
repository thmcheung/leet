class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left = [-1 for i in range(l)]
        right = [-1 for i in range(l)]
        temp = -1
        for i in range(l):
            if height[i] > temp:
                temp = height[i]
            left[i] = temp
        temp = -1
        for i in range(l):
            if height[l-1-i] > temp:
                temp = height[l-1-i]
            right[l-1-i] = temp
        ans = 0
        for i in range(l):
            ans += min(left[i], right[i]) - height[i]
        return ans