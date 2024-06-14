class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        for i in t:
            dic[i] = 0
        window = dic.copy()
        total = 0
        for i in t:
            dic[i] += 1
            if dic[i] == 1:
                total += 1
        left = 0
        right = 0
        ans = ""
        flag = 0
        length = 100000
        while left < len(s):
            if flag == total:
                try:
                    window[s[left]] -= 1
                    if window[s[left]] < dic[s[left]]:
                        flag -= 1
                except:
                    pass
                left += 1
            else:
                if right == len(s):
                    break
                try:
                    window[s[right]] += 1
                    if window[s[right]] == dic[s[right]]:
                        flag += 1
                except:
                    pass
                right += 1
            if flag == total and right + 1 - left < length:
                ans = s[left:right]
                length = right + 1 - left
        return ans