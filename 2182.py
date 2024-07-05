class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        dic = {}
        for i in s:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        ar = list(dic.keys())
        ar.sort(reverse = True)
        index = 0
        flag = 0
        ans = ''
        while True:
            if len(ans) == len(s):
                return ans
            if dic[ar[index]] > 0 and flag < repeatLimit:
                ans += ar[index]
                dic[ar[index]] -= 1
                flag += 1
            elif dic[ar[index]] == 0:
                index += 1
                flag = 0
            elif flag == repeatLimit:
                prev = index
                index += 1
                if index >= len(ar):
                    return ans
                while dic[ar[index]] == 0:
                    index += 1
                    if index >= len(ar):
                        return ans
                ans += ar[index]
                dic[ar[index]] -= 1
                index = prev
                flag = 0
        return ans