from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i].append(i)
        times.sort()
        ar = [0] * len(times)
        ans = [-1] * len(times)
        for i in range(len(times)):
            for j in range(len(times)):
                if ar[j] <= times[i][0]:
                    ar[j] = times[i][1]
                    ans[times[i][2]] = j
                    break
        return ans[targetFriend]