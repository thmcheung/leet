class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = path.split('/')
        ar = []
        for i in temp:
            if i:
                if i == '..':
                    if len(ar) > 0:
                        ar.pop()
                elif i != '.':
                    ar.append(i)
        ans = ''
        for i in ar:
            ans += '/' + i
        if ans == '':
            ans = '/'
        return ans