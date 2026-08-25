class Solution:
    def climbStairs(self, n: int) -> int:
        befo2=1
        befo1=1
        
        for i in range(2,n+1):
            curr=befo2+befo1
            befo2=befo1
            befo1=curr
        return befo1
