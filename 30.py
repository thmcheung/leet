class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        dic = {}
        l = len(words)
        k = len(words[0])
        length = l * k
        it = len(s) - length
        for i in words:
            dic[i] = 0
        bro = dic.copy()
        for i in words:
            bro[i] += 1
        for i in range(it + 1):
            temp = dic.copy()
            start = i
            end = i + k
            for j in range(l):
                try:
                    temp[s[start:end]] += 1
                except:
                    break
                start = end
                end = start + k
            if temp == bro:
                ans.append(i)
        return ans