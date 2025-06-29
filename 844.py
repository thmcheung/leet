class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = s[::-1]
        t = t[::-1]
        cnt = 0
        new_s = ""
        for i in range(len(s)):
            if s[i] == "#":
                cnt += 1
            elif cnt == 0:
                new_s += s[i]
            else:
                cnt -= 1
        new_t = ""
        cnt = 0
        for j in range(len(t)):
            if t[j] == "#":
                cnt += 1
            elif cnt == 0:
                new_t += t[j]
            else:
                cnt -= 1
        return new_t == new_s