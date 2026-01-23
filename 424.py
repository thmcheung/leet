class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s) + 1:
            return len(s)
        left = 0
        right = 0
        dic = {}
        ans = k
        while right <= len(s) - 1:
            try:
                dic[s[right]] += 1
            except:
                dic[s[right]] = 1
            cur_val = max(list(dic.values()))
            if right - left - cur_val + 1 > k:
                dic[s[left]] = dic[s[left]] - 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans