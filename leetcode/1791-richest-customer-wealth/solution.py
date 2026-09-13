class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        for i in accounts:
            if sum(i)>maximum:
                maximum=sum(i)
        return maximum        
