class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ar = []
        dic = {}
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                ar.append(nums1[i] + nums2[j])
        for i in range(n):
            for j in range(n):
                try:
                    dic[nums3[i] + nums4[j]] += 1
                except:
                    dic[nums3[i] + nums4[j]] = 1
                
        ans = 0
        for num in ar:
            try:
                dic[-num] > 0
                ans += dic[-num]
            except:
                continue
        return ans