class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        path = []
        def dfs(i):
            if i == n and len(path) == 4:
                ans.append(".".join(map(str, path.copy())))
                return
            for j in range(i, n):
                string = s[i:j+1]
                if len(string) > 1 and string[0] == '0':
                    break
                if len(path) < 4 and int(string) <= 255:
                    path.append(string)
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return ans