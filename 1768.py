class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = 0
        j = 0
        flag = 0
        w1 = len(word1)
        w2 = len(word2)
        while True:
            if i < w1 and j < w2:
                if flag == 0:
                    ans += word1[i]
                    i += 1
                    flag = 1
                else:
                    ans += word2[j]
                    j += 1
                    flag = 0
            else:
                break
        if i < w1:
            ans += word1[i:]
        if j < w2:
            ans += word2[j:]
        return ans