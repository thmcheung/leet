class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        global visited
        visited = set()
        for i in wordDict:
            if i == s[:len(i)]:
                if self.build_trie(s, wordDict, i) == 0:
                    return True
        return False

    def build_trie(self, s, wordDict, word):
        s = s[len(word):]
        if len(s) == 0:
            return 0
        if s in visited:
            return 1
        else:
            for i in wordDict:
                if i == s[:len(i)]:
                    if self.build_trie(s, wordDict, i) == 0:
                        return 0
            visited.add(s)
            return 1