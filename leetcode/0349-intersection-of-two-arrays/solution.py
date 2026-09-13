class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        nums2_set = set(nums2)
        for i in set(nums1):
            if i in nums2_set:
                lst.append(i)

        return lst 
        
