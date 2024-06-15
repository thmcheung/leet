class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        for i in range(len(s) - 1):
            if s[i] == s[i+1] == '0':
                return 0
        index = len(s) - 1
        visited = [0 for i in range(index + 1)]
        def recursion(index):
            if index <= 0:
                return 1
            if visited[index] != 0:
                return visited[index]
            ans = 0
            if s[index] == '0':
                if s[index - 1] != '0' and int(s[index - 1] + s[index]) <= 26:
                    ans += recursion(index - 2)
                else:
                    ans = -float('inf')
            else:
                ans += recursion(index - 1)
                if s[index - 1] != '0' and int(s[index - 1] + s[index]) <= 26:
                    ans += recursion(index - 2)
            visited[index] = ans
            if ans > 0:
                return ans
            return 0
        return recursion(index)
