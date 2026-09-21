class Solution:
    import math
    def findNumbers(self, nums: List[int]) -> int:
        tot=0
        for i in nums:
            if (math.floor(math.log10(i))+1)%2==0:
                tot+=1
        return tot


        
