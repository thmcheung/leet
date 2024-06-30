class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        k = len(intervals)
        if k == 1:
            return intervals
        index = 0
        while index < k - 1:
            if intervals[index][1] >= intervals[index + 1][0]:
                intervals[index] = [intervals[index][0], max(intervals[index + 1][1], intervals[index][1])]
                del(intervals[index+1])
                k -= 1
            else:
                index += 1
        return intervals