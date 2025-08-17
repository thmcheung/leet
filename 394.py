class Solution:
    def decodeString(self, s: str) -> str:
        ans, i = self.iterate(s, 0)
        return ans
                
    
    def iterate(self, s: str, i):
        ans = ""
        while i < len(s):
            if s[i].isdigit():
                j = i + 1
                while s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                i = j
                a, index_now = self.iterate(s, i)
                ans += a * num
                i = index_now + 1
                continue
            if s[i] != "[" and s[i] != "]":
                ans += s[i]
            if s[i] == "]":
                return ans, i
            i += 1
        return ans, i