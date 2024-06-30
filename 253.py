import heapq
    
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key= lambda x: x[0])
        cnt = 1
        ar = [intervals[0][1]]
        for interval in intervals[1:]:
            if interval[0] >= ar[0]:
                heapq.heappush(ar, interval[1])
                heapq.heappop(ar)
            else:
                heapq.heappush(ar, interval[1])
                cnt += 1
        return cnt