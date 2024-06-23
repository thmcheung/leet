class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        ar = [[] for i in range(length)]
        for thing in richer:
            a = thing[0]
            b = thing[1]
            ar[b].append(a)
        #BFS
        final = []
        for i in range(length):
            loud = float('inf')
            ans = i
            current = [i]
            visited = [0 for _ in range(length)]
            while current:
                node = current.pop()
                if visited[node] == 0:
                    visited[node] = 1
                    if quiet[node] < loud:
                        loud = quiet[node]
                        ans = node
                    current.extend(ar[node])
            final.append(ans)
        return final