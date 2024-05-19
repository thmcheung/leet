class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        index = 0
        minimum = float('inf')
        cur = 0
        l = len(gas)
        for i in range(l):
            cur += gas[i] - cost[i]
            if cur < minimum:
                minimum = cur
                index = i
        if cur < 0:
            return -1
        return (index + 1) % l