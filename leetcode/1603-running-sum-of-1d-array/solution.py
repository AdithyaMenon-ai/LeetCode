class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=[]
        total=0
        for i in nums:
            total+=i
            lst.append(total)
        return lst
