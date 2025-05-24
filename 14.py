class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = max(strs)
        b = min(strs)
        index = 0
        k = min(len(a), len(b))
        for i in range(k):
            if a[i] == b[i]:
                index += 1
            else:
                return a[:index]
        return a[:index]