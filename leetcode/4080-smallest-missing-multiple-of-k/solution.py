class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while True:
            multi=i*k
            if multi not in nums:
                return multi
            i+=1

        
