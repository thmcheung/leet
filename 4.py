class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ar = []
        count1 = 0
        count2 = 0
        while count1 < len(nums1) and count2 < len(nums2):
            if nums1[count1] > nums2[count2]:
                ar.append(nums2[count2])
                count2 += 1
            else:
                ar.append(nums1[count1])
                count1 += 1
        ar.extend(nums1[count1:] + nums2[count2:])
        return ar
                
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ar = self.merge(nums1, nums2)
        a = len(ar)
        if a % 2 == 1:
            return ar[a//2]
        else:
            return (ar[a//2] + ar[a//2 - 1]) / 2