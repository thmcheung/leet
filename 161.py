class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t) == 0:
            return False
        if len(s) == len(t):
            cnt = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    cnt += 1
            if cnt == 1:
                return True
            else:
                return False
        if len(s) + 1 == len(t):
            j = 0
            cnt = 0
            for i in range(len(s)):
                if s[i] != t[j]:
                    if cnt == 1:
                        return False
                    j += 1
                    cnt = 1
                    if s[i] != t[j]:
                        return False
                j += 1
            return True
        if len(s) == len(t) + 1:
            j = 0
            cnt = 0
            for i in range(len(t)):
                if t[i] != s[j]:
                    if cnt == 1:
                        return False
                    j += 1
                    cnt = 1
                    if t[i] != s[j]:
                        return False
                j += 1
            return True
        return False